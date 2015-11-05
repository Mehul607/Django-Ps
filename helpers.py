__author__ = 'tangy'

import cPickle as pkl
from copy import deepcopy
import re

def perform_or(y_lists):
    num_clfs = len(y_lists)
    num_samples = len(y_lists[0])
    y_pred = [0 for i in xrange(num_samples)]
    for clf_idx in xrange(num_clfs):
        y_pred = [y_pred[i] or y_lists[clf_idx][i] for i in xrange(num_samples)]
    return y_pred

def unpack_list(lst_lsts):
    unpacked_lst = []
    for lst in lst_lsts:
        unpacked_lst += lst
    return unpacked_lst

def dump_model(obj,name):
    f = open(name,"wb")
    pkl.dump(obj,f)
    f.close()

def load_model(name):
    f = open(name,"r")
    obj = pkl.load(f)
    f.close()
    return obj

def deconstructor(utter,utter_labels,todel):
    utter_labels = deepcopy(utter_labels)
    utter = deepcopy(utter)
    y_id_new = []
    for i in xrange(len(utter_labels)):
        y_id_temp = []
        for j in xrange(len(utter_labels[i])-1,-1,-1):
            if utter_labels[i][j] == todel:
                del utter[i][j]
                del utter_labels[i][j]
                y_id_temp.insert(0,j)
        y_id_new.append(y_id_temp)
    return utter, y_id_new, utter_labels

def reconstructor(utter_label,y_id_new,toadd):
    utter_label = deepcopy(utter_label)
    for i in xrange(len(y_id_new)):
        for j in xrange(len(y_id_new[i])):
            utter_label[i].insert(y_id_new[i][j],toadd)
    return utter_label

def check_x(word_token,nums,punct,acronyms):
    if not re.match(r'[^@]+@[^@]+\.[^@]+', word_token):
        email = False
    else:
        email = True
    if not re.match(r"(:|;|=)[-pPdD)\\3(/'|\]}>oO]+", word_token):
        smiley = False
    else:
        smiley = True
    return all(word_token[i] in punct for i in xrange(len(word_token))) or all(i in nums or i == '.' for i in word_token) or word_token.startswith('http://') or word_token.startswith('https://') or any(word.lower() == (word_token.lower()) for word in acronyms)  or word_token[0] in ['@','#'] or email or smiley

def run_cleanup(word_token,x_label):
        punct = ['!', '#', '"', '%', '$', "'", '&', ')', '(', '+', '*', '-', ',', '/', '.', ';', ':', '=', '<', '?', '>', '@', '[', ']', '\\', '_', '^', '`', '{', '}', '|', '~']
        numbers = [str(i) for i in xrange(10)]
        # This would work fine if other checks performed first (in order)
        if any(char in punct for char in word_token):
            # Cannot directly replace the following since if they are in isolation then problem
            if x_label == 'NX':
                for punch in punct:
                    word_token = word_token.replace(punch,"")
        return word_token