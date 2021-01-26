if __name__ == '__main__':
    N = int(input())
    arr=[]
    for commands in range(N):
        command=input().split()
        # Inserts element x at position i. 
        if command[0]=='insert':
            arr.insert(int(command[1]),int(command[2]))
        elif command[0]=='print':
            print(arr)
            # Adds a single element x to the end of a list.
        elif command[0]=='append':
            arr.append(int(command[1]))
        # Sorts the list. 
        elif command[0]=='sort':
            arr.sort()
        # Removes the last element of a list. If an argument is passed, that index item is popped out.
        elif command[0]=='pop':
            arr.pop()
        # Reverses the list. 
        elif command[0]=='reverse':
            arr.reverse()
        # Removes the first occurrence of element x.
        elif command[0]=='remove':
            arr.remove(int(command[1]))
       
        
