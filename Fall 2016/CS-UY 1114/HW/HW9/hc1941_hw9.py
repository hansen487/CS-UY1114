"""
CS-UY 1114
Hansen Chen
Katz
hc1941 N11730096
Print stops of MTA lines
"""

def create_dictionary(filename):
    file = open(filename, 'r')
    file.readline()
    dictionary = {}
    for line in file:
        line = line.split(sep = ",")
        stop_id = line[0]
        train_line  = stop_id[0]
        stop_name = line[2]
        if stop_name in dictionary:
            train_line += dictionary[stop_name] + train_line
        dictionary[stop_name] = train_line
    file.close()
    return dictionary

def print_train_stops(dictionary, train_line):
    stops = train_line + ' line: '
    for key in dictionary:
        if (train_line in dictionary[key]):
            stops += key + ', '
    stops = stops[0:len(stops) - 2]
    return stops

def main():
    filename = input("Enter a filename to open: ")
    dictionary = create_dictionary(filename)
    train_line = input("Please enter a train line, or 'done' to stop: ")
    while (train_line != 'done'):
        stops = print_train_stops(dictionary, train_line)
        print(stops)
        train_line = input("Please enter a train line, or 'done' to stop: ")
main()
