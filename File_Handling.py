#Create a text file named number.txt
    #Add 20 integers in the text file

#Create a code that will create a text file named even.txt and will have the even integers from number.txt
with open("number.txt", "r") as numbers:
    for integers in numbers:
        integers= integers.strip()
        print(integers)



#Create a code that will create a text file name odd.txt and will have the odd integers from number.txt

