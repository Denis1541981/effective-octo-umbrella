# сloc = "23:59:59"
# hour = int(сloc.split(":")[0])
# minute = int(сloc.split(":")[1])
# second = int(сloc.split(":")[2])
# print(type(hour), type(minute), type(second), hour, minute, second)
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(type(current_time))

hour = int(input("Enter hour: "))
if len(str(hour)) == 1:
    hour = "0" + str(hour)
minute = int(input("Enter minute: "))
if len(str(minute)) == 1:
    minute = "0" + str(minute)
second = int(input("Enter second: "))
if len(str(second)) == 1:
    second = "0" + str(second)
timer = f"{hour}:{minute}:{second}"
print(type(timer))