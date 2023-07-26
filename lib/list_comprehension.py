#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [number for number in num_list if number % 2 == 0]
    return new_list
        

def make_exclamation(sentence_list):
    new_sentence_list = [sentence + "!" for sentence in sentence_list]
    return new_sentence_list