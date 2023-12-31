import time
import re
import os

matcher = re.compile(r"^(\d\d) (\d\d) (\d\d) (\d\d) ([A-Z]+)$")

def main():
    mission_time_seconds = 0
    day = hour = minute = second = speaker = ""
    with open(os.path.join(os.path.dirname(__file__), 'log.txt')) as file:
        for line in file:
            match_result = matcher.match(line)
            if match_result:
                day = match_result[1]
                hour = match_result[2]
                minute = match_result[3]
                second = match_result[4]
                speaker = match_result[5]
                
                time_seconds = (int(day)*24*60*60)+(int(hour)*60*60)+(int(minute)*60)+(int(second))
                
                sleep_time = time_seconds - mission_time_seconds
                sleep_time = 1 if sleep_time < 0 else sleep_time
                if sleep_time > 60*60*24: # sometimes the transcription is wrong
                    sleep_time = 1
                time.sleep(sleep_time)
                mission_time_seconds = time_seconds
            else:
                stripped_line = line.strip()
                if stripped_line and speaker:
                    print(f"[{speaker}] {day} {hour}:{minute}:{second} {stripped_line}", flush=True)

if __name__ == '__main__':
    main()
