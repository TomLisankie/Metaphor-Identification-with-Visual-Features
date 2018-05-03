import gzip
import msgpack

fin = gzip.open('wikipedia.msgpack.gz', 'rb')
unpacker = msgpack.Unpacker(fin, encoding='utf-8')

for i, sent in enumerate(unpacker):
    print(sent[1])
    if i > 9: break

fin.close()