# Task 1.1
sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(sample_bay[0])

last = sample_bay[len(sample_bay) - 1]

print(last)

print((len(sample_bay)))

# Task 1.2
for i in range((len(sample_bay))):
    print("Transmitting data for:", sample_bay[i])

# Task 1.3
new_findings = []

x = 0
while True:
    if x <= 2:
        new = input("Please enter a rock type: ")
        new_findings.append(new)
        x = x + 1

    else:
        print(new_findings)
        break

# Task 1.4
for y in sample_bay:
    if "Dust" in sample_bay:
        re = sample_bay.pop(3)
        print(sample_bay)
    else:
        continue


