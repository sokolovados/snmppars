from snmpVLAN import snmp
import defauldict
import re

# генерирует словарь vlanvlan- port
def allvlangen(unit): # на входе должен получать файл с snmp выводом по 1 
    allvlan = []
    regexallvlan = (r'(2.17.7.1.4.3.1.1.)(\d+)')
    for line in unit:
        match = re.search(regexallvlan,line)
        #print(match.group(2))
        allvlan.append(match.group(2)) 
    return(allvlan) # список vlan

def untagged(unit):
    untaggedvlan = {}
    regexuntagged = (r'(2.17.7.1.4.3.1.4.)(\d+)( = 0x)(\w+)')
    print(unit)
    for line in unit:
        match = re.search(regexuntagged,line)
        vlan = match.group(2)
        binresult = (bin(int(((match.group(4))[:-3]),16))[2:])
        num = 1
        for element in binresult:
            
            if element is '1':
                untaggedvlan.update({('port '+str(num)):vlan})
                num += 1
                print(untaggedvlan)

    return(untaggedvlan)

        
