#!/usr/bin/env python
# -*- coding: utf-8 -*
# author: SAI
import os,sys,time
import pykd
import struct
import socket
from common import *

g_protocols = {
    0:"HOPOPT",
    1:"ICMP",
    2:"IGMP",
    3:"GGP",
    4:"IPv4",
    5:"ST",
    6:"TCP",
    7:"CBT",
    8:"EGP",
    9:"IGP",
    10:"BBN-RCC-MON",
    11:"NVP-II",
    12:"PUP",
    13:"ARGUS",
    14:"EMCON",
    15:"XNET",
    16:"CHAOS",
    17:"UDP",
    18:"MUX",
    19:"DCN-MEAS",
    20:"HMP",
    21:"PRM",
    22:"XNS-IDP",
    23:"TRUNK-1",
    24:"TRUNK-2",
    25:"LEAF-1",
    26:"LEAF-2",
    27:"RDP",
    28:"IRTP",
    29:"ISO-TP4",
    30:"NETBLT",
    31:"MFE-NSP",
    32:"MERIT-INP",
    33:"DCCP",
    34:"3PC",
    35:"IDPR",
    36:"XTP",
    37:"DDP",
    38:"IDPR-CMTP",
    39:"TP++",
    40:"IL",
    41:"IPv6",
    42:"SDRP",
    43:"IPv6-Route",
    44:"IPv6-Frag",
    45:"IDRP",
    46:"RSVP",
    47:"GRE",
    48:"DSR",
    49:"BNA",
    50:"ESP",
    51:"AH",
    52:"I-NLSP",
    53:"SWIPE",
    54:"NARP",
    55:"MOBILE",
    56:"TLSP",
    57:"SKIP",
    58:"IPv6-ICMP",
    59:"IPv6-NoNxt",
    60:"IPv6-Opts",
    61:"Host-interal",
    62:"CFTP",
    63:"Local Network",
    64:"SAT-EXPAK",
    65:"KRYPTOLAN",
    66:"RVD",
    67:"IPPC",
    68:"Dist-FS",
    69:"SAT-MON",
    70:"VISA",
    71:"IPCV",
    72:"CPNX",
    73:"CPHB",
    74:"WSN",
    75:"PVP",
    76:"BR-SAT-MON",
    77:"SUN-ND",
    78:"WB-MON",
    79:"WB-EXPAK",
    80:"ISO-IP",
    81:"VMTP",
    82:"SECURE-VMTP",
    83:"VINES",
    84:"TTP",
    84:"IPTM",
    85:"NSFNET-IGP",
    86:"DGP",
    87:"TCF",
    88:"EIGRP",
    89:"OSPFIGP",
    90:"Sprite-RPC",
    91:"LARP",
    92:"MTP",
    93:"AX.25",
    94:"IPIP",
    95:"MICP",
    96:"SCC-SP",
    97:"ETHERIP",
    98:"ENCAP",
    99:"Encryption",
    100:"GMTP",
    101:"IFMP",
    102:"PNNI",
    103:"PIM",
    104:"ARIS",
    105:"SCPS",
    106:"QNX",
    107:"A/N",
    108:"IPComp",
    109:"SNP",
    110:"Compaq-Peer",
    111:"IPX-in-IP",
    112:"VRRP",
    113:"PGM",
    114:"0-hop",
    115:"L2TP",
    116:"DDX",
    117:"IATP",
    118:"STP",
    119:"SRP",
    120:"UTI",
    121:"SMP",
    122:"SM",
    123:"PTP",
    124:"ISIS over IPv4",
    125:"FIRE",
    126:"CRTP",
    127:"CRUDP",
    128:"SSCOPMCE",
    129:"IPLT",
    130:"SPS",
    131:"PIPE",
    132:"SCTP",
    133:"FC",
    134:"RSVP-E2E-IGNORE",
    135:"Mobility Header",
    136:"UDPLite",
    137:"MPLS-in-IP",
    138:"manet",
    139:"HIP",
    140:"Shim6",
    141:"WESP",
    142:"ROHC",
    143:"Unassigned",
    144:"Unassigned",
    145:"Unassigned",
    146:"Unassigned",
    147:"Unassigned",
    148:"Unassigned",
    149:"Unassigned",
    150:"Unassigned",
    151:"Unassigned",
    152:"Unassigned",
    153:"Unassigned",
    154:"Unassigned",
    155:"Unassigned",
    156:"Unassigned",
    157:"Unassigned",
    158:"Unassigned",
    159:"Unassigned",
    160:"Unassigned",
    161:"Unassigned",
    162:"Unassigned",
    163:"Unassigned",
    164:"Unassigned",
    165:"Unassigned",
    166:"Unassigned",
    167:"Unassigned",
    168:"Unassigned",
    169:"Unassigned",
    170:"Unassigned",
    171:"Unassigned",
    172:"Unassigned",
    173:"Unassigned",
    174:"Unassigned",
    175:"Unassigned",
    176:"Unassigned",
    177:"Unassigned",
    178:"Unassigned",
    179:"Unassigned",
    180:"Unassigned",
    181:"Unassigned",
    182:"Unassigned",
    183:"Unassigned",
    184:"Unassigned",
    185:"Unassigned",
    186:"Unassigned",
    187:"Unassigned",
    188:"Unassigned",
    189:"Unassigned",
    190:"Unassigned",
    191:"Unassigned",
    192:"Unassigned",
    193:"Unassigned",
    194:"Unassigned",
    195:"Unassigned",
    196:"Unassigned",
    197:"Unassigned",
    198:"Unassigned",
    199:"Unassigned",
    200:"Unassigned",
    201:"Unassigned",
    202:"Unassigned",
    203:"Unassigned",
    204:"Unassigned",
    205:"Unassigned",
    206:"Unassigned",
    207:"Unassigned",
    208:"Unassigned",
    209:"Unassigned",
    210:"Unassigned",
    211:"Unassigned",
    212:"Unassigned",
    213:"Unassigned",
    214:"Unassigned",
    215:"Unassigned",
    216:"Unassigned",
    217:"Unassigned",
    218:"Unassigned",
    219:"Unassigned",
    220:"Unassigned",
    221:"Unassigned",
    222:"Unassigned",
    223:"Unassigned",
    224:"Unassigned",
    225:"Unassigned",
    226:"Unassigned",
    227:"Unassigned",
    228:"Unassigned",
    229:"Unassigned",
    230:"Unassigned",
    231:"Unassigned",
    232:"Unassigned",
    233:"Unassigned",
    234:"Unassigned",
    235:"Unassigned",
    236:"Unassigned",
    237:"Unassigned",
    238:"Unassigned",
    239:"Unassigned",
    240:"Unassigned",
    241:"Unassigned",
    242:"Unassigned",
    243:"Unassigned",
    244:"Unassigned",
    245:"Unassigned",
    246:"Unassigned",
    247:"Unassigned",
    248:"Unassigned",
    249:"Unassigned",
    250:"Unassigned",
    251:"Unassigned",
    252:"Unassigned",
    253:"Experimental",
    254:"Experimental",
    255:"Reserved",
}

