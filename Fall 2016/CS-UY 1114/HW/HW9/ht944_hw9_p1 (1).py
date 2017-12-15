
"""
Hofai Tang
ht944
"""
def train_data(train_data_filename):
    inp = ""
    while (inp != "done"):
        inp = str(input("Please enter a train line, or 'done' to stop: "))
        if(inp == "done"):
            return ""
        elif(inp == "A" or inp == "B" or inp == "C" or inp == "D" or inp == "E" or inp == "F" or inp == "G" or inp == "J" or inp == "L" or inp == "M" or inp == "N" or inp == "Q" or inp == "S" or inp == "Z" or inp == "1" or inp == "2" or inp == "3" or inp == "4" or inp == "5" or inp == "6" or inp == "7"):   
            print(inp + " line: " , end="")
            train = open(train_data_filename, "r")
            line = train.readline()
            stops = []
            for line in train:
                line2 = line.split(",")
                first = line2[0]   
                if(inp == first[0]):  
                    stop = line2[2]    
                    stops.append(str(stop))
            stops1 = ""  
            for i in range (len(stops)-1):
                if(stops[i] != stops[i+1]):
                    stops1 += str(stops[i]) + ", " 
                    num = len(stops1)
                    stops2 = stops1[0:num-2]
            print(stops2, end="") 
            train.close()
        else:
            print("This train does not exist")
        print("\n")
                       
def main():   
    train_data("hw9 - mta train stop data.csv")
main()