# -*- coding:utf-8 -*-
"""
created by server on 14-7-23下午3:45.
"""
import time
if __name__ == '__main__':
    test = {123456: {'position': 1, 'contribution': 1, 'k_num': 2},
            123457: {'position': 1, 'contribution': 1, 'k_num': 3},
            123458: {'position': 2, 'contribution': 1, 'k_num': 2}}

    new_test = sorted(test.items(), key=lambda x: (-1 * x[1]['position'], x[1]['contribution'],
                                                   x[1]['k_num']), reverse=True)
    # new_test = test.pop(0)
    print new_test[-1][0]

    # test1 = {'info': {'name': u'gnamf', 'level': 1, 'fund': 0, 'call': '',
    #                   'p_list': {104L: {'position': 1, 'contribution': 0, 'k_num': 0}}, 'exp': 0, 'apply': [104L],
    #                   'p_num': 1, 'record': 0}}
    # test1.get('info').get('p_list').pop(104L)
    # print 'test1:', test1

    # d = u'中国1111aaa'
    # a = len("123")
    # b = len(d.encode('utf-8'))
    # c = len('中国1111aaa')
    # print '111111111111:', a, b, c, d

    # ------------Time---------------------------
    # print 'time:', int(time.time())

    # timeStamp = int(time.time())
    # timeArray = time.localtime(timeStamp)
    # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print 'otherStyleTime:', otherStyleTime

    # print '时间戳减法：', int(time.time())-1406602661
    # b = 1
    # for a in [1, 2, 3, 4, 5]:
    #     b += a
    # print 'b:', b