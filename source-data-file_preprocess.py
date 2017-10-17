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

import os
if __name__ == '__main__':

    dir_name = '/home/steve/Data/BLELocation/src_data/'
    file_name = os.listdir(dir_name)[0]

    the_file = open(dir_name+file_name)
    lines_str = the_file.readlines()


    data = np.zeros([len(lines_str),81])

    for i in range(data.shape[0]):
        tmp_str = lines_str[i]
        data[i,0] = timestampconvert(tmp_str.split(',')[0])

        for j in range(1,data.shape[1]):
            data[i,j] = float(tmp_str.split(',')[j*2])


    plt.figure()
    plt.title('all data')
    plt.imshow(data[:,1:])
    plt.grid()



    plt.show()

