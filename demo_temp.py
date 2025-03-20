from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=20a01944eda34a13f4a4dcecfff77197").json()
    W_label1.config(text=data["weather"][0]["main"])
    Wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])



win = Tk()
win.title("CLIMATRIX")
win.config(bg= "#1e1e1e")#Dark background
win.geometry("500x570")

name_label = Label(win,text="MS Weather App",  font=("Time New Roman",30,"bold"),bg="#1e1e1e",fg="white")
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="MS Weather App",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

# done_button = Button(win,text="Done",font=("Time New Roman",20,"bold"))
# done_button.place(y=190,height=50,width=100,x=200)


W_label1 = Label(win,text=" ",  font=("Time New Roman",20))
W_label1.place(x=250,y=260,height=50,width=220)

W_label = Label(win,text=" Weather climate",  font=("Time New Roman",20))
W_label.place(x=25,y=260,height=50,width=220)



Wb_label = Label(win,text=" Weather descrption",  font=("Time New Roman",17))
Wb_label.place(x=25,y=330,height=50,width=220)

Wb_label1 = Label(win,text=" ",  font=("Time New Roman",17))
Wb_label1.place(x=250,y=330,height=50,width=220)




temp_label = Label(win,text=" temprature",  font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=220)

temp_label1 = Label(win,text=" ",  font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=220)



per_label = Label(win,text=" pressure",  font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=220)

per_label1 = Label(win,text=" ",  font=("Time New Roman",20))
per_label1.place(x=250,y=470,height=50,width=220)

def on_enter(e):
    done_button.config(bg="green")  # Change to any color

def on_leave(e):
    done_button.config(bg="white")  # Reset to original color

done_button = Button(win,text="Done",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)



# done_button = {"bg": "#00bcd4", "fg": "white", "font": ("Arial", 12), "width": 20, "borderwidth": 2}
# entry_style = {"bg": "#333333", "fg": "white", "font": ("Arial", 12), "width": 20, "borderwidth": 2}

done_button.bind("<Enter>", on_enter)  # Mouse enters button
done_button.bind("<Leave>", on_leave)  # Mouse leaves button
win.mainloop()
