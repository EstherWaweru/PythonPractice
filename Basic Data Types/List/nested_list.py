
if __name__ == '__main__':
    name_list=[]
    score_list=[]
    range_list=int(input())
    for _ in range(range_list):
        name = input()
        score = float(input())
        score_list.append(name)
        score_list.append(score)
    #create a nested list 
arr= [score_list[i:i+2] for i in range(0, len(score_list), 2)]  
#sort with respect to marks then by names
arr.sort(key=lambda x: (x[1],x[0]))
#extract name and marks
names = [i[0] for i in arr]
marks = [i[1] for i in arr]
min_val=min(marks)
#remove the minimum values
while marks[0]==min_val:
    marks.remove(marks[0])
    names.remove(names[0])
#print the second lowest grade
for x in range(0,len(marks)):
    if marks[x]==min(marks):
        print(names[x])


         

    
        
        
