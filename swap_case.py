def swap_case(s):
    swap=s.swapcase() #function to swap
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)