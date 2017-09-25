# Dominic Smith <domlucasmith@gmail.com>

import argparse

##__________________________________________________________________||
parser = argparse.ArgumentParser()
parser.add_argument('--lat', type = float, default = 40.7268, help = 'Input latitude')
parser.add_argument('--long', type = float, default = -73.9972, help = 'Input longitude')
parser.add_argument('--distance', type = int, default = 100, help = 'Measure of accuracy')
args = parser.parse_args()
