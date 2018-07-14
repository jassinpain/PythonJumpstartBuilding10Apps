#!/usr/bin/env python3
import os
import collections


def main():
    datafile = os.path.abspath('./data/datafile.csv')
    HouseData = collections.namedtuple('HouseData', get_csv_header(datafile))
    banner()


def banner():
    print('----------------------------------------------')
    print('              Real Estate App                 ')
    print('----------------------------------------------')

def load_data():
    print('Loading CSV real estate data from ... {}'.format(datafile), end=' ')
    #TODO this is a CSV so making it over simple I am sure but hey
    open(datafile, 'r') as fin:
       for id,line in enumerate(fin):
           if id == 0:
               continue
           else:
               HouseData.extend(line)
    print('... done')

def get_csv_header(datafile):
    print('Loading CSV real estate data from ... {} ... done'.format(datafile))
    #TODO this is a CSV so making it over simple I am sure but hey
    open(datafile, 'r') as fin:
       for id,line in enumerate(fin):
           if id == 0:
               print('Header: ' + line)
               file_header = line

        return file_header


def find_most_expensive_house(datafile):
    #TODO use HouseData to figure out most expensive house
    print('Most expensive house is: ' + line)

def find_least_expensive_house(datafile):
    #TODO use HouseData to figure out least expansive house
    print('Least expensive house is: ' + line)

def calculate_average_house(beds):
    if beds = 0:
    #TODO use HouseData to figure out averge house price
    avg_price = 1
    bed_count = 1
    bath_count = 0
    print('Average house: {}, {} bed, {} bath '.format(avg_price, bed_count, bath_count))



if __name__ == '__main__':
    main()