def swap_case(s):
    new_s=''
    for i in range(len(s)):
        if s[i].isupper():
            new_s+=s[i].lower()
        elif s[i].islower():
            new_s+=s[i].upper()
        else:
            new_s+=s[i]
    #s.swapcase()
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)