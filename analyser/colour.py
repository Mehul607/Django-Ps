import re
from annotator import run_demo

def colour_coder(sentence):
    wordslist=sentence.split()
    langlist=run_demo(sentence).split()
    print langlist
    wordslist=zip(wordslist,langlist)
    print wordslist
    return wordslist