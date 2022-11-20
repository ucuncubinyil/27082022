import time
from threading import Thread


def thread_action(number):
    for i in range(number):
        print("Thread ile çağrıldı: ", str(i))
        time.sleep(1)

def function():
    for i in range(5):
        print("Normal çağrıldı: ", str(i))
        time.sleep(3)


thread =  Thread(target=thread_action, args=(4,))
thread.start()
function()