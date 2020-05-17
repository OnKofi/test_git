import timeit
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
import csv
import xlsxwriter
import datetime

d1 = datetime.datetime.now()
while True:
    date_input = input("Are you checking in today? (Yes/No): ")
    try:
        if date_input == "Yes":

            print(d1.strftime("Good morning Nana. Your check in date is: %d %b %Y"))
            break
        else:
            print("Hope to see you soon")
    except ValueError:
        print("Invalid input")


t1 = datetime.datetime.now()
while True:
    time_input = input(" Are you starting a task right now? (Yes/No): ")
    try:
        if time_input == "Yes":
            print(t1.strftime("Great, you started work at: %H:%M:%S"))
            break
        else:
            print("Hope you start a task soon")
    except ValueError:
        print("Invalid input")

t2 = datetime.datetime.now()
while True:
    closing_time = input("Are you done for the day?(Yes/No):  ")
    try:
        if closing_time == "Yes":
            print(t2.strftime("Enjoy the rest of your day. You closed at: %H:%M:%S"))
            time_difference = t2 - t1
            hour = time_difference.total_seconds()/3600.0
            print('Nana worked for ', "%.2f"%hour, ' hours')
            break
        else:
            print("Keep working Harder then")
    except ValueError:
        print('Invalid input')

amount_paid = hour * 5
print("Thanks for your service, your wage for today is ", "%.2f"%amount_paid, 'dollars')


myData = [[d1, t1, t2, hour, amount_paid]]
myFile = open('NanaFile.csv', 'a')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)



