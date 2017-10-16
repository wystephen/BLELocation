# -*- coding:utf-8 -*-
# Created by steve @ 17-10-16 下午2:44
'''
                   _ooOoo_ 
                  o8888888o 
                  88" . "88 
                  (| -_- |) 
                  O\  =  /O 
               ____/`---'\____ 
             .'  \\|     |//  `. 
            /  \\|||  :  |||//  \ 
           /  _||||| -:- |||||-  \ 
           |   | \\\  -  /// |   | 
           | \_|  ''\---/''  |   | 
           \  .-\__  `-`  ___/-. / 
         ___`. .'  /--.--\  `. . __ 
      ."" '<  `.___\_<|>_/___.'  >'"". 
     | | :  `- \`.;`\ _ /`;.`/ - ` : | | 
     \  \ `-.   \_ __\ /__ _/   .-` /  / 
======`-.____`-.___\_____/___.-`____.-'====== 
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
         佛祖保佑       永无BUG 
'''


import matplotlib.pyplot as  plt

import numpy as np
import scipy as sp
import pandas

from TimeStampConvert import timestampconvert

import os

if __name__ == '__main__':

    dir_name = '/home/steve/Data/BLELocation/1/'

    the_file_list = list()

    for f in os.listdir(dir_name):
        if 'txt' in f:
            tmp_file = open(dir_name + f)
            the_file_list = tmp_file.readlines()

    print(len(the_file_list))

    print(len(the_file_list[1].split(',')))

    all_data = np.zeros([len(the_file_list)-1,len(the_file_list)-1])

    for i in range(1,len(the_file_list)-1):

        tmp_str = the_file_list[i]
        print('current line :',tmp_str)
        all_data[i,0] = timestampconvert(tmp_str.split(',')[0])
        for j in range(1,len(tmp_str.split(','))-1):
            all_data[i,j] = float(tmp_str.split(',')[j])


    all_data = all_data[1:,:]*1.0
    ### time,x,y, rssi0,rssi1 .... rssi n
    plt.figure()
    plt.plot(all_data[:,0])
    plt.grid()

    plt.figure()
    plt.plot(all_data[:,1],all_data[:,2])
    plt.grid()

    plt.figure()
    for i in range(3,all_data.shape[1]):
        plt.plot(all_data[:,i],'.-')
    plt.grid()


    plt.figure()
    for i in range(3,10):
        plt.plot(all_data[:,i],'-*',label=str(i-2))
    plt.legend()
    plt.show()



