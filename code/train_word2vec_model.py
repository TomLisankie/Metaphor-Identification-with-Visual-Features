from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import gzip
import msgpack

data = gzip.open('../data/wikipedia.msgpack.gz', 'rb')
unpacked_data = msgpack.Unpacker(data, encoding='utf-8')

for i, sent in enumerate(unpacker):
    print(' '.join(sent[1]))
    print(str(sent[3])+'\n')
    if i > 9: break

sentences = LineSentence('../data/wikipedia.msgpack.gz')

model = Word2Vec(sentences = sentences, sg = 1, size = 100, window = 5, negative = 10, iter = 3)

data.close()