'''
Dominic Smith <domlucasmith@gmail.com>
Sentiance Assignment 1.1
'''

import os, sys
import re
import logging

from datasets.Datasets import Datasets
from core.Parser import args

args_dict = vars(args)
logging.basicConfig(level = logging.getLevelName(args.logging_level))
##__________________________________________________________________||
def main():

    dataset = Datasets(**args_dict)
    dataset.backupWorkspace()

##__________________________________________________________________||    
if __name__ == '__main__':
    main()
