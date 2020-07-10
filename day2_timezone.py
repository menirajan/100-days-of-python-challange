import datetime
import pytz


dt =  datetime.datetime(2020,6,20,9,20,13,100000, tzinfo=pytz.UTC)
print(dt)
# for current UTC time
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.now().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# for location time
dt_ktm= dt_utcnow.astimezone(pytz.timezone('Asia/Katmandu'))
print("Nepali time zone :",dt_ktm)

dt_delhi= dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print("Indian time zone ::",dt_delhi)

#for all time zome 
#for tz in pytz.all_timezones:
   # print(tz) 


    