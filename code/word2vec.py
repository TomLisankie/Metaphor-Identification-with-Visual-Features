import gzip
import msgpack
from gensim.models import word2vec, Word2Vec

fin = gzip.open('../data/wikipedia.msgpack.gz', 'rb')
unpacker = msgpack.Unpacker(fin, encoding='utf-8')

i = 0
for sentence in unpacker:
    print(sentence[1])
    i+=1
    if i>9: break

word2vec_model = Word2Vec(sentences=word2vec.LineSentence(unpacker), sg=1, size=100, window=5, negative=10, iter=3)

fin.close()