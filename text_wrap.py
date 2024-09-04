import textwrap

def wrap(string, max_width):
    s_wrap= textwrap.wrap(string,max_width)   #FUNCTION TO WRAP TEXT
    return '\n'.join(s_wrap)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)