
"""
Hofai Tang
ht944
"""
def print_stops(filename, user_input):
    file = open(filename, "r")
    line = file.readline()
    stops = []
    for line in file:
        line = line.split(",") 
        stop_id = line[0]
        if(user_input == stop_id[0]):    
            stops.append(line[2])
    if (stops != []):
        stops1 = user_input + " line: " 
        for i in range (len(stops) - 1):
            if(stops[i] != stops[i+1]):
                stops1 += stops[i] + ", " 
        stops1 = stops1[0:len(stops1) - 2]
        print(stops1, end="") 
    else:
        print("This train does not exist")
    print("\n")
    file.close()
                       
def main():
    inp = input("Please enter a train line, or 'done' to stop: ")
    while (inp != "done"):
        print_stops("hw9 - mta train stop data.csv", inp)
        inp = input("Please enter a train line, or 'done' to stop: ")
main()
