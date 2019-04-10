#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:39:15 2019

@author: asanka
"""

import time
import zmq
import random
import numpy as np
import matplotlib.pyplot as plt

def subscriber():
    consumer_id = random.randrange(1,10005)
    print("I am subscriber #%s" % (consumer_id))
    context = zmq.Context()
    subscriber_receiver = context.socket(zmq.SUB)
    subscriber_receiver.setsockopt_string(zmq.SUBSCRIBE, "")
    subscriber_receiver.connect("tcp://127.0.0.1:5557")
    
    while True:
        buff = subscriber_receiver.recv()
        print(time.time())
        data = np.frombuffer(buff, dtype="float32")
        data = data[0::2] + 1j*data[1::2]
        print(type(data))
        print(len(data))
        #plt.figure()
        #plt.psd(data, NFFT=len(data), Fs=4e6, Fc=1e3)
        #plt.savefig("psd_sub.png")
        #time.sleep(0.5)
        #exit()
        
subscriber()
