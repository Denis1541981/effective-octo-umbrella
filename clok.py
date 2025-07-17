#!/usr/bin/python3

import pygame
import time
import sys
import os
from datetime import datetime
from pogoda import get_info_weather


def get_setting_clock():
    hour = input("Введите часы: ").zfill(2)
    minute = input("Введите минуты: ").zfill(2)
    second = '00'
    timer = f"{hour}:{minute}:{second}"
    return timer


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def play_sound(file_path):
    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Ошибка воспроизведения звука: {e}")


def timer_cycle(file_path):
    timer = get_setting_clock()
    print(f"Будильник установлен на: {timer}")
    print("Счастливо отработать!!! Берегите нервы!!!")

    time_start = get_current_time()
    time_end = timer
    delta_time = datetime.strptime(time_end, "%H:%M:%S") - datetime.strptime(time_start, "%H:%M:%S")
    print(f"До будильника осталось: {delta_time}")
    print('=' * 40)

    while True:
        current_time = get_current_time()
        print(f"\rТекущее время: {current_time}", end="")
        sys.stdout.flush()
        time.sleep(1)
        if current_time == timer:
            print("\nПора собираться!!!")
            play_sound(file_path)
            print(get_info_weather())
            break

    print(f"{current_time} == {timer}")
    print("Рабочее время вышло, будильник выключен. До завтра!!!")
    print('=' * 40)


def main():
    file_path = "Tishiny_tishiny_khochu_sample.mp3"  # Убедись, что этот файл существует
    print(get_info_weather())
    timer_cycle(file_path)


if __name__ == "__main__":
    main()
