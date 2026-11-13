# Imports go at the top
from microbit import *
import read_moisture as moist
import pump as pump

def get_light():
    light = display.read_light_level()
    return(light)

def get_temp():
    temp = temperature()
    return(temp)

def get_moisture():
    moisture = moist.read_moisture()
    return(moisture)

def water_plant(ifwater):
    if ifwater == 1:
        pump.pump()
        print("water has been pumped")

def calc_health(light, temp, moisture, time, pref_light, pref_moisture, pref_temp):
    
    light_health = 100
    moisture_health = 100
    temp_health = 100
    
    range_light = 50
    range_moisture = 10
    range_temp = 10
    
    health_stat = "ok"
    light_stat = "correct"
    moisture_stat = "correct"
    temp_stat = "correct"

    health = 100

    if (light >= pref_light + range_light) or (light <= pref_light - range_light):
        light_health = max(light_health - abs(light - pref_light), 0)
        if light >= pref_light + range_light:
            light_stat = "too bright"
        elif light <= pref_light - range_light:
            light_stat = "too dim"
    if (moisture >= pref_moisture + range_moisture) or (moisture <= pref_moisture - range_moisture):
        moisture_health = max(moisture_health - abs(moisture - pref_moisture), 0)
        if moisture >= pref_moisture + range_moisture:
            moisture_stat = "too wet"
        elif moisture <= pref_moisture - range_moisture:
            moisture_stat = "too dry"
    if (temp >= pref_temp + range_temp) or (temp <= pref_temp - range_temp):
        temp_health = max(temp_health - abs(temp - pref_temp), 0)
        if temp >= pref_temp + range_temp:
            temp_stat = "too hot"
        elif temp <= pref_temp - range_temp:
            temp_stat = "too cold"

    health = (light_health + moisture_health + temp_health) / 3

    if health >= 82:
        health_stat = "good"
    elif health >= 50:
        health_stat = "ok"
    elif health >= 0:
        health_stat = "poor"

    print("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
    print("It has been ", time / 60, " minutes since plant care system was started")
    print("The overall health score (1-100) is: ", health)
    print("The overall health is: ", health_stat)
    print("The light level is ", light, " and the light health score (1-100) is ", light_health)
    print("The light level is: ", light_stat)
    print("The moisture level is ", moisture, " and the moisture health score (1-100) is ", moisture_health)
    print("The soil moisture is: ", moisture_stat)
    print("The temperature level is ", temp, " degrees C and the temp health score (1-100) is ", temp_health)
    print("The temperature is: ", temp_stat)
    
    
    if moisture <= pref_moisture - range_moisture:
        #print("need water")
        return(1, health_stat)
       
    else:
        return(0, health_stat)
    
time = 0  
ifwater = 0
pref_light = float(input("Input desired plant light level: "))
pref_moisture = float(input("Input desired plant soil moisure level: "))
pref_temp = float(input("Input desired plant temperature level: "))

temp_data = []
moisture_data = []
light_data = []

while True:
    light = get_light()
    moisture = get_moisture()
    temp = get_temp()
    light_data.append(light)
    moisture_data.append(moisture)
    temp_data.append(temp)
    ifwater, health_stat = calc_health(light, temp, moisture, time, pref_light, pref_moisture, pref_temp)
    water_plant(ifwater)
    display.scroll(health_stat)
    sleep(10000)
    time = time + 10
    

    

