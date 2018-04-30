#!/usr/bin/env python3

import argparse
import json
import msgpack

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Stanford CoreNLP JSON file', nargs='+')
parser.add_argument('output', help='adjectives')
args = parser.parse_args()

with open(args.output, 'ab') as fout:
    for infile in args.input:
        with open(infile, 'r') as fin:
            sentences = json.load(fin)['sentences']
        for sentence in sentences:
            words, lemmas, tags = list(zip(*((t['word'],t['lemma'],t['pos'])
                for t in sentence['tokens'])))
            basic_deps = [(d['dep'],int(d['governor']),int(d['dependent']))
                    for d in sentence['basic-dependencies']]
            enhanced_deps = [(d['dep'],int(d['governor']),int(d['dependent']))
                    for d in sentence['collapsed-ccprocessed-dependencies']]
            if len(words) == len(lemmas) == len(tags):
                msgpack.dump((words,lemmas,tags,basic_deps,enhanced_deps), fout)
