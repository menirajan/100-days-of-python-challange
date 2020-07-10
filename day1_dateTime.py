import datetime

#for date

date=datetime.date.today()
print(date)

#for time
time=datetime.time(9,20,30,111)
print(time)
print("hour:",time.hour)
print("minute:",time.minute)
print("second:",time.second)
print("microsecond:",time.microsecond)

#for both date and time
dt=datetime.datetime(2020,6,20,9,20,13,100000)
print("full date and time:",dt)
print("full date :",dt.date())
print("full time :",dt.time())

#current date and time
dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()

print("today :",dt_today)
print("now :",dt_now)
print("utcnow :",dt_utcnow)




