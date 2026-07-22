import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
""" with open("ipl_stats.csv",'w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['Player name','Team','Matches','Runs','Strike Rate'],
        ['Jarvis','pbks',2,570,450],
        ['melon','rbc',3,370,120],
        ['notew','rbc',4,590,230],
        ['rews','csk',2,70,100],
        ['defos','pbks',5,580,300],
        ['lavis','mi',2,534,100]
    ])
df=pd.read_csv("ipl_stats.csv")
sorted_df=df.sort_values(by="Runs",ascending=False)
print(sorted_df.head(5))
filtered=df[df['Strike Rate']>140]
print(filtered)
print(df['Runs'].mean())
highest_score=df['Runs'].max()
print(df[df['Runs']==highest_score])

x=df['Player name']
y=df['Runs']
plt.bar(x,y)
plt.xlabel("Players")
plt.ylabel("Runs")
plt.show()

x=df['Matches']
y=df['Runs']
plt.scatter(x,y)
plt.xlabel("Matches")
plt.ylabel('Runs')
plt.show()

data=df['Strike Rate']
plt.hist(data)
plt.xlabel("Strike Run")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show() """

#2
""" data={
    'Flight Number':['101','102','103','104','105','106'],
    'Source':['India','US','China','Pak','Nepal','EU'],
    'Destination':['US','EU','AFrica','China','India','India'],
    'Ticket Price':[2500,8000,12000,8000,5000,9000],
    'Seats Available':[32,20,30,14,26,16]
}
df=pd.DataFrame(data)
filtered=df[df['Ticket Price']>7000]
print(filtered)
filteredSeats=df[df['Seats Available']<25]
print(filteredSeats)

highTP=df['Ticket Price'].max()
lowTP=df['Ticket Price'].min()
avgTP=df['Ticket Price'].mean()
print(highTP)
print(lowTP)
print(avgTP)

#data=df['Destination']
#plt.pie(data)
#plt.show()
#pie chart
y=df['Ticket Price']
x=df['Flight Number']
plt.bar(x,y)
plt.xlabel("Flight no.")
plt.ylabel("Ticket Price")
plt.show()"""

#3
with open("smartphone.csv",'w+') as file:
    writer=csv.writer(file)
    writer.writerows([
        ['Brand','Model','RAM','Storage','Battery','Price'],
        ['a','t',16,128,5600,45000],
        ['s','r',8,128,2800,30000],
        ['d','e',4,256,6000,20000],
        ['f','w',32,1024,8000,40000],
        ['g','q',4,128,5600,20000],
    ])
df=pd.read_csv('smartphone.csv')
filtram=df[df['RAM']>=8]
print(filtram)
filtprice=df[df['Price']<30000]
print(filtprice)
highpr=df['Price'].max()
print(highpr)
avgpr=df['Price'].mean()
print(avgpr)
x=df['RAM']
y=df['Price']
plt.scatter(x,y)
plt.show()

data=df['Battery']
plt.hist(data)
plt.show()

y=df['Price']
x=df['Brand']
plt.bar(x,y)
plt.show()



