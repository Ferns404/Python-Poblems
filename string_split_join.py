def split_and_join(line):
    line=line.split(" ") #to split
    line="-".join(line) #to join
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)