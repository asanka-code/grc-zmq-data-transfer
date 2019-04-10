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

def consumer():
    consumer_id = random.randrange(1,10005)
    print("I am consumer #%s" % (consumer_id))
    context = zmq.Context()
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    
    while True:
        buff = consumer_receiver.recv()
        print(time.time())
        data = np.frombuffer(buff, dtype="float32")
        data = data[0::2] + 1j*data[1::2]
        print(type(data))
        print(len(data))
        #plt.figure()
        #plt.psd(data, NFFT=len(data), Fs=4e6, Fc=1e3)
        #plt.savefig("psd.png")
        #time.sleep(0.5)
        #exit()
        
consumer()
