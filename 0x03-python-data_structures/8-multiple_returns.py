#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        le = len(sentence)
    else:
        le = 0
    return (le, sentence if not sentence else sentence[:1])
