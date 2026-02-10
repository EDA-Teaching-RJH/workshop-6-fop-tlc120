# Task 3.1
try:
    X = int(input("Enter Motor Speed: "))
    print(f"Speed set to {X}")
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")

# Task 3.2
def get_coordinate():
    while True:
        try:
            co = int(input("Please enter the X-coordinate: "))
            print(co)
            
        except ValueError:
            print("Invalid coordinate")
        else:
            break

get_coordinate()

# Task 3.3
def get_coordinate1():
    while True:
        try:
            co = int(input("Please enter the X-coordinate: "))
            print(co)

            if co > 100 or co < -100:
                print("Coordinate out of range")
                continue
            
        except ValueError:
            print("Invalid coordinate")
        else:
            break

get_coordinate1()


