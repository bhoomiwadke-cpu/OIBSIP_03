import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = "a7be54b6a396ccb134f4fd99793ef833"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        result = (
            f"City: {city}\n"
            f"Temperature: {main['temp']} °C\n"
            f"Humidity: {main['humidity']} %\n"
            f"Condition: {weather['description'].title()}\n"
            f"Wind Speed: {wind['speed']} m/s"
        )
        weather_label.config(text=result)
    else:
        messagebox.showerror("Error", "City not found or API issue.")

# GUI Setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=10)

root.mainloop()