def listConnections():
    pass
    
def listSocket():
    try:
        r=pykd.dbgCommand('.reload tcpip.sys')
        if is_2000():
            print 'no support'
        elif is_xp() or is_2003():
            AddrObjTable=pykd.getOffset('tcpip!AddrObjTable')
            AddrObjTable=pykd.ptrPtr(AddrObjTable)
            AddrObjTableSize=pykd.getOffset('tcpip!AddrObjTableSize')
            AddrObjTableSize=pykd.ptrPtr(AddrObjTableSize)
            print '='*20
            print 'AddrObjTable:%x AddrObjTableSize:%d' % (AddrObjTable, AddrObjTableSize)
            if pykd.is64bitSystem():
                Next_offset=0
                localIP_offset=0x58 #4bytes
                LocalPort_offset=0x5c#2bytes
                Protocol_offset=0x5e #2bytes
                pid_offset=0x238 #4bytes
            else:
                if is_xp():
                    Next_offset=0
                    localIP_offset=0x2c #4bytes
                    LocalPort_offset=0x30#2bytes
                    Protocol_offset=0x32 #2bytes
                    pid_offset=0x148 #4bytes
                    
                elif is_2003():
                    Next_offset=0
                    localIP_offset=0x30 #4bytes
                    LocalPort_offset=0x34#2bytes
                    Protocol_offset=0x36 #2bytes
                    pid_offset=0x14c #4bytes
            
            print 'local remote protocol pid'
            for i in xrange(AddrObjTableSize):
                obj=pykd.ptrPtr(AddrObjTable+i*g_mwordsize)
                while obj!=0:
                    LocalIP=pykd.ptrMWord(obj+localIP_offset)
                    LocalPort=pykd.ptrWord(obj+LocalPort_offset)
                    LocalPort=socket.htons(LocalPort)
                    Protocol=pykd.ptrWord(obj+Protocol_offset)
                    pid=pykd.ptrMWord(obj+pid_offset)
                    Protocol=g_protocols.get(Protocol)
                    print '%16s:%5d *.* %10s %d' % (socket.inet_ntoa(struct.pack('I', LocalIP)), LocalPort, Protocol, pid)
                    obj=pykd.ptrPtr(obj+Next_offset)

            print '='*20
            
            TCBTable=pykd.getOffset('tcpip!TCBTable')
            TCBTable=pykd.ptrPtr(TCBTable)
            MaxHashTableSize=pykd.getOffset('tcpip!MaxHashTableSize')
            MaxHashTableSize=pykd.ptrPtr(MaxHashTableSize)
            print 'TCBTable:%x MaxHashTableSize:%d' % (TCBTable, MaxHashTableSize)
            
            Next_offset=0
            RemoteIP_offset=0x0c#4bytes
            LocalIP_offset=0x10#4bytes
            RemotePort_offset=0x14#2bytes
            LocalPort_offset=0x16 #2bytes
            pid_offset=0x18 #4bytes
                
            print 'local remote protocol pid'
            for i in xrange(MaxHashTableSize):
                obj=pykd.ptrPtr(TCBTable+i*g_mwordsize)
                while obj!=0:
                    RemoteIP=pykd.ptrMWord(obj+RemoteIP_offset)
                    LocalIP=pykd.ptrMWord(obj+LocalIP_offset)
                    RemotePort=pykd.ptrWord(obj+RemotePort_offset)
                    RemotePort=socket.htons(RemotePort)
                    LocalPort=pykd.ptrWord(obj+LocalPort_offset)
                    LocalPort=socket.htons(LocalPort)
                    pid=pykd.ptrMWord(obj+pid_offset)
                    print '%16s:%5d %16s:%5d  TCP %d' % (socket.inet_ntoa(struct.pack('I', LocalIP)), LocalPort, socket.inet_ntoa(struct.pack('I', RemoteIP)), RemotePort, pid)
                    obj=pykd.ptrPtr(obj+Next_offset)
        else:
            print 'no support'
        
        
    except Exception, err:
        print err
    
if __name__=='__main__':
    listSocket()
    listConnections()
    
    pass

