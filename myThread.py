# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:50:26 2021

@author: seoleary

Provides a simple example class for implementing a thread for counting down, 
in the commented out code at the bottom, this class will implement two threads
that will not execute sequentially because of a built in delay
"""
import threading as th
import time

class myThread(th.Thread):
    def __init__(self, name, delay):
        th.Thread.__init__(self)
        self.name = name
        self.delay = delay
    
    def run(self):
        print('Starting thread %s.' % self.name)
        thread_count_down(self.name, self.delay)
        print('Finished thread %s.' % self.name)
        
def thread_count_down(name, delay):
    counter = 5
    
    while counter:
        time.sleep(delay)
        print('Thread %s is counting down: %i...'%(name, counter))
        counter-=1
        
'''

from myThread import myThread

thread1 = myThread('A',.5)
thread2 = myThread('B',.5)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

'''