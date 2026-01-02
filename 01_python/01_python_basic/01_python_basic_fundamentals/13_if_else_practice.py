# ============================================
# 13. If-Else Practice
# Weather and Temperature Checker
# ============================================
# This file practices conditional statements (if / elif / else)
# using simple real-world examples.
# Expected outputs are shown as comments for clarity.
# ============================================


# ----------------------------
# Weather Checker
# ----------------------------

# Ask the user about today's weather
weather = input("How is the weather today? ")

if weather == "rain" or weather == "snow":
    print("Please take an umbrella.")
elif weather == "fine dust":
    print("Please wear a mask.")
else:
    print("No preparation needed.")

# Example Inputs and Results:
# Input -> rain
# Result -> Please take an umbrella.
#
# Input -> snow
# Result -> Please take an umbrella.
#
# Input -> fine dust
# Result -> Please wear a mask.
#
# Input -> sunny
# Result -> No preparation needed.


# ----------------------------
# Temperature Checker
# ----------------------------

# Ask the user about today's temperature
temp = int(input("What is the temperature today? "))

if temp >= 30:
    print("It's too hot. Stay inside.")
elif 10 <= temp < 30:
    print("The weather is nice.")
elif 0 <= temp < 10:
    print("Please bring a jacket.")
else:
    print("It's too cold. Stay inside.")

# Example Inputs and Results:
# Input -> 35
# Result -> It's too hot. Stay inside.
#
# Input -> 20
# Result -> The weather is nice.
#
# Input -> 5
# Result -> Please bring a jacket.
#
# Input -> -3
# Result -> It's too cold. Stay inside.
