# Task 2.1
rover_status = {
    "Battery": 100,
    "Heater": "Off",
    "Camera": "Standby"
}

print(rover_status["Battery"])

# Task 2.2

rover_status.update({"Battery": 85})
rover_status.update({"Heater": "On"})
rover_status["Speed"] = 5

print(rover_status)

# Task 2.3
mission_log = [
    {"Site": "Crater A", "Radiation": "Low", "Water": "False"},
    {"Site": "Dune B", "Radiation": "High", "Water": "True"}
]

for mis in mission_log:
    print(mis["Site"], "has",mis["Radiation"],"radiation.")
          