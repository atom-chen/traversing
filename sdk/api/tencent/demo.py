# coding: utf-8
from sdk.api.tencent.midas_api import MidasApi

from sdk.api.tencent.msdk import Msdk
from sdk.util import logger


zone_id = 1001
host = 'msdk.qq.com'
pay_host = ('10.142.22.11', 8080)
buy_goods_host = ('10.142.22.11', 8080)
valid_host = ('10.130.2.233', 80)

qq_appid = 1104297231
qq_appkey = 'y33yRx3FveVZb1dw'
wx_appid = 'wxf77437c08cb06196'
wx_appkey = '8274b9e862581f8b4976ba90ad2d4b77'

pay_host = ('10.142.22.11', 8080)
goods_host = ('10.142.22.11', 8080)
valid_host = ('10.130.2.233', 80)
wx_rank_host = ('api.weixin.qq.com', 80)
qq_rank_host = ('10.153.96.115', 10000)

qzoneconfig = {'title':'', 'share_url':'', 'pics':''}


# Android
android_pay_appid = 1450000302
android_pay_appKey = 'vPriPtbnsDylVOLSHrExnTXBxOzYR80l'
android_discountid = 'UM13082314420414'
android_giftid = '1636707689PID20130823144204220'

# iOS
ios_pay_appid = 1450000303
ios_pay_appKey = 'JMJYLZVmk6H7uYXPStC7jaaUDN8yvxB4'
ios_discountid = 'UM130826111807639'
ios_giftid = '1636707689PID201308261118076461'


log = logger.new_log('TxApi')

# MSDK使用实例
msdk = Msdk(host, qq_appid, qq_appkey, wx_appid, wx_appkey, log=log)
res = msdk.verify_login(2, '8C9477C15CC283575062B2AB7C106C56', '88209224CA8FCD74EA4176F0BBFBB3A5')
print(res)

# Midas使用实例
#pay = MidasApi(host, goods_host, valid_host, log=log)
#res = pay.get_balance_m(1, 1, 1, 1, 1, 1, 1, 1)
#print(res)
