#Create a text file named number.txt
    #Add 20 integers in the text file

#Create a code that will create a text file named even.txt and will have the even integers from number.txt
with open("number.txt", "r") as numbers:
    try:
        integers = [int(line.strip()) for line in numbers]

        even_integers = [num for num in integers if num % 2 == 0]

        with open("even.txt", "w") as even:
            for num in even_integers:
                even.write(f"{num}\n")
        print("Even integers have been sorted out to the created file (even.txt)")

    except ValueError:
        print("An Invalid Integer found in number.txt")



#Create a code that will create a text file name odd.txt and will have the odd integers from number.txt

