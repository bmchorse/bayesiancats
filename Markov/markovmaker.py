#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Markov-chain text maker

# Modified from https://github.com/robincamille/bot-tutorial/
# blob/master/mashup_markov
# Which in turn was modified from:
#  http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
# Original MarkovGen library from https://github.com/mattspitz/markovgen;
# modified by RobinCamille to spit out smaller chunks


# This script takes a .txt file and makes a mashup of it
# using a Markov chain: linking word phrases together
# from different spots in the text.

# For instance, if the text contained two lines,
# "she has a dog" and "my dog has a tail,"
# this might generate "my dog has a dog" and "she has a tail."


# Housekeeping
import markovgen
import re
import string


# Choose original file, new filename
original = open('bayesiancats.txt')
outfile = open('bayesiantweets.txt', 'w')


# Repeatable Markov'd text generator
newtext = []
mk = markovgen.Markov(original)

counter = 0
while counter < 10:  # Change 10 to however many lines you want to generate
    line = '\n' + mk.generate_markov_text()

    # remove punctuation
    exclude = ['"', '(', ')', ';']
    line = ''.join(ch for ch in line if ch not in exclude)

    # make line lowercase, add period at end
    line = line.lower() + "."

    print(line)
    newtext.append(line)
    counter = counter + 1


for aline in newtext:
    outfile.write(aline)  # makes text file line by line


# next steps if you want to tweet these lines:
# move the newly-made file into the mybot folder
# open mybot2.py
# insert new filename


outfile.close()
original.close()
