#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    if (lenght == 0):
        return(lenght, None)
    first = sentence[0]
    return(lenght, first)
