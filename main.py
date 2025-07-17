def get_weather(temperature, humidity):
    if temperature > 30 and humidity < 50:
        return "It's hot and dry."
    elif temperature < 10:
        return "It's cold."
    else:
        return "The weather is moderate."
    