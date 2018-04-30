import gzip
import msgpack

fin = gzip.open('wikipedia.msgpack.gz', 'rb')
unpacker = msgpack.Unpacker(fin, encoding='utf-8')

for i, sent in enumerate(unpacker):
    print(' '.join(sent[1]))
    print(str(sent[3])+'\n')
    if i > 9: break

fin.close()