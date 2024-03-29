
import datetime

current_time = datetime.datetime.now()

print("The attributes of now() are :")

print("Year :", current_time.year)

print("Hour : ", current_time.hour)

print("Minute : ", current_time.minute)

print("Second :", current_time.second)

def greeting_time():
    currentTime = datetime.datetime.now()
    currentTime.hour
    print(currentTime.hour,":",currentTime.minute,":",currentTime.second,":",currentTime.microsecond)
    if  currentTime.hour < 12:
        print('Good morning', "sir ")
        greeting=" good morning sir "
    elif 12 <= currentTime.hour < 18:
        print('Good afternoon', "sir")
        greeting="good afternoon sir "
    else:
        print('Good evening', "sir")
        greeting="good evening sir " 

greeting_time()

