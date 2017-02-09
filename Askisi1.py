sentence = raw_input("Please enter your sentence: ")

length = len(sentence)
last= sentence[length-1]

chars = []
for line in sentence:
    chars.extend(line)

space = [' ',' ']

chars.extend(space)



if (last == "!"):
 check=1
else:
 check=0




for counter in range(0, length):
    

    if ( 
           (
             chars[counter] == "!" and chars[counter+1] == "." 
           )
           
           or (
                chars[counter] == "!" and chars[counter+1].isupper() == True 
                
              )

           or (
                chars[counter] == "!" and chars[counter+2].isupper() == True and chars[counter+1] == " "
                
              )
        ):

    	    chars[counter] = "!"
            

    elif ( chars[counter] == "!" ): 

    	    chars[counter] = ""



chars = chars[0:length-1]
new_sentence = ''.join(chars)


if (check==1):
	print "The new sentence without the Exclamation marks (!) is:"
	print new_sentence+"!"
else:
	print "The new sentence without the Exclamation marks (!) is:"
	print new_sentence


