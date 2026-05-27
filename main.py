from weather.fetcher import get_weather, parse_weather

def display_weather(weather: dict) -> None:
    """Print weather details in a formatted layout."""
    print("\n" + "=" * 40)
    print(f"{weather['city']}, {weather['country']}")
    print("=" * 40)
    print(f"  Condition     : {weather['description']}")
    print(f"  Temperature   : {weather['temperature_c']}°C / {weather['temperature_f']}°F")
    print(f"  Feels Like    : {weather['feels_like_c']}°C")
    print(f"  Humidity      : {weather['humidity']}%")
    print(f"  Wind          : {weather['wind_speed_kmph']} km/h {weather['wind_direction']}")
    print(f"  Visibility    : {weather['visibility_km']} km")
    print(f"  UV Index      : {weather['uv_index']}")
    print("=" * 40 + "\n")

def main() -> None:
    print("\n====  WEATHER APP  ====\n")

    while True:
        city = input("Enter city name (or 'q' to quit): ").strip()

        if city.lower() == "q":
            print("Goodbye!")
            break

        if not city:
            print("Please enter a valid city name.\n")
            continue

        data = get_weather(city)
        weather = parse_weather(data)
        display_weather(weather)

if __name__ == "__main__":
    main()