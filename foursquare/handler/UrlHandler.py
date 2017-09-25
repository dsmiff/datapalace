# Dominic Smith <domlucasmith@gmail.com>

import urllib2
import json
import pandas as pd
from pandas.io.json import json_normalize
import os
import time

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 4096)
pd.set_option('display.max_rows', 65536)
pd.set_option('display.width', 1000) 

##__________________________________________________________________||    
class UrlHandler(object):
    def __init__(self, client_id, client_secret, category_id, coords, accuracy):
        self.client_id = client_id
        self.client_secret = client_secret
        self.category_id = category_id
        pass

    def make_request(self,url):
        '''
        Makes a new HTTP request to the given URL
        
        :param url: The URL to request
        :returns: JSON response that will be transformed to a pandas DataFrame
        '''

        try:            
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            data = json.loads(response.read())
            response.close()
            return data
        
        except Exception, e:
            print e

    def convertToDataFrame(self, data, requested_keys):
        data = pd.DataFrame(data["response"]['venues'])[requested_keys]
        writeDFtoFile(data, None, './', 'Venues', True)
        return data
    
    def analyseDataFrame(self, data, sigma, requested_keys):
        self.venueIds = []
        self.frames = []
        for d in data['id']:
            # Pass each id into API
            url2 = "https://api.foursquare.com/v2/venues/%s?client_id=%s&client_secret=%s&v=%s" % (d, self.client_id, self.client_secret, time.strftime("%Y%m%d"))
            sub_data = self.make_request(url2)
            id_data = sub_data['response']               
            nom_data = json_normalize(id_data['venue'])
            
            print 'List of possible venues: ',  id_data['venue']['name']
            self.venueIds.append(d)

            if "rating" not in nom_data.columns:
                nom_data["rating"] = 'NONE'                 
                
            self.frames.append(nom_data[requested_keys])

    def mapCoordsToVenue(self):
        '''
        The location of a venue is given by its latitude and longitude.
        Assume the distribution of the latitude and longitude is Gaussian and centered at their
        nominal value. The width of each Gaussian is determined by the standard
        deviation. 
        Depending on the value of the lat/long the standard deviation can be determined 
        in metres (assuming 1 degree equals 111 km).
        Using the accuracy argument and the standard deviation, it should 
        be possible to filter out venues.
        '''
        pass
            
##__________________________________________________________________||
def writeDFtoFile(tbl, variable, dir, prefix=None, force=False):
    '''
    Write a produced DataFrame to a txt file 
    given a variable name and output directory
    '''

    if variable is None: variable = 'out'
    if not os.path.exists(dir): os.makedirs(dir)

    tblName = os.path.join(dir,'tbl_n{}_{}.txt'.format(prefix, variable))
    if force and os.path.exists(tblName): os.remove(tblName)

    with open(tblName,'a') as f:
        tbl.to_string(f, index=True)
        f.write('\n')
        f.close()
        print('DataFrame {} written to file'.format(tblName))

##__________________________________________________________________||        
def meter_to_coord(p, d, lat_m, long_m):
    lat = p['lat']
    long = p['long']

    lat1 = lat + lat_m * (d / (11100.0/90*1000) * cos(lat))
    long1 = long + long_m * (d / (11100.0/90*1000))

    return {'lat': lat1, 'long': long1}
