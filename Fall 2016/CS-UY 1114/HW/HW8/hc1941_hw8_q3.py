'''

Hansen Chen
CS 1114
hc1941

Read weather values from a file and use them
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    old_file = open(complete_weather_filename, 'r')
    new_file = open(cleaned_weather_filename, 'w')
    for line in old_file:
        line = line.split(sep = ",")
        if line[0] != "\n":
            city = line[0]
            date = line[1]
            high = line[2]
            low = line[3]
            precipitation = line[8]
            if (precipitation.isalpha() == True):
                if (precipitation != 'Precipitation'):
                    precipitation = '0'
            data = city + "," + date + "," + high + "," + low + "," + precipitation
            new_file.write(data)
            new_file.write('\n')
    old_file.close()
    new_file.close()


# Part B
def f_to_c(f_temperature):
    c_temperature = round((float(f_temperature) - 32) * (5 / 9), 2)
    c_temperature = str(c_temperature)
    return c_temperature

def in_to_cm(inches):
    cm = round(float(inches) * 2.54, 2)
    cm = str(cm)
    return cm

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    old_file = open(imperial_weather_filename, 'r')
    new_file = open(metric_weather_filename, 'w')
    for line in old_file:
        line = line.split(sep = ',')
        city = line[0]
        date = line[1]
        if (line[2] == 'High'):
            high = line[2]
        else:
            high = f_to_c(line[2])
        if (line[3] == 'Low'):
            low = line[3]
        else:
            low = f_to_c(line[3])
        line[4]=line[4].strip('\n')
        if (line[4] == 'Precipitation'):
            precipitation = line[4]
        elif (line[4] != 'Precipitation' and line[4].isalpha() == True):
                precipitation = '0'
        else:
            precipitation = in_to_cm(line[4])
        data = city + "," + date + "," + high + "," + low + "," + precipitation
        new_file.write(data)
        new_file.write('\n')
    old_file.close()
    new_file.close()


# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    file = open(weather_filename, 'r')
    date = []
    high = []
    low = []
    for line in file:
        line = line.split(sep = ',')
        if (city == line[0]):
            date.append(line[1\)
            high.append(line[2])
            low.append(line[3])
    months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    averages_high = []
    averages_low = []
    counter = 0
    high_sum = 0
    low_sum = 0
    for i in range(1,len(date)-1):
        date_split = date[i].split(sep='/')
        if (i == 1):
            high_sum += float(high[1])
            low_sum += float(low[1])
            counter += 1
            month = date_split[0]
        elif (date_split[0] == month):
            high_sum += float(high[i])
            low_sum += float(low[i])
            counter += 1
            month = date_split[0]
        elif (date_split[0] != month):
            averages_high.append(months[int(month)-1])
            averages_low.append(months[int(month)-1])
            high_sum /= counter
            high_sum = round(high_sum, 2)
            low_sum /= counter
            low_sum = round(low_sum, 2)
            averages_high.append(high_sum)
            averages_low.append(low_sum)
            high_sum = 0
            low_sum = 0
            high_sum += float(high[i])
            low_sum += float(low[i])
            counter =  1
            month = date_split[0]
    average_high = []
    average_low = []
    for i in range(1, 24, 2):
        total_high = 0
        total_low = 0
        j  = i
        count = 0
        while (j < len(averages_high)):
            total_high += averages_high[j]
            total_low += averages_low[j]
            j += 24
            count += 1
        total_high = round(total_high/count, 2)
        total_low = round(total_low/count, 2)
        average_high.append(averages_high[i-1])
        average_high.append(total_high)
        average_low.append(averages_low[i-1])
        average_low.append(total_low)
    print("Average Temperatures for", city)
    for i in range(0,len(average_high), 2):
        print(average_high[i], average_high[i+1], "High", average_low[i+1], "Low")
    print()
        
                 
# Part D
# Which city has the highest maximum temperature?
def highest_temperature(city1, city2, weather_filename):
    file = open(weather_filename, 'r')
    max1 = 0
    max2 = 0
    for line in file:
        line = line.split(sep=',')
        if (line[2] != 'High'):
            line[2] = int(line[2])
            if (line[0] == city1):
                if (line[2] > max1):
                    max1 = line[2]
            if (line[0] == city2):
                if (line[2] > max2):
                    max2 = line[2]
    if (max1 > max2):
        return city1
    if (max2 > max1):
        return city2
                
def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_averages_per_month("New York", "weather in metric.csv", "metric")
    print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    city1 = input("Insert city 1: ")
    city2 = input("Insert city 2: ")
    filename = input("Insert weather file to be opened: ")
    city = highest_temperature(city1, city2, filename)
    print(city, "has the highest maximum temperature recorded.")
    
main()
