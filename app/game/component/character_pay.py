# -*- coding:utf-8 -*-
"""
created by server on 14-8-26
"""
# import time
# from gfirefly.server.logobj import logger
from app.game.component.Component import Component
from gfirefly.server.globalobject import GlobalObject
from gfirefly.server.logobj import logger
from shared.utils.const import const


class CharacterPay(Component):

    def __init__(self, owner):
        super(CharacterPay, self).__init__(owner)
        self._platform = 0
        self._openid = ""
        self._open_key = ""
        self._pay_token = ""
        self._appid = ""
        self._pf = ""
        self._pfkey = ""
        self._zoneid = 0

    def set_pay_arg(self, value):
        self._platform = value.get("platform")
        self._openid = str(value.get("openid"))
        self._openkey = str(value.get("openkey"))
        self._pay_token = str(value.get("pay_token"))
        self._appid = str(value.get("appid"))
        self._appkey = str(value.get("appkey"))
        self._pf = str(value.get("pf"))
        self._pfkey = str(value.get("pfkey"))
        self._zoneid = str(value.get("zoneid"))
        self.get_balance() # 登录时从tx拉取gold

    def _get_balance_m(self):
        logger.debug("_get_balance_m: platform- %s\
                     openid- %s \
                     openkey - %s \
                     pay_token - %s \
                     appid - %s \
                     appkey - %s \
                     pf - %s \
                     pfkey - %s \
                     zoneid - %s "%
                     (self._platform, self._openid,
                      self._openkey, self._pay_token,
                      self._appid, self._appkey,
                      self._pf,
                      self._pfkey, self._zoneid))
        if not const.REMOTE_DEPLOYED:
            return
        try:
            data = GlobalObject().pay.get_balance_m(self._platform, self._openid, self._appid,
                                         self._appkey, self._openkey, self._pay_token,
                                         self._pf, self._pfkey, self._zoneid)
            logger.debug(data)
        except Exception, e:
            logger.error("get balance error:%s" % e)
            return

        if data['ret'] == 1018:
            return False
        elif data['ret'] != 0:
            logger.error("get_balance failed: %s" % data)
            return
        balance = data['balance']
        gen_balance = data['gen_balance']
        return balance, gen_balance

    def get_balance(self):
        result = self._get_balance_m()
        if not result:
            return False

        balance, gen_balance = result # 充值结果：balance 当前值， gen_balance 赠送
        recharge_balance = balance - gen_balance # 累计充值数量
        if recharge_balance > 0:
            self._owner.base_info.set_vip_level(recharge_balance)
        self._owner.finance.gold = balance
        self._owner.finance.save_data()
        return True

    def _pay_m(self, num):
        result = {}
        try:
            result = GlobalObject().pay.pay_m(self._platform, self._openid, self._appid,
                                         self._appkey, self._openkey, self._pay_token,
                                         self._pf, self._pfkey, self._zoneid, num)
        except Exception, e:
            logger.error("pay error:%s" % e)
            return

        if result['ret'] == 1018:
            return False
        elif result['ret'] != 0:
            logger.error("pay_m failed: %s", result)
            return False
        billno = result['billno']
        balance = result['balance']
        return billno, balance



    def pay(self, num, func=None, *args, **kwargs):
        """
        func: 发货方法
        args, kwargs: 发货方法的参数
        """
        result = self._pay_m(num)
        if not result:
            return False
        gain_res = []
        if not func:
            self.get_balance()
            return gain_res
        billno, _balance = result

        try:
            gain_res = func(*args, **kwargs)
        except:
            self._cancel_pay_m(num, billno)
            return False
        self.get_balance()
        return gain_res

    def _cancel_pay_m(self, num, billno):
        """
        取消订单
        """
        result = {}
        try:
            result = GlobalObject().pay.pay_m(self._platform, self._openid, self._appid,
                                         self._appkey, self._openkey, self._pay_token,
                                         self._pf, self._pfkey, self._zoneid, num)
        except Exception, e:
            logger.error("pay error:%s" % e)
            return

        if result['ret'] == 1018:
            return False
        elif result['ret'] != 0:
            logger.error("cancel_pay_m failed: %s", result)
        return True

    def _present_m(self, num):
        """
        赠送gold, 用于掉落包中的gold
        """
        result = {}
        try:
            pay = GlobalObject().pay
            discountid = pay.discountid
            giftid = pay.giftid
            result = GlobalObject().pay.present_m(self._platform, self._openid, self._appid,
                                            self._appkey, self._openkey, self._pay_token,
                                            self._pf, self._pfkey, self._zoneid, discountid, giftid, num)
        except Exception, e:
            logger.error("present error:%s" % e)
            return

        if result['ret'] == 1018:
            return False
        elif result['ret'] != 0:
            logger.error("present_m failed: %s", result)
            return False
        return True

    def present(self, num):
        """
        赠送gold, 用于掉落包中的gold, 更新gold
        """
        self._present_m(num)
        self.get_balance()
