# %%
'''
### Watch this video: 
https://youtu.be/CFRhGnuXG-4


### Exercise: extract functions from the following (terrible) code.
Some things to keep in mind:
- Keep the functions pure (i.e.: no interaction with their environment)
- Good interfaces (input/output) make them testable
- Try to keep modules similarly sized (not a must, but a good rule-of-thumb)
- Use good naming practices to describe the functionality

python=
'''
def kelvin_to_celsius(temperature):
    if temperature < 0.0:
        #print("Invalid temperature")
        return "Invalid temperature"
    else:
        return temperature - 273.15
def celsius_to_kelvin(temperature):
    if temperature < -273.15:
        #print("Invalid temperature")
        return "Invalid temperature"
    else:
        return temperature + 273.15
def celsius_to_fahrenheit(temperature):
    if temperature < -273.15:
        #print("Invalid temperature")
        return "Invalid temperature"
    else:
        return (temperature * (9.0 / 5.0)) + 32.0
def fahrenheit_to_celsius(temperature):
    if temperature < -459.67:
        #print("Invalid temperature")
        return "Invalid temperature"
    else:
        return (temperature - 32.0) * (5.0 / 9.0)
def kelvin_to_fahrenheit(temperature):
    if temperature < 0.0:
        #print("Invalid temperature")
        return "Invalid temperature"
    else:
        return (temperature - 273.15) * (5.0 / 9.0) + 32.0
def fahrenheit_to_kelvin(temperature):
    """This function converts the temperature value from Fahrenheit to Kelvin

    Args:
        temperature (float): Value of the temperature in Fahrenheit

    Returns:
        float/String: Returns the modified value of the temperature in Kelvin, given that the entered input is valid. If the input value is not valid, returns a string prompting the invalidity.
    """
    if temperature < -459.67:
        #print("Invalid temperature")
        return "Invalid temperature"
    else:
        return (temperature - 32.0) * (5.0 / 9.0) + 273.15

def convert_temperature(temperature, unit):   
    if unit == "F":
        print(fahrenheit_to_celsius(temperature), "C")
        print(fahrenheit_to_kelvin(temperature), "K")

    if unit == "C":
        print(celsius_to_fahrenheit(temperature), "F")
        print(celsius_to_kelvin(temperature), "K")

    if unit == "K":
        print(kelvin_to_fahrenheit(temperature), "F")
        print(kelvin_to_celsius(temperature), "C")
# %%
convert_temperature(-458,"F")
# %%
'''
def convert_temperature(temperature, unit):
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                if temperature % 2 == 0:
                    return "Invalid temperature"
                else:
                    if kelvin % 2 == 0:
                        return "Invalid temperature"
                    else:
                        return celsius, kelvin
            else:
                if celsius % 2 == 0:
                    # Convert Celsius to Fahrenheit
                    fahrenheit = (celsius * (9 / 5)) + 32
                    if fahrenheit < -459.67:
                        # Invalid temperature, below absolute zero
                        return "Invalid temperature"
                    else:
                        if fahrenheit % 2 == 0:
                            return fahrenheit, kelvin
                        else:
                            return fahrenheit, celsius
                else:
                    return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * (9 / 5)) + 32
        if fahrenheit < -459.67:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = temperature + 273.15
            if kelvin < 0:
                # Invalid temperature, below absolute zero
                if temperature % 2 == 0:
                    return "Invalid temperature"
                else:
                    if kelvin % 2 == 0:
                        return "Invalid temperature"
                    else:
                        return fahrenheit, kelvin
            else:
                if temperature % 2 == 0:
                    # Convert Celsius to Fahrenheit
                    fahrenheit = (temperature * (9 / 5)) + 32
                    if fahrenheit < -459.67:
                        # Invalid temperature, below absolute zero
                        return "Invalid temperature"
                    else:
                        if fahrenheit % 2 == 0:
                            return fahrenheit, kelvin
                        else:
                            return fahrenheit, temperature
                else:
                    return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        if celsius < -273.15:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                if celsius % 2 == 0:
                    # Convert Celsius to Fahrenheit
                    fahrenheit = (celsius * (9 / 5)) + 32
                    if fahrenheit < -459.67:
                        # Invalid temperature, below absolute zero
                        return "Invalid temperature"
                    else:
                        if fahrenheit % 2 == 0:
                            return fahrenheit, celsius
                        else:
                            return fahrenheit, kelvin
                else:
                    return celsius, fahrenheit
    else:
        return "Invalid unit"
'''