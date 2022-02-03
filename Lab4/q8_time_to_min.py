if __name__ == '__main__':
    hrs, mins, sec = int(input('hrs: ')), int(input('min: ')), int(input('sec: '))
    time_to_min = lambda hrs, mins, sec: hrs*60+mins+sec/60
    print(f"time_to_min({hrs}, {mins}, {sec}) = {time_to_min(hrs, mins, sec)}")