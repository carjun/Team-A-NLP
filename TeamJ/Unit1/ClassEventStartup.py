from __future__ import division
import nltk
from nltk.book import *
import dateutil
import pyparsing
import numpy
import six
import matplotlib
import os
from nltk.corpus import PlaintextCorpusReader
wordlists = PlaintextCorpusReader("../CollectionSmall", '.*')
# The next step is to show the file names under the directory (optional step)
wordlists.fileids()
ClassEvent = nltk.Text(wordlists.words())