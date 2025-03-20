# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# A few years ago, NASA made history with the first controlled flight on another planet.
#  Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. Ingenuity made its third flight,

#  during which it flew faster and further than it had on any of its test flights on Earth. 
# Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars,
#  an Earthling's weight on Mars is 37.8% of their weight on Earth. 

# Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

# The output should be rounded to two decimal places when necessary. 

# Python has a round function which can help you with this.
#  You pass in the value to be rounded and the number of decimal places to use. In the example below,
#  the number 3.1415926 is rounded to 2 decimal places which is 3.14.

# SOLUTION
def mars_weight_calculator():
      user_input = float(input("Enter Your Earth Weight: "))
      mars_weight: float = user_input * 0.378
      rounded_weight: float = round(mars_weight, 2)
      print(f"Your weight on Mars: {mars_weight} kg")
mars_weight_calculator()

# Milestone #2: Adding in All Planets

# Mars is not the only planet in our solar system with its own unique gravity. In fact, 
# each planet has a different gravitational constant, which affects how much an object would weigh on that planet. 
# Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. 
# The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about 
# the case where they type in something other than one of the above planets.

planet_gravity = {
          "Mercury": 0.376,
          "Venus": 0.889,
          "Mars": 0.378,
          "Jupiter": 2.360,
          "Saturn": 1.081,
          "Uranus": 0.815,
          "Neptune": 1.140
     }
def planet_weight():
     earth_weight = float(input("Enter Your Earth Weight please: "))
     planet_of_choice = str (input("Enter the name of the planet: "))
     if planet_of_choice in planet_gravity:
          planet_weight = earth_weight * planet_gravity[planet_of_choice] / 100
          rounded_weight = round(planet_weight, 2)
          print(f"Your weight on {planet_of_choice}: {rounded_weight} kg")
     else:
          print("Invalid planet name")
  
    #  planet_weight = earth_weight * planet_gravity[planet_name]
    #  rounded_weight = round(planet_weight, 2)
    #  print(f"Your weight on {planet_name}: {rounded_weight} kg")

planet_weight()

