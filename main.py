from dictGen import allvlangen
from dictGen import untagged
from snmpVLAN import snmp
from pprint import pprint
from jinja2 import Template,Environment, FileSystemLoader

snmpout1 = snmp('10.220.43.168','nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.1') #community и ip  в переменных

listofvlan = allvlangen(snmpout1) #все вланы на коммуте

snmpout2 = snmp('10.220.43.168','nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.4')
snmpout3 = snmp('10.220.43.168','nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.2')
sysdescr = snmp('10.220.43.168','nfrnjrfr','1.3.6.1.2.1.1.1')
vlanport = untagged(snmpout2,snmpout3,sysdescr)
pprint(vlanport)

env = Environment(loader = FileSystemLoader('/home/python_projects/snmppars/'))
template = env.get_template('template.txt')

with open('result.txt','w') as f:
    f.write(template.render(vlanport=vlanport))
    
print(type(vlanport))





