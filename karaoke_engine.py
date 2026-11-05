from datetime import datetime
from time import sleep

with open("song.lrc", 'r', encoding='utf-8') as file:
    offset = 0
    for line in file.readlines():
        raw_time, text = line.strip().split(" ", 1)
        time = datetime.strptime(raw_time.strip("[]"), "%M:%S.%f")
        seconds = time.minute * 60 + time.second + time.microsecond / 1000000
        sleep(seconds - offset)
        print(text)
        offset = seconds