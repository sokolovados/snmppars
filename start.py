def start():
   # Model = input('Какой шаблон использовать(28,52): ')
    print("Ip заменяемых коммутаторов. Ctrl-D  to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    #Community= input('SNMP Community: ')
    #Location = input('Регион: ')
    return(contents)

