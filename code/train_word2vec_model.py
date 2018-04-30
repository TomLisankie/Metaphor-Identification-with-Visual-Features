from gensim.models import Word2Vec
import gzip
import msgpack

data = gzip.open('../data/wikipedia.msgpack.gz', 'rb')
unpacked_data = msgpack.Unpacker(data, encoding='utf-8')


for i, sent in enumerate(unpacked_data):
    print(sent[1])
    if i > 100: break

data.close()