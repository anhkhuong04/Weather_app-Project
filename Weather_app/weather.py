# UNG DUNG DU BAO THOI TIET
import datetime
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Dự Báo Thời Tiết")
root.geometry("890x470")
root.resizable(False, False)

img = PhotoImage(file="Images/clouds-and-sun(1).png")
def getWeather():
    global img
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="GeoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M")
        time = local_time.strftime("%I:%M:%p")
        today = date.today().strftime("%B, %d, %Y")
        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E")


        #weather
        api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=97a310e1694d1983ac5b6d2c58289650"
        json_data = requests.get(api).json()

        #current
        temp = json_data['current']['temp']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']

        t.config(text = f"{temp}°C")
        c.config(text = f"{description} | in {city} | {time} | {today}")
        h.config(text = f"{humidity} %")
        p.config(text = f"{pressure} hPa")
        w.config(text = f"{wind} m/s")
        d.config(text = f"{description}")

        #first cell
        firstdayimage = json_data['daily'][0]['weather'][0]['icon']
        photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
        firstimage.config(image=photo1)
        firstimage.image=photo1
        print(firstdayimage)

        tempday1 = json_data['daily'][0]['temp']['day']
        tempnight1 = json_data['daily'][0]['temp']['night']
        day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")

        #second cell
        seconddayimage = json_data['daily'][1]['weather'][0]['icon']
        img = (Image.open(f"icon/{seconddayimage}@2x.png"))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        secondimage.config(image=photo2)
        secondimage.image=photo2

        tempday2 = json_data['daily'][1]['temp']['day']
        tempnight2 = json_data['daily'][1]['temp']['night']
        day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")

        #third cell
        thirddayimage = json_data['daily'][2]['weather'][0]['icon']
        img = (Image.open(f"icon/{thirddayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo3 = ImageTk.PhotoImage(resized_image)
        thirdimage.config(image=photo3)
        thirdimage.image = photo3

        tempday3 = json_data['daily'][2]['temp']['day']
        tempnight3 = json_data['daily'][2]['temp']['night']
        day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

#fourth cell
        fourdayimage = json_data['daily'][3]['weather'][0]['icon']
        img = (Image.open(f"icon/{fourdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo4 = ImageTk.PhotoImage(resized_image)
        fourthimage.config(image=photo4)
        fourthimage.image = photo4

        tempday4 = json_data['daily'][3]['temp']['day']
        tempnight4 = json_data['daily'][3]['temp']['night']
        day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")

#fifth cell
        fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
        img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo5 = ImageTk.PhotoImage(resized_image)
        fifthimage.config(image=photo5)
        fifthimage.image = photo5

        tempday5 = json_data['daily'][4]['temp']['day']
        tempnight5 = json_data['daily'][4]['temp']['night']
        day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

#sixth cell
        sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
        img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo6 = ImageTk.PhotoImage(resized_image)
        sixthimage.config(image=photo6)
        sixthimage.image = photo6

        tempday6 = json_data['daily'][5]['temp']['day']
        tempnight6 = json_data['daily'][5]['temp']['night']
        day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")

#seven cell
        seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
        img = (Image.open(f"icon/{seventhdayimage}@2x.png"))
        resized_image = img.resize((50, 50))
        photo7 = ImageTk.PhotoImage(resized_image)
        seventhimage.config(image=photo7)
        seventhimage.image = photo7

        tempday7 = json_data['daily'][6]['temp']['day']
        tempnight7 = json_data['daily'][6]['temp']['night']
        day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")

#days
        first = datetime.now()
        day1.config(text=first.strftime("%A"))

        second = first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        third = first + timedelta(days=2)
        day3.config(text=third.strftime("%A"))

        fourth = first + timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))

        fifth = first + timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        sixth = first + timedelta(days=5)
        day6.config(text=sixth.strftime("%A"))

        seventh = first + timedelta(days=6)
        day7.config(text=seventh.strftime("%A"))

        #logo
        if current_time >= "18:00" or current_time < "05:00":
            img = PhotoImage(file="Images/moon1.png")
        else:
            img = PhotoImage(file="Images/sunlogo.png")
        logo.config(image=img)
        logo.image = img
    except Exception:
        messagebox.showerror("Weather app", "Không Tìm Thấy địa điểm!")

#CenterScreen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height,x, y))



# icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)
#search box
Search_image = PhotoImage(file = "Images/Rounded Rectangle 3.png")
my_image = Label(image=Search_image)
my_image.place(x=20, y=15)

textfield = tk.Entry(root, justify = 'center' , width=15, font=('poppins', 25, 'bold'),bg="#203243", border=0, fg="white")
textfield.place(x=50, y=27)
textfield.focus()

Search_icon = PhotoImage(file="Images/Layer 6.png")
my_image_icon = Button(image = Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
my_image_icon.place(x=390, y=20)

# logo
logo = Label(image=img)
logo.place(x=20, y=100)

# Box weather
Round_box = PhotoImage(file="Images/Copy of box (2).png")
Label(root, image=Round_box).place(x=190, y=190)
#label
label2 = Label(root, text="Humidity", font=('arial', 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=230, y=205)

label3 = Label(root, text="Pressure", font=('arial', 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=360, y=205)

label4 = Label(root, text="Wind Speed", font=('arial', 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=490, y=205)

label4 = Label(root, text="Description", font=('arial', 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=640, y=205)

# status weather
t = Label(root, font=('arial', 45, 'bold'), fg="#1ab5ef")
t.place(x=210, y=90)

c = Label(root, font=('arial', 13, 'bold'))
c.place(x=200, y=160)

h = Label(root, font=('arial', 13, 'bold'), fg="white", bg="#1ab5ef")
h.place(x=250, y=235)

p = Label(root, font=('arial', 13, 'bold'), fg="white", bg="#1ab5ef")
p.place(x=370, y=235)

w = Label(root, font=('arial', 13, 'bold'), fg="white", bg="#1ab5ef")
w.place(x=510, y=235)

d = Label(root, font=('arial', 13, 'bold'), fg="white", bg="#1ab5ef")
d.place(x=635, y=235)

#timezone
timezone=Label(root, font=("Times new Roman", 20))
timezone.place(x=670, y=15)

long_lat=Label(root, font=("Times new Roman", 13))
long_lat.place(x=670, y=50)

#Bottom Box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

#Bottom Boxes
firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

#first cell
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=315)

day1 = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)

#second cell
secondframe = Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=305, y=325)

day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=10, y=5)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=23)

day2temp = Label(secondframe, bg="#282829", fg="#fff")
day2temp.place(x=2, y=70)

#third
thirdframe = Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=2, y=5)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=23)

day3temp = Label(thirdframe, bg="#282829", fg="#fff")
day3temp.place(x=2, y=70)

#fouth cell
fourthframe = Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=2, y=5)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=23)

day4temp = Label(fourthframe, bg="#282829", fg="#fff")
day4temp.place(x=2, y=70)

#fifth cell
fifthframe = Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=2, y=5)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=23)

day5temp = Label(fifthframe, bg="#282829", fg="#fff")
day5temp.place(x=2, y=70)

#sixth cell
sixthframe = Frame(root, width=70, height=115, bg="#282829")
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=2, y=5)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=7, y=23)

day6temp = Label(sixthframe, bg="#282829", fg="#fff")
day6temp.place(x=2, y=70)

#seventh cell
seventhframe = Frame(root, width=70, height=115, bg="#282829")
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, bg="#282829", fg="#fff")
day7.place(x=2, y=5)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=7, y=23)

day7temp = Label(seventhframe, bg="#282829", fg="#fff")
day7temp.place(x=2, y=70)

root.mainloop()
