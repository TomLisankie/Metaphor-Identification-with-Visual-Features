import gzip
import msgpack
from gensim.models import Word2Vec, word2vec
from gensim.models.callbacks import CallbackAny2Vec

the_file = gzip.open("../data/wikipedia.msgpack.gz", "rb")
unpacker = msgpack.Unpacker(the_file, encoding = "utf-8")

class WikiLemmaIterable(object):
    # Iterable for all lemmatized sentences in the corpus
    def __iter__(self):
        i = 0
        for sentence in unpacker:
            yield sentence[1]
            if i % 10000 == 0:
                print("Yielded 10,000 more sentences. Total yielded is at", i)
            i += 1

class BatchLogger(CallbackAny2Vec):
    def __init__(self):
        self.batch = 0
    def on_batch_begin(self, model):
        print("Batch #{} start".format(self.batch))
    def on_batch_end(self, model):
        print("Batch #{} end".format(self.batch))
        self.batch += 1

class EpochLogger(CallbackAny2Vec):
    def __init__(self):
            self.epoch = 0
    def on_epoch_begin(self, model):
        print("Epoch #{} start".format(self.epoch))
    def on_epoch_end(self, model):
        print("Epoch #{} end".format(self.epoch))
        self.epoch += 1

wiki_iterable = WikiLemmaIterable()
batch_logger = BatchLogger()
epoch_logger = EpochLogger()

word2vec_model = Word2Vec(sentences=wiki_iterable, sg=1, size=100, window=5, min_count=100, workers=32, hs=0,
                            negative=10, iter=3, callbacks=[batch_logger, epoch_logger])

word2vec_model.train(wiki_iterable, total_examples=len(wiki_iterable), epochs=3)

word2vec_model.save("../data/word2vec_model")

the_file.close()