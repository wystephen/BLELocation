# -*- coding:utf-8 -*-
# Created by steve @ 17-10-17 下午7:41
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

def smoothrssi(data,constant_time = 2.0):
    '''

    :param data: time,rssi0, rssi1 ...rssi80
    :param constant_time:
    :return:
    '''
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
            if data[i, 0] - initial_time[j - 1] > constant_time:
                initial_val[j-1] = 0.0

        new_data[i, 0] = data[i, 0] * 1.0
        new_data[i, 1:] = initial_val * 1.0
        print(i,':')
        print(data[i,1:])
        print(new_data[i,1:])

    data = new_data * 1.0
    return data