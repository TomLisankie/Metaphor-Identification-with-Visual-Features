# Parsed Wikipedia dump #

This corpus was prepared by Jean Maillard (jm864). Feel free to contact
<jean@maillard.it> should you have any questions about it.

## Source ##

Source dump: <https://dumps.wikimedia.org/enwiki/20150805/enwiki-20150805-pages-articles.xml.bz2>

The XML dump was processed using the `WikiExtractor.py` script found in this
directory. The original script was written by Giuseppe Attardi and can
be found at <https://github.com/attardi/wikiextractor>. I modified it slightly
to get rid of XML markup of documents, and so that it would not output article
headings.

After processing, the text was < 10 GB.

## Parser ##

I used Stanford CoreNLP version 3.5.2, with the following options:
        -annotators tokenize,ssplit,pos,lemma,depparse -outputFormat json

I then used the `convert_stanford_json.py` script to turn it into a more useful
representation, and save it in MessagePack format (see <http://msgpack.org>).

## How to use ##

The parsed corpus can be found in the `wikipedia.msgpack.gz` file, and contains
72839472 sentences.

The compressed file weighs 15 GB, while the uncompressed file weighs 56 GB.

### Format ###

The file `wikipedia.msgpack.gz` contains a streamable set of MessagePack objects
for every sentence, in the format:

    {
        [ word1, word2, word3, ... ],
        [ lemma1, lemma2, lemma3, ... ],
        [ pos1, pos2, pos3, ... ],
        [ ( basic_gr1, head1, dep1), (basic_gr2, head2, dep2), ... ],
        [ ( enhanced_gr1, head1, dep1), (enhanced_gr2, head2, dep2), ... ]
    }

MessagePack was used a serialisation format because it is much faster than
Python's Pickle format, streamable (so we do not need to load the
whole file in memory), and compact. Libraries are also available for all major
languages.

The GRs used are Universal Dependencies. The first set are the standard basic
dependencies, while the second set are the collapsed dependencies. For more
information see <http://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/trees/GrammaticalStructure.Extras.html>. `headN` and `depN` are the positions of head and dependent words in the sentence, 1-indexed (0 represents the ROOT).

### Python example ###

This is a Python example that loops through the sentences and prints the lemmas
and basic GRs for the first 10.

    import gzip
    import msgpack

    fin = gzip.open('wikipedia.msgpack.gz', 'rb')
    unpacker = msgpack.Unpacker(fin, encoding='utf-8')

    for i, sent in enumerate(unpacker):
        print(' '.join(sent[1]))
        print(str(sent[3])+'\n')
        if i > 9: break

    fin.close()

The first two lines of output, corresponding to the first sentence, are:

    Anarchism be a political philosophy that advocate stateless society often define as self-governed voluntary institution , but that several author have define as more specific institution base on non-hierarchical free association .
    [['ROOT', 0, 5], ['nsubj', 5, 1], ['cop', 5, 2], ['det', 5, 3], ['amod', 5, 4], ['nsubj', 7, 6], ['acl:relcl', 5, 7], ['amod', 9, 8], ['dobj', 7, 9], ['advmod', 11, 10], ['dep', 7, 11], ['case', 15, 12], ['amod', 15, 13], ['amod', 15, 14], ['nmod', 11, 15], ['punct', 5, 16], ['cc', 5, 17], ['mark', 22, 18], ['amod', 20, 19], ['nsubj', 22, 20], ['aux', 22, 21], ['conj', 5, 22], ['case', 26, 23], ['amod', 26, 24], ['amod', 26, 25], ['nmod', 22, 26], ['acl', 26, 27], ['case', 31, 28], ['amod', 31, 29], ['amod', 31, 30], ['nmod', 27, 31], ['punct', 5, 32]]

### Other languages ###

There are MessagePack libraries for most languages.

* C/C++: <https://github.com/msgpack/msgpack-c>
* C#/CLI: <https://github.com/msgpack/msgpack-cli>
* Java: <https://github.com/msgpack/msgpack-java>
* Lua: <https://github.com/fperrad/lua-MessagePack>
* Python: <https://pypi.python.org/pypi/msgpack-python>
