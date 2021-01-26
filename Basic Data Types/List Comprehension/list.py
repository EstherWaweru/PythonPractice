if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    new_list=[]
    lst=[]
    # for a in range(x+1):
    #     for b in range(y+1):
    #         for c in range(z+1):
    #             if a+b+c!=n:
    #                 new_list.extend([a,b,c])
    # lst.append(new_list)
    # print(lst)
    new_arr=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n ]
    print(new_arr)
                    