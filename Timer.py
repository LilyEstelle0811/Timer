import time
def print_one_line(hours, minutes, seconds, tenths):
    while True:
        printout= f'{hours:02d}:{minutes:02d}:{seconds:02d}.{tenths}'
        print(printout)
        tenths +=1
        if tenths ==10:
            tenths = 0
            seconds +=1
            if seconds == 60:
                seconds = 0
                minutes +=1
                if minutes == 60:
                    minutes = 0
                    hours +=1
                    if hours ==24:
                        hours = 0
        time.sleep(0.1)
