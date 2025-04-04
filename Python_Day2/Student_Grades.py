avg_dic={}
def student():
    No_Of_Students=int(input("Enter No of Students"))
    No_Of_Subjects=int(input("Enter No of Subjects"))
    dic={}
    for name in range(0, No_Of_Students):
        summ=0
        avg=0
        avg_dic['name']=dic['name']=input("Enter student name")
        for marks in range(0, No_Of_Subjects):
            dic["marks"]=input("Enter Student marks")
        summ=sum(dic[marks])
        avg=float(summ/No_Of_Subjects)
        avg_dic['marks']=avg

def choice(avg_dic):
    given=input("Enter the name of the student you want to know avg marks")
    for i in avg_dic:
        if (given==i):
            print(i)

student()
choice(avg_dic)