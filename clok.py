from playsound import playsound
import time
from datetime import datetime 
from pogoda import get_info_weather
def clock():
    pass
        
def get_setting_clock():
    hour = int(input("Введите час: "))
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    minute = int(input("Введите минуты: "))
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    second = int(input("Введите секунды: "))
    if len(str(second)) == 1:
        second = "0" + str(second)
    timer = f"{hour}:{minute}:{second}"
    return timer

def timer_cikl(file_path, temp):
    timer = get_setting_clock()
    
    print(timer)
    hour = timer[0]
    if len(str(hour)) == 1:
        hour = "0" + str(hour)
    minute = timer[1]
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    second = timer[2]
    if len(str(second)) == 1:
        second = "0" + str(second)
    print(f"Будильник установлен на: {timer}")
    print("Счастливо отработать!!! Берегите нервы!!!")
       
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, end="\r")
        time_start = current_time
        time_end = timer
        delta_time = datetime.strptime(time_end, "%H:%M:%S") - datetime.strptime(time_start, "%H:%M:%S")
        
        time.sleep(1)
        if current_time == timer:
            print("Пора собираться!!!")
            time.sleep(1)
            temp = get_info_weather()
            playsound(file_path)
            print('Температура за бортом: ', temp)
            break
    print(f"{current_time} == {hour}:{minute}:{second}")
    print(f"Рабочее время вышло, будильник выключен. До завтра!!!")
        
def main():
    timer_cikl(file_path=file_path, temp=temp)
temp = get_info_weather()
file_path = "Tishiny_tishiny_khochu_sample.mp3"
if __name__ == "__main__":
    main()