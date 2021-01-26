#tuples are used in swapping a,b=b,a  also used for keys in dictionaries

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
