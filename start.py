def start():
   # Model = input('Какой шаблон использовать(28,52): ')
    print("Ip заменяемых коммутаторов в формате (X.X.X.X/X). Ctrl-D для сохранения ввода .")
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

