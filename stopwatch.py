# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:13:01 2020

@author: VK
"""


import time
print("Press Enter to start the stopwatch")
print("Press CTRL+C to stop the stopwatch")
while True:
    try:
        input()
        start_time = time.time()
        print("Stopwatch started")
    except KeyboardInterrupt:
        print("Stopwatch stopped")
        end_time = time.time()
        total_time = round(end_time - start_time,2)
        print("The total time:",total_time,"seconds")
        break
    