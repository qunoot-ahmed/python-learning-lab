import requests

def get_weather():
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        exit()

    try:
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)
        data = response.json()

        temp = data["current_condition"][0]["temp_C"]
        humidity = data["current_condition"][0]["humidity"]
        wind_speed = data["current_condition"][0]["windspeedKmph"]
        condition = data["current_condition"][0]["weatherDesc"][0]["value"]

        print("\n===== Weather Report =====")
        print(f"City: {city.title()}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")

    except:
        print('Unable to fetch weather data')

def show_menu():
    print("\n===== Weather App =====")
    print("1. Check Weather")
    print("2. Exit")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            get_weather()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 2.")


main()