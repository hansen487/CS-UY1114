# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:32:52 2016

@author: Hansen
"""

def print_stations(filename, inp):
    file = open(filename, 'r')
    dictionary = {}
    file.readline()
    for line in file:
        new_line = line.split(",")
        stop = new_line[0][0]
        if new_line[2] in dictionary:
            stop += dictionary[new_line[2]]
        dictionary[new_line[2]] = stop
    stops = inp + ' line: '
    for key in dictionary:
        if (inp in dictionary[key]):
            stops += key + ', '
    stops = stops[0:len(stops) - 2]
    return stops
          
def main():
    file = 'hw9 - mta train stop data.csv'
    line = input("Please enter a train line, or 'done' to stop: ")
    while (line != 'done'):
       print(print_stations(file, line))
       line = input("Please enter a train line, or 'done' to stop: ")
    
main()