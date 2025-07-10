from tkinter import*
from tkinter import messagebox
from configparser import ConfigParser
import requests
import emoji



api_file='api.key'
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_a['api_key']['key']
url_api= " https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

def weather_find(city):
    final=requests.get(url_api.format(city,api_key))
    if final:
        json_file=final.json()
        city=json_file['name']
        country_name=json_file['sys']['country']
        k_temperature=json_file['main']['temp']
        c_temperature=k_temperature-273.15
        f_temperature=(k_temperature-273.15)*9/5+32

        weather_display=json_file['weather'][0]['main']
        result=(city,country_name,c_temperature,f_temperature,weather_display)
        return result
    
    else:
        return None
def print_weather():
    city=search_city.get()
    weather=weather_find(city)

    if weather:
        location_entry['text']='{},{}'.format(weather[0],weather[1])
        temperature_entry['text']='{:.2f} C,{:.2f} F'.format(weather[2],weather[3])
        weather_entry['text']=weather[4]

    else:
        messagebox.showerror('Error!,please enter a valid city name')


root=Tk()
root.title("Weather Forecast ⛅")
root.config(background="#87CEEB")
root.geometry("700x400")

search_city=StringVar()
enter_city=Entry(root,textvariable=search_city,fg="grey",font=("arial",18,"bold"))
enter_city.pack()
search_button=Button(root,text='Search Weather 🔍',width=20,bg="black",fg="white",font=("Arial",16,"italic"),command=print_weather)
search_button.pack()
location_entry=Label(root,text='',font=("arial",18,"bold"),fg="white",background="brown")
location_entry.pack()

temperature_entry=Label(root,text='',font=("arial",18,"bold"),fg="white",background="brown")
temperature_entry.pack()

weather_entry=Label(root,text='',font=("arial",18,"bold"),fg="white",background="brown")
weather_entry.pack()



root.mainloop()



