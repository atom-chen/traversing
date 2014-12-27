# -*- coding: utf-8 -*-
'''
Created on 2014-11-28

@author: hack
'''
import cPickle
from myredis import Ranking

class MineOpt(object):
    rank = Ranking()
    def __init__(self):
        pass
    
    @classmethod
    def add_mine(cls, uid, mid, data):
        v = cPickle.dumps(data)
        label = 'mine.%s' % uid
        
        cls.rank.hset(label, mid, 1)
        label = 'mine'
        print 'add_mine------', label, mid, data
        cls.rank.hset(label, mid, v)
        
    @classmethod
    def rem_mine(cls, mid):
        label = 'mine'
        cls.rank.hdel(label, mid)
        
    @classmethod
    def get_mine(cls, mid):
        label = 'mine'
        ret = cls.rank.hget(label, mid)
        print 'get_mine------', label, mid, cPickle.loads(ret)
        return cPickle.loads(ret)
    
    @classmethod
    def get_user_mines(cls, uid):
        label = 'mine.%s' % uid
        mids = cls.rank.hkeys(label)
        return mids
    
    @classmethod
    def lock(cls, tid):
        label = 'mine.lock'
        val = cls.rank.zincrby(label, tid, 1)
        return val
    
    @classmethod
    def unlock(cls, tid):
        label = 'mine.lock'
        cls.rank.zadd(label, tid, 0)
        
    @classmethod
    def update(cls, label, k, v):
        """
        label : "user_level","sword",玩家等级，团队战力
        """
        old_score = cls.rank.zget(label, k)
        if old_score:
            if old_score >= v:
                return
        cls.rank.zadd(label, k, v)

    @classmethod
    def rand_user(cls, label, k, front, back):
        """
        label : "user_level","sword",玩家等级，团队战力
        """
        ret = cls.rank.znear(label, k, front, back)
        return ret
    @classmethod
    def get_user(cls, label, k):
        """
        label : "user_level","sword",玩家等级，团队战力
        """
        ret = cls.rank.zget(label, k)
        return ret
    