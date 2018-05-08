from gensim.models import Word2Vec, word2vec
from gensim.models.callbacks import CallbackAny2Vec

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

model = Word2Vec.load("../data/word2vec_model")

print(model.wv.most_similar(positive="polite"))