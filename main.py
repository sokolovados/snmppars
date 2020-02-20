from dictGen import allvlangen
from dictGen import untagged
from snmpVLAN import snmp
from pprint import pprint


snmpout1 = snmp('10.220.43.168','nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.1') #community и ip  в переменных

listofvlan = allvlangen(snmpout1) #все вланы на коммуте

snmpout2 = snmp('10.220.43.168','nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.4')
snmpout3 = snmp('10.220.43.168','nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.2')

untaggeddict,taggeddict = untagged(snmpout2,snmpout3)
#for k,v in untaggeddict.items():
#    print(k + ':' +v)
pprint(untaggeddict)

pprint(taggeddict)




