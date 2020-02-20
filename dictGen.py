from snmpVLAN import snmp

from collections import OrderedDict,defaultdict
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

def untagged(unit,unit1): #на входе получает snmp вывод untagged портов, формирует словарь port:vlan
    untaggedvlan = OrderedDict()
    taggedvlan = defaultdict(list)
    regexuntagged = (r'(2.17.7.1.4.3.1.4.)(\d+)( = 0x)(\w+)')
    regexuntagged_2 = (r'(2.17.7.1.4.3.1.2.)(\d+)( = 0x)(\w+)')
    #print(unit)
    for line,line1 in zip(unit,unit1):
        #________________________________#
        binresult = ''
        binresult_all = ''
        bin_tag = ''
        match = re.search(regexuntagged,line)
        match_All = re.search(regexuntagged_2,line1)
        vlan = match.group(2) # untagged ports
        ports =match.group(4)  
        Vlan_All = match_All.group(2) # all ports
        Ports_All = match_All.group(4)
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
        binresult = (bin(int(((match.group(4))[:-3]),16))[2:])
       ##формирует untag словарь## 
        num = 1
        for element in binresult:
            if element is '1':
                untaggedvlan['port '+str(num)] = vlan
                num += 1
            else:
                num +=1       
        ##формирует tagged словарь##
        num2 = 1    
        for element in bin_tag:
            if element is '1':
                (taggedvlan['port '+str(num2)]).append(vlan)
                num2 += 1
            else:
                num2 +=1
    itemlist = []    
    for key in taggedvlan.keys():
        itemlist = taggedvlan[key]
        for num in range(0,(len(itemlist))):
            i = 0
            if (int(itemlist[num])+1) ==  int(itemlist[num+1]):
                while num+i+1<(len(itemlist)-1) and (int(itemlist[num+i])+1) == int(itemlist[num+i+1]) :
                    itemlist.pop(num+i) 
                    i += 1
                    
                else:
                    second = int(itemlist[num+i])
                    print(second)
            else:
                pass
#        print(itemlist)
#        print(taggedvlan[key])

    return(untaggedvlan,taggedvlan)
     ##################




    