Dicts = {"Power": 100, "Samples": 0}
inventory = []
x = 100
while True: 
    try:
        print("\n____MENU____")
        print("1. Dig for Sample")
        print("2. Report Status")
        print("3. Emergency Stop")

        choices = int(input("\nPlease enter your choice: "))

        if choices == 1:
            co = input("Please enter a sample name: ")
            inventory.append(co)
            x = x - 10
            Dicts.update({"Power": x})

        elif choices == 2:
            print(Dicts)
            print(inventory)
           
        elif choices == 3:
            break
            
            
    except ValueError:
        print("Error Handling")

