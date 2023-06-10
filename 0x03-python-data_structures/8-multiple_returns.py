#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    length = len(sentence)
    return length, sentence[0]
