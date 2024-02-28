Imports
#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
#function to give a remark on my mood based on avg_mood value
def interpret_mood(avg_mood):
    if avg_mood >= 9:
        return "Excellent mood today, thank god"
    elif avg_mood <  5:
        return "Middlin today, thanks for asking"
    elif 5 <= avg_mood < 9:
        return "Improving thanks."
    else:
        return "Not really sure, not enough info \n"
    Take in 3 wellness indicators
#Take them in as integers, as all inputs default to strings
screentime_wellbeing = int(input("On a scale of 1-10 from poorly to ready, how prepared for exams are you?"))
physical_wellbeing = int(input("On a scale of 1-10 from tired to energetic, how much energy do you have?"))
mental_wellbeing = int(input("On a scale of 1-10 from crappy friend relations to happy/clappy friend relations to ?"))
avg_mood = round(mean([intellectual_wellness,physical_wellness,social_wellness]),2)
mood_remark = interpret_mood(avg_mood)
print("My Average mood today is ",mood_remark, " ", avg_mood)
df = pd.read_csv('microbitdata105638.csv')
print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
light_min = df['Light'].min()
light_max = df['Light'].max()
light_mean = df['Light'].mean()
print (light_min,light_max,light_mean, avg_mood)
f = open("BR1-3_results.csv", "a", newline='')
csver = csv.writer(f)

csver.writerow([light_min, light_max, light_mean, avg_mood])