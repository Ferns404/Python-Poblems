def count_substring(string, sub_string):
    count=0
    slen=len(sub_string)
    for i in range(len(string)-slen + 1):    #for loop to traverse string
        if string[i:i+slen]==sub_string:     #to count
            count+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)