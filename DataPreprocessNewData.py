# -*- coding:utf-8 -*-
# Created by steve @ 17-10-18 下午7:00
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
from SmoothRssi import smoothrssi

import os

if __name__ == '__main__':

    dir_name = '/home/steve/Data/BLELocation/6/'

    the_file_list = list()

    for f in os.listdir(dir_name):
        if 'txt' in f:
            tmp_file = open(dir_name + f)
            the_file_list = tmp_file.readlines()

    print(len(the_file_list))

    print(len(the_file_list[1].split(',')))

    all_data = np.zeros([len(the_file_list), 80])

    # for i in range( len(the_file_list) - 1):
    #
    #     tmp_str = the_file_list[i]
    #     print('current line :', tmp_str)
    #     all_data[i, 0] = timestampconvert(tmp_str.split(',')[0])
    #     for j in range(all_data.shape[1]):
    #         all_data[i, j] = float(tmp_str.split(',')[j*2+2])
    #
    # # all_data = all_data[1:, :] * 1.0
    # ### time,x,y, rssi0,rssi1 .... rssi n
    '''
    Find all MAC
    '''
    mac_dic = dict()

    for tmp_str in the_file_list:
        mac_str = tmp_str.split(',')[1]
        if not mac_str in mac_dic:


    # all_data = smoothrssi(all_data,2.0)
    plt.figure()
    plt.title('time stamp')
    plt.plot(all_data[:, 0], '-*')
    plt.grid()
    plt.figure()
    plt.title('time interval')
    plt.plot(all_data[1:, 0] - all_data[:-1, 0], '-*')
    plt.grid()

    print('average time interval :', np.mean(all_data[1:, 0] - all_data[:-1, 0]))

    plt.figure()
    plt.plot(all_data[:, 1], all_data[:, 2], '-*')
    plt.grid()

    plt.figure()
    for i in range(3, all_data.shape[1]):
        plt.plot(all_data[:, i], '.-')
    plt.grid()

    plt.figure()
    for i in range(3, 10):
        plt.plot(all_data[:, i], '-*', label=str(i - 2))
    plt.legend()

    matrix_dis = np.zeros([all_data.shape[0], all_data.shape[0]])
    for i in range(all_data.shape[0]):
        for j in range(all_data.shape[0]):
            matrix_dis[i, j] = np.linalg.norm(all_data[i, 3:] - all_data[j, 3:])

    plt.figure()
    plt.title('rssi distance')
    plt.imshow(matrix_dis)

    plt.figure()
    plt.title('rssi matrix')
    plt.imshow(all_data[:, 3:].transpose())
    plt.xlim((0, all_data.shape[1] - 3))
    plt.ylim((0, all_data.shape[0]))

    plt.show()