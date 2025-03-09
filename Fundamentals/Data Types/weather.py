
try:
    temperature = float(input("Enter the temperature in Fahrenheit: "))
    rainy = input("Is it raining? (True/False): ").lower() == 'true'
    if rainy:
        forecast = "Bring an umbrella."
    else:
        snowing = input("Is it snowing? (True/False): ").lower() == 'true'
        if snowing:
            forecast = "Wear a hat and gloves."
        else:
            cloudy = input("Is it cloudy? (True/False): ").lower() == 'true'
            if cloudy:
                forecast = "Wear a jacket."
            else:
                forecast = "Wear a t-shirt."
    
    if temperature > 90:
        print("It's too hot outside.")    
    elif temperature < 50:  
        print("It's too cold outside.")    
    else:
        print("It's just right outside.\n But " + forecast)
except ValueError:
    print("Please enter a valid input.")