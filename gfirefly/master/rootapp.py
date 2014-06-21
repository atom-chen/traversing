#coding:utf8
'''
Created on 2013-8-7

@author: lan (www.9miao.com)
'''
from gfirefly.server.globalobject import GlobalObject
from gtwisted.utils import log


def _doChildConnect(name,transport):
    """当server节点连接到master的处理
    """
    # 当前启动的server 的配置
    print 'master dochildconnect:',  name, transport
    server_config = GlobalObject().json_config.get('servers',{}).get(name,{})
    print 'server_config:', server_config
    remoteport = server_config.get('remoteport',[])
    print 'remoteport:', remoteport
    child_host = transport.transport.address[0]
    print 'child_host:', child_host
    root_list = [rootport.get('rootname') for rootport in remoteport]
    print 'root_list:', root_list
    GlobalObject().remote_map[name] = {"host":child_host,"root_list":root_list}
    print 'remote_map:', GlobalObject().remote_map
    #通知有需要连的node节点连接到此root节点
    print root_list
    for servername,remote_list in GlobalObject().remote_map.items():
        remote_host = remote_list.get("host","")
        remote_name_host = remote_list.get("root_list","")
        if name in remote_name_host:
            GlobalObject().root.callChild(servername,"remote_connect",name,remote_host)
    #查看当前是否有可供连接的root节点
    master_node_list = GlobalObject().remote_map.keys()
    for root_name in root_list:
        if root_name in master_node_list:
            root_host = GlobalObject().remote_map[root_name]['host']
            GlobalObject().root.callChild(name,"remote_connect",root_name,root_host)
    
def _doChildLostConnect(childId):
    """
    """
    try:
        del GlobalObject().remote_map[childId]
    except Exception,e:
        log.msg(str(e))

GlobalObject().root.doChildConnect = _doChildConnect
GlobalObject().root.doChildLostConnect = _doChildLostConnect