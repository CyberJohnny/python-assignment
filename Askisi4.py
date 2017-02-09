

my_inputlist = raw_input("Please enter your list and seperate the objects with a comma (,) ( example: 19,2,8,53,100 ): ")

mylist = my_inputlist.split(",")

length = len(mylist)

 
mylist.remove(max(mylist))
mylist.remove(max(mylist))
mylist.remove(min(mylist))
mylist.remove(min(mylist))


N = len(mylist)


results = map(int, mylist)

x = 0.0

    
for counter in range(0, N):
 x = x + results[counter]


Average = x/N


end = [i for i in range(N)]



for counter in range(0, N):
 end[counter]= (results[counter]*1.0 - Average)**2



SUM=0.0
for counter in range(0, N):
 SUM= SUM + end[counter]


x=(SUM/N)

print "The result is:" , x**(0.5)






