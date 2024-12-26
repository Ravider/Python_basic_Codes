
#*args and *kwargsd

print("--------------------*args----------------------------")
def sum(a,*numbers):
    print(numbers)
    print(a)
    sum=0
    for i in numbers:
        sum +=i
    print("Sum is:",sum)

print("--------------------**kwargs----------------------------")
sum(1,2,3)
sum(1,2,3,4,5)
sum(1,2,3,4,5,6,7)

def details(*detail,**info):
    for key,value in info.items():
        print(key,value)
    print(detail)
    
details(1,2,Name="Vijay", Age=20, Department="CE")
details(1,2,3,Name="Jay", Age=50, Collage="Atmiya", Department="IT")