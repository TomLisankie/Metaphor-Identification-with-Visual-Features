import gzip
import msgpack
from gensim.models import word2vec, Word2Vec

fin = gzip.open('../data/wikipedia.msgpack.gz', 'rb')
unpacker = msgpack.Unpacker(fin, encoding='utf-8')

i = 0
sentence_list = []
for sentence in unpacker:
    sentence_list.append(sentence[1])
    if i % 10000 == 0:
        print("Appended 10000 more, currently at", i)
    i = i + 1

print("Started Initializing Word2Vec Model")
word2vec_model = Word2Vec(sentences=sentence_list, sg=1, size=100, window=5, min_count=100, negative=10, workers=32)
print("Finished Initializing Word2Vec Model")

print("Started Training Word2Vec Model")
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.start()

def check_in():
    print "1 Minute has passed"

sched.add_interval_job(check_in, seconds = 60)

word2vec_model.train(sentence_list, total_examples=len(sentence_list), epochs=3)
sched.shutdown()
print("Finished Training Word2Vec Model")

print("Started Saving Word2Vec Model")
word2vec_model.save("../data/word2vec_model")
print("Finished Saving Word2Vec Model")

fin.close()