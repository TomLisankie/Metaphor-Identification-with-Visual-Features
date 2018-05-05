import gzip
import msgpack
from gensim.models import word2vec, Word2Vec

fin = gzip.open('../data/wikipedia.msgpack.gz', 'rb')
unpacker = msgpack.Unpacker(fin, encoding='utf-8')

i = 0
sentence_list = []
for sentence in unpacker:
    sentence_list.append(sentence[1])

word2vec_model = Word2Vec(sentences=sentence_list, sg=1, size=100, window=5, min_count=100, negative=10, iter=3)

fin.close()