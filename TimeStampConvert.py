# -*- coding:utf-8 -*-
# Created by steve @ 17-10-16 下午2:46
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



import time


def timestampconvert(str='10-04-31-73'):
    print(str)
    the_time = 0.0
    for i in range(3):
        # print(i)
        # print(str.split('-')[i],':',str.split('-')[i],':')
        the_time = the_time*60.0 + float(str.split('-')[i])
        if(i>0 and float(str.split('-')[i])>60.0):
            print('error at timestampconvert :',str,'some value is out of range')



    the_time += float(str.split('-')[3]) / 1000.0
    return the_time


if __name__ == '__main__':
    print('begin test')

    print('one hour',timestampconvert('1-0-0-0')-timestampconvert('0-0-0-0'))
    print('one min', timestampconvert('0-1-0-0'))
    print('one sec',timestampconvert('0-0-1-0'))
    print('100 ms',timestampconvert('0-0-0-100'))
    print('not out range',timestampconvert('1000'))


