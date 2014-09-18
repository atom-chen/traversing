#coding:utf8
"""
Created on 2013-8-14

@author: lan (www.9miao.com)
"""
from gfirefly.server.globalobject import GlobalObject
from gfirefly.netconnect.datapack import DataPackProtoc


def conn_made(conn):
    '''当连接建立时调用的方法'''
    if not GlobalObject().netfactory.connmanager.hasConnection(conn.transport.sessionno):
        queue_num = GlobalObject().netfactory.connmanager.queue_num
        GlobalObject().netfactory.pushObject(1326, str(queue_num), [conn.transport.sessionno])
    return


def conn_lost(conn):
    dynamic_id = conn.transport.sessionno
    if dynamic_id != 0:
        GlobalObject().remote['gate'].callRemoteNotForResult("net_conn_lost", dynamic_id)

    # pop queue conn to normal conn, when conn lost
    conn = GlobalObject().netfactory.connmanager.pop_queue()
    if conn:
        GlobalObject().netfactory.pushObject(1326, str(0), [conn.instance.transport.sessionno])


GlobalObject().netfactory.doConnectionLost = conn_lost
GlobalObject().netfactory.doConnectionMade = conn_made
dataprotocl = DataPackProtoc(0, 0, 0, 0, 0, 0)
GlobalObject().netfactory.setDataProtocl(dataprotocl)


def load_module():
    import netapp
    import gatenodeapp