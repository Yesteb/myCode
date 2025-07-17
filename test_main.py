from main import get_weather

def test_get_weather():
    assert get_weather(35, 40) == "It's hot and dry."
    assert get_weather(5, 60) == "It's cold."
    assert get_weather(20, 70) == "The weather is moderate."
    assert get_weather(30, 50) == "The weather is moderate."
    assert get_weather(15, 30) == "The weather is moderate."