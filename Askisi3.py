

my_inputlist = raw_input("Please enter your list and seperate the objects with a comma (,) ( example: 1,a,2,b ): ")

mylist = my_inputlist.split(",")
length = len(mylist)


x=0
new = [i for i in range(length)]

for counter in range(0, length):
    if (mylist[counter] != "0"):
    	new[x] = mylist[counter]
    	x=x+1




for counter in range(x, length):
 new[counter] = '0'   	


print new
