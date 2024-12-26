print("Finonacci Program.")
print("----------------------------------")

length= int(input("Enter the length of numbre:"))
x=0
y=1
iteration=0

if length<=0:
	print("Enter a grater than zero number.")
elif length==1:
    print(x)
else:
    print("The Finonacci Sequance has {} elements".format(length),":")

while (iteration<length):
	print(x,end=',')
	z=x+y
	x=y
	y=z
	iteration+=1
