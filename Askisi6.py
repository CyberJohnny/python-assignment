import urllib2
import json

my_input = raw_input("Please give the numbers !(7-digit numbers only)! you want to check seperated by comma (,) ( example: 1234567,7654321,1122334 ):")
my_input = my_input.split(",")
length = len(my_input)
my_numbers = [i for i in range(length)]

for i in range(0,length):

   my_numbers[i] = map(int,str(my_input[i]))


response = urllib2.urlopen('http://applications.opap.gr/DrawsRestServices/proto/last.json')

html = response.read()
last_draw_No=json.loads(html)["draw"]["drawNo"]


all_numbers = [i for i in range(8)]


for counter in range(0, 8):

    x = urllib2.urlopen('http://applications.opap.gr/DrawsRestServices/proto/%s.json'%(last_draw_No - counter))
    draw_numbers=json.loads(x.read())["draw"]["results"]  
    all_numbers[counter]=draw_numbers
 

Wins=0

c1=0
c2=0
c3=0
c4=0
c5=0
c6=0

money=0

for i in range(0,length):

  for j in range(0,8):
      

      if  ( 
            
              my_numbers[i][0] == all_numbers[j][0] and my_numbers[i][1] == all_numbers[j][1] and 
              my_numbers[i][2] == all_numbers[j][2] and my_numbers[i][3] == all_numbers[j][3] and 
            my_numbers[i][4] == all_numbers[j][4] and my_numbers[i][5] == all_numbers[j][5] and 
              my_numbers[i][6] == all_numbers[j][6]
             
            ):

              Wins=Wins+1
              c1=c1+1
              money=money-1
              



      elif ( 
            (
              my_numbers[i][0] == all_numbers[j][0] and my_numbers[i][1] == all_numbers[j][1] and 
              my_numbers[i][2] == all_numbers[j][2] and my_numbers[i][3] == all_numbers[j][3] and 
            my_numbers[i][4] == all_numbers[j][4] and my_numbers[i][5] == all_numbers[j][5]
             )
             or (
                  my_numbers[i][6] == all_numbers[j][6] and my_numbers[i][5] == all_numbers[j][5] and 
                  my_numbers[i][4] == all_numbers[j][4] and my_numbers[i][3] == all_numbers[j][3] and 
                my_numbers[i][2] == all_numbers[j][2] and my_numbers[i][1] == all_numbers[j][1]  
                 )
            ):

              Wins=Wins+1
              c2=c2+1
              money=money+25000
              



      elif ( 
            (
              my_numbers[i][0] == all_numbers[j][0] and my_numbers[i][1] == all_numbers[j][1] and 
              my_numbers[i][2] == all_numbers[j][2] and my_numbers[i][3] == all_numbers[j][3] and 
            my_numbers[i][4] == all_numbers[j][4] 
             )
             or (
                  my_numbers[i][6] == all_numbers[j][6] and my_numbers[i][5] == all_numbers[j][5] and 
                  my_numbers[i][4] == all_numbers[j][4] and my_numbers[i][3] == all_numbers[j][3] and 
                my_numbers[i][2] == all_numbers[j][2]  
                 )
            ):

              Wins=Wins+1
              c3=c3+1
              money=money+2500
              



      elif ( 
            (
              my_numbers[i][0] == all_numbers[j][0] and my_numbers[i][1] == all_numbers[j][1] and 
              my_numbers[i][2] == all_numbers[j][2] and my_numbers[i][3] == all_numbers[j][3] 
             )
             or (
                  my_numbers[i][6] == all_numbers[j][6] and my_numbers[i][5] == all_numbers[j][5] and 
                  my_numbers[i][4] == all_numbers[j][4] and my_numbers[i][3] == all_numbers[j][3] 
               )
            ):

              Wins=Wins+1
              c4=c4+1
              money=money+250
              
               


      elif ( 
            (
              my_numbers[i][0] == all_numbers[j][0] and my_numbers[i][1] == all_numbers[j][1] and 
              my_numbers[i][2] == all_numbers[j][2]  
             )
             or (
                  my_numbers[i][6] == all_numbers[j][6] and my_numbers[i][5] == all_numbers[j][5] and 
                  my_numbers[i][4] == all_numbers[j][4] 
               )
            ):

              Wins=Wins+1
              c5=c5+1
              money=money+25
              



      elif ( 
            (
              my_numbers[i][0] == all_numbers[j][0] and my_numbers[i][1] == all_numbers[j][1] 
             )
             or (
                  my_numbers[i][6] == all_numbers[j][6] and my_numbers[i][5] == all_numbers[j][5] 
               )
            ):

              Wins=Wins+1
              c6=c6+1
              money=money+2
              



print " You won",Wins,"times!"

print " Wins in 1st category:",c1
print " Wins in 2nd category:",c2
print " Wins in 3rd category:",c3
print " Wins in 4th category:",c4
print " Wins in 5th category:",c5
print " Wins in 6th category:",c6

if (money <= -1 ):
  print " TZAK-POT!!! :)"
else:
  print " Total amount earned:",money,"EUR"

