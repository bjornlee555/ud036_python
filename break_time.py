import webbrowser
import time

num = 1

while num < 4:
    print ('This program started at: ' + time.ctime())
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=LWbjrFCecPY')
    num += 1
