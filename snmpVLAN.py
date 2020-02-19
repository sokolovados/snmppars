from pysnmp.hlapi import *

def snmp(ip,com,mib):
    result = []
    for (errorIndication,
         errorStatus,
        errorIndex,
        varBinds) in bulkCmd(SnmpEngine(),
            CommunityData(com),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            0, 25,  # fetch up to 25 OIDs one-shot
            ObjectType(ObjectIdentity(mib)),
            lexicographicMode=False):
        if errorIndication or errorStatus:
            print(errorIndication or errorStatus)
            break
        else:
            for varBind in varBinds:
                result.append(' = '.join([x.prettyPrint() for x in varBind]))
    return(result)
#res = snmpout1 = snmp('10.220.43.168','nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.4')


