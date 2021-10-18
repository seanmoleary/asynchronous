# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:15:25 2021

@author: seoleary
"""

import time
import asyncio


async def counter(name, delay):
    
    tab = (ord(name)-ord('A'))*'\t'
    number =3
    
    while number>0:
        
        
        await asyncio.sleep(delay)
        
        count = time.perf_counter()-start
        
        print('-'*40)
        print('%.4f \t%s%s=%i'% (count, tab, name, number))
        
        number-=1
      
loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(counter('A',1)),
    loop.create_task(counter('B',.8)),
    loop.create_task(counter('C',.5))
    ]

start= time.perf_counter()

loop.run_until_complete(asyncio.wait(tasks))


