from dictGen import allvlangen
from dictGen import untagged
from snmpVLAN import snmp
from pprint import pprint
from jinja2 import Template,Environment, FileSystemLoader
from start import start


ipaddresses = start()
print('######GENERATE######')
for ip in ipaddresses:
    snmpout1 = snmp(ip,'nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.1') #community и ip  в переменных
    if snmpout1 is False:
        print('*'*20)
        pass
    else:
            
        listofvlan = allvlangen(snmpout1) #все вланы на коммуте
        snmpout2 = snmp(ip,'nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.4')
        snmpout3 = snmp(ip,'nfrnjrfr','.1.3.6.1.2.1.17.7.1.4.3.1.2')
        sysdescr = snmp(ip,'nfrnjrfr','1.3.6.1.2.1.1.1')
        print('snmpwalk to ' + ip + ' sucsess')
        vlanport = untagged(snmpout2,snmpout3,sysdescr,ip)
        env = Environment(loader = FileSystemLoader('/home/python_projects/snmppars/'))
        template = env.get_template('template.txt') 
        print('creating a config for ' +ip)

        with open(ip+'.cfg','w') as f:
            f.write(template.render(vlanport=vlanport))
            
        print('DONE!')
        print('*'*20)





