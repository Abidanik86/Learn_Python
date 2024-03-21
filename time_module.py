import time

current_time = time.localtime()
hour = current_time.tm_hour

if hour < 12:
    print("Good morning!")
elif hour == 12:
    print("Good noon!")
else:
    print("Good afternoon!")