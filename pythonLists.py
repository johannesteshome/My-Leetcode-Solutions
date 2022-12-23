if __name__ == '__main__':
    N = int(input())
    
    # print(N)
    
    commands = []
    for i in range(N):
       commands.append(input())
    #    print(commands[i])
       
    myList = []
       
    for i in range(len(commands)):
        if(commands[i].split()[0] == 'insert'):
            myList.insert(int(commands[i].split()[1]), int(commands[i].split()[2]))
        elif(commands[i].split()[0] == 'print'):
            print(myList)
        elif(commands[i].split()[0] == 'remove'):
            myList.remove(int(commands[i].split()[1]))
        elif(commands[i].split()[0] == 'append'):
            myList.append(int(commands[i].split()[1]))
        elif(commands[i].split()[0] == 'pop'):
            myList.pop()
        elif(commands[i].split()[0] == 'sort'):
            myList.sort()
        elif(commands[i].split()[0] == 'reverse'):
            myList.reverse()
