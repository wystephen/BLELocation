# -*- coding:utf-8 -*-
# Created by steve @ 17-10-17 下午6:13
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

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from TimeStampConvert import timestampconvert
from Rssi2Dis import rssi2dis

import os

if __name__ == '__main__':

    dir_name = '/home/steve/Data/BLELocation/src_data/'
    file_name = os.listdir(dir_name)[0]

    the_file = open(dir_name + file_name)
    lines_str = the_file.readlines()

    data = np.zeros([len(lines_str), 81])

    for i in range(data.shape[0]):
        tmp_str = lines_str[i]
        data[i, 0] = timestampconvert(tmp_str.split(',')[0])

        for j in range(1, data.shape[1]):
            data[i, j] = float(tmp_str.split(',')[j * 2])
            # data[i,j] = rssi2dis(data[i,j])

    plt.figure()
    plt.title('all data')
    plt.imshow(data[:, 1:])
    plt.grid()

    distance_matrix = np.zeros([data.shape[0], data.shape[0]])
    for i in range(distance_matrix.shape[0]):
        for j in range(distance_matrix.shape[1]):
            distance_matrix[i, j] = np.linalg.norm(data[i, 1:] - data[j, 1:])

    # distance_matrix = distance_matrix / np.linalg.norm(distance_matrix, axis=1)
    plt.figure()
    plt.title('all distance ')
    plt.imshow(distance_matrix)
    print(data)

    # add
    initial_val = data[0, 1:]*1.0
    initial_time = np.zeros_like(initial_val)
    initial_time += data[0, 0]

    new_data = np.zeros_like(data)

    for i in range(data.shape[0]):

        # updata intiial_val
        for j in range(1, data.shape[1]):
            if data[i, j] < 0.0:
                initial_val[j - 1] = data[i, j]
                initial_time[j - 1] = data[i, 0]

        # clear initial val
        for j in range(1, data.shape[1]):
            if data[i, 0] - initial_time[j - 1] > 2.0:
                initial_val[j-1] = 0.0

        new_data[i, 0] = data[i, 0] * 1.0
        new_data[i, 1:] = initial_val * 1.0
        print(i,':')
        print(data[i,1:])
        print(new_data[i,1:])

    data = new_data * 1.0

    print(data)

    plt.figure()
    plt.title('all new data')
    plt.imshow(data[:, 1:])
    plt.grid()

    distance_matrix = np.zeros([data.shape[0], data.shape[0]])
    for i in range(distance_matrix.shape[0]):
        for j in range(distance_matrix.shape[1]):
            distance_matrix[i, j] = np.linalg.norm(data[i, 1:] - data[j, 1:])

    # distance_matrix = distance_matrix / np.linalg.norm(distance_matrix, axis=1)
    plt.figure()
    plt.title('all new distance ')
    plt.imshow(distance_matrix)

    plt.show()
