import textwrap

def wrap(string, max_width):
    newString = ""
    for i in range(len(string)):
        # print("sth")
        if((i+1) % max_width == 0):
            newString += string[i]
            newString += '\n'
            # print(newString)
        else:
            newString += string[i]
    
    return newString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
