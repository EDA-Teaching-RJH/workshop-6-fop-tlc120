# Task 4.1
travel_log = []

while True:
    try:
        co = int(input("Please enter the Sensor Reading (Slope Angle): "))

        if co > 45:
            print("CRITICAL TILT! HALTING.")
            travel_log.append(co)
            break

        else:
            travel_log.append(co)
            print("Path Stable. Moving forward.")
            
            
    except ValueError:
        print("Sensor Glitch")


#Task 4.2
print("Mission Terminated.")

for i in range(len(travel_log)):
    print("Total steps taken: ", i + 1)
    print(travel_log)
    