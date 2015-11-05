__author__ = 'tangy'

# -*- coding: utf-8 -*-

import re
import string


TOY_FLAG = False

#NUM_UTTERANCES = 2908
TOY_UTTERANCES = 20




def clean(utterance, utterance_labels):
    cleaned_x=[]
    cleaned_y=[]
    num_utter=len(utterance)

    for id in xrange(num_utter):
        utter_x=[]
        utter_y=[]
        utter_labels_tokens = utterance_labels[id].split()
        utter_tokens=utterance[id].split()
        try:
            assert(len(utter_tokens) == len(utter_labels_tokens))
        except:
            print "Length mismatch b/w labels and utter. Continuing..."
            #print id
            continue

        for i in xrange(len(utter_labels_tokens)):
            [x.decode('UTF-8') for x in utter_tokens]
            if not (utter_labels_tokens[i]=='X' or utter_tokens[i].isdigit() or utter_labels_tokens[i].startswith('NE')or utter_labels_tokens[i].startswith('MI')or utter_labels_tokens[i].startswith('X')or utter_labels_tokens[i].startswith('O')or utter_labels_tokens[i].startswith('N')):
                if not re.search(r'[.]+',utter_tokens[i]):
                    try:
                        utter_x.append(utter_tokens[i])
                        utter_y.append(utter_labels_tokens[i])
                    except:
                        continue
        try:
            assert(len(utter_x) == len(utter_y))
        except AssertionError:
            print 'Another mishap!'
            continue
        sentence_x=(' '.join(utter_x))
        sentence_x=re.sub(r'[@#;,"().*!?:\/\\-]','',sentence_x)
        sentence_x=re.sub(r'[_\']','',sentence_x)
        try:
            assert(len(sentence_x.split())==len(utter_y))
        except AssertionError:
            print 'Final mishap!'
            #print id
            continue
        cleaned_x.append(sentence_x)
        cleaned_y.append(' '.join(utter_y))
    return cleaned_x,cleaned_y


def get_data(path):
    # Getting Training data in dataset
    with open(path,'r') as ip:
        xml_str = ip.read()
        id_list = map(int,re.findall(r'id="(\d+)"',xml_str))
        utter_list = re.findall(r'id="\d+">\s*(.*)\s*</',xml_str)
        assert len(id_list) == len(utter_list),"Mismatch in count of ids and utterances"
        return id_list,utter_list

def getXs():
    # Creating list of acronyms
    with open('./Resources/AcroNew2.txt','r') as ip:
        acronyms = ip.read().split()
    # Other Disallowed components
    punct = set(string.punctuation)
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return acronyms, punct, nums