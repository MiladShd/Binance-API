# Multiprocessing in Python

## Introduction:
-I recommend to run the code by jupyter.
-In order to take advantage of multi processing in Python, Threads package is a good starting point.
-In this page, I want to show how to get price of a currency from binance and stop that process by asking user to decide it.
-Stopping threads which run forever loops is not easy and mostly the solution is restart the kerel. But I suggest a way to stop the mentioned thread without interrupting the kernel.

## The problem:
-We want to write a program to get the most recent price of Ripple (XRPBTC) from Binance server. Because server responses every minutes
we need to **delay** the process to avoid getting redundant and repepetive data.
-We want to stop the procedure of getting data by asking user to do it. Therefore we need to use **Threads module** to run two different procedure tpgether.

## Delay and Time:
-**Time** module, included **time.sleep(t)** which **t** is amount of delay in seconds.
-**datetime** module can return the current time.
## Two Functions:
-The frist function fetch the price data from the server. And print the most current data and time of fetching it. This time is user's system time.
-Second function will ask the user to decide whether the first function stop or not. The input 0 will stop the threads.

## Additional Points:
-A thread cannot be started more than one time. The command thread = threading.Thread(target=func()), should be called again for another start.
-Thread will not be started unless the thread.start() is called. 
-Global variable: it can be defined by, global variable_name. In each function, the command global variable_name is needed.

##Code:

import threading 
from threading import Thread
import time
from datetime import datetime

def getPrice(): #Function to get the price of XRPBTC
    global stopPrice
    global price
    while True:
        if (stopPrice==0):
            break
        price=float(client.get_recent_trades(symbol='XRPBTC')[499]['price']) #Server return 500 recent price, but we need the last one
        print('XRPBTC '+ str(datetime.now()), price) #datetime.now() return system time
        time.sleep(30) #Delay
       
def stopPriceFunc():
    global stopPrice
    stopPrice = int(input("Input 0 to stop the program: ")) # I assume the user will not use other values, because the thread won't be stopped. A simple while loop can control this issue!
    
threads = []
tGetPrice = threading.Thread(target=getPrice)
tGetStopPrice= threading.Thread(target=stopPriceFunc)
#Remember: Still the threads are not started

tGetPrice.start()

tGetStopPrice.start()

Thanks for reading this article:
Milad Shaddelan
MSc. Business Analytics & MBA
University of Texas at Dallas
