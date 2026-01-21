# Initialize a counter
day = 1
hour = 8
min = 00


# Loop while the condition (day < 32) is True
# while day < 32:

while hour < 23: #d01_08h30m
#d01_22h30m 
    print(str(hour) + 'd' + str(day))     # Increment the counter in each iteration
    #day += 1
    hour += 1
    #min += 30 
    if hour == 22:
        hour = 8
        day += 1