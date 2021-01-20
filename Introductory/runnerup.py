if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    
    # arr.sort()
    new_lst=sorted(set(arr))
    
    print(new_lst[-2])
    