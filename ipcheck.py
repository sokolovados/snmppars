import ipaddress as ip


def net_details(net_details):
    """
    net_details ожидает на входит строку формата "ip/prefix"


    На выходе в словарь enviroment добавляется словарь net_details c полями:
    examples:
    net_details_ip_prefix = 10.10.1.10/24
    net_details_net = 10.10.1.0/24
    net_details_ip = 10.10.1.10
    net_details_ip_with_netmask = 10.10.1.10/255.255.255.0
    net_details_netmask = 255.255.255.0
    net_details_reverse_mask = 0.0.0.255
    net_details_arpa = 10.1.10.10.in-addr.arpa
    net_details_arpa_for_bind = 10.1.10.10.in-addr.arpa. IN PTR sw1
    net_details_def_gateway = 10.10.1.1

    """
    net_details = ip.ip_interface(net_details)
    net_details_ip_prefix = net_details.compressed
    net_details_net = net_details.network.compressed
    net_details_ip = net_details.ip.compressed
    net_details_ip_with_netmask = net_details.with_netmask
    net_details_netmask = net_details.netmask.compressed
    net_details_reverse_mask = net_details.hostmask.compressed
    net_details_arpa = net_details.ip.reverse_pointer
    net_details_def_gateway= (list(ip.ip_network(net_details_net).hosts())[0])
    
    return(net_details_ip,net_details_netmask,net_details_def_gateway)

