from snmpVLAN import snmp
from pprint import pprint
from collections import OrderedDict,defaultdict
import re

# генерирует словарь vlanvlan- port
def allvlangen(unit): # на входе должен получать файл с snmp выводом по 1 
    allvlan = []
    regexallvlan = (r'(2.17.7.1.4.3.1.1.)(\d+)')
    for line in unit:
        match = re.search(regexallvlan,line)
        allvlan.append(match.group(2)) 
    return(allvlan) # список vlan

def untagged(unit,unit1): #на входе получает snmp вывод untagged портов, формирует словарь port:vlan
    untaggedvlan = defaultdict(list)
    taggedvlan = defaultdict(list)
    vlanport = {}
    regexuntagged = (r'(2.17.7.1.4.3.1.4.)(\d+)( = 0x)(\w+)')
    regexuntagged_2 = (r'(2.17.7.1.4.3.1.2.)(\d+)( = 0x)(\w+)')
    for line,line1 in zip(unit,unit1):
        #________________________________#
        binresult = ''
        binresult_all = ''
        bin_tag = ''
        match = re.search(regexuntagged,line)
        match_All = re.search(regexuntagged_2,line1)
        if match:
            vlan = match.group(2) # untagged portsi
            ports = match.group(4)  
        else:
            break
        if match_All:

            Vlan_All = match_All.group(2) # all ports
            Ports_All = match_All.group(4)
        else:
            pass
        #_________________________________#
        ######## получает двоичное значение по untag портам#
        for hexsymbol in ports:
            hexsymbol = (bin(int(hexsymbol,16)))[2:]
            while int(len(hexsymbol))<4:
                hexsymbol= '0'+hexsymbol
            binresult = binresult+hexsymbol
        ######## получает двоичное занчение all_ports с untag портами#
        for hexsymbol_all in Ports_All:
            hexsymbol_all = (bin(int(hexsymbol_all,16)))[2:]
            while int(len(hexsymbol_all))<4:
                hexsymbol_all= '0'+hexsymbol_all
            binresult_all = binresult_all + hexsymbol_all
        
        for bin_untag,bin_all in zip(binresult,binresult_all):
            if bin_untag is '1' and bin_all is '1':
                bin_tag = bin_tag + '0'
            else:
                bin_tag =bin_tag + bin_all
        
        ##формирует untag словарь## 
        num = 1
        for element in binresult:
            if element is '1':
                (untaggedvlan[str(num)]).append(vlan)
                num += 1
            else:
                num +=1       
        ##формирует tagged словарь##
        num2 = 1    
        for element in bin_tag:
            if element is '1':
                (taggedvlan[str(num2)]).append(vlan)
                num2 += 1
            else:
                num2 +=1
       ##формирует общий словарь по портам ! ДОПИСАТЬ range ! 
        for key in untaggedvlan:
            vlanport[key] = {'untag':(str(untaggedvlan[key])).strip("[]'")}
        for key in taggedvlan:
            vlanport[key].update({'tagged': (str(taggedvlan[key])).strip("[]'")})
        
    return(vlanport)
     ##################
    


