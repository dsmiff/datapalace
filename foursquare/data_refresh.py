'''
Dominic Smith <domlucasmith@gmail.com>
Sentiance Assignment 2.1
'''

import os, sys
import re
import time
import pandas as pd

from handler.UrlHandler import UrlHandler
from core.Parser import args

args_dict = vars(args)
##__________________________________________________________________||
client_id = ''
client_secret = ''
category_id = ''

##__________________________________________________________________||
def main(lat, long, distance):

    coords = {'lat': lat, 'long':long}
    accuracy = distance
    # Uncertainty on distance
    sigma = 0.68
    # P.O.I
    requested_keys = ["categories","id","location","name"]

    url = "https://api.foursquare.com/v2/venues/search?ll=%s,%s&intent=browse&radius=%s&categoryId=%s&client_id=%s&client_secret=%s&v=%s" % (coords["lat"], coords["long"], distance, category_id, client_id, client_secret, time.strftime("%Y%m%d"))
  
    data_object = UrlHandler(client_id, client_secret, category_id, coords, accuracy)
    data = data_object.make_request(url)
    # Convert out of API request to pandas DataFrame
    df = data_object.convertToDataFrame(data, requested_keys)
    data_object.analyseDataFrame(df, sigma, ["id","name", "likes.count"])
    
##__________________________________________________________________||    
if __name__ == '__main__':
    main(**args_dict)
