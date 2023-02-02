#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "JungHwan Ryu"
__copyright__ = "Copyright 2023, IPXACT project"
__credits__ = ["JungHwan Ryu"]
__license__ = "GPL"
__date__ = "2023.02.02"
__version__ = "0.0.1"
__maintainer__ = "JungHwan Ryu"
__email__ = "kypilop@gmail.com"
__status__ = "NA"



import os, sys, json
import guessDef
from collections import OrderedDict


class guessDef:
    def __init__(self, jsonin):
        self.sorted_js = OrderedDict(sorted({j: i for i, j in jsonin.items()}.items()))
        self.jsin = jsonin

    def __repr__(self):
        return list(self.jsin)


guessDef({2:"E", 9:"WER", 0:"ZXC"})
