
#For square of the even integers
#create a function
def source_file(file_name):
    # create a code that will open source file of 20 integers
    with open("number.txt", "r") as file:
        #source file used was the number.txt that is used in File_Handling
        try:
            integers = [int(line.strip()) for line in file]

            even_integers = [num for num in integers if num % 2 == 0]
            # create a code that will Find the square of the even integers in the source file
            even_squared = [num * num for num in even_integers]

            with open("Double.txt", "w") as even:
                for num in even_squared:
                    even.write(f"{num}\n")
            print("Even integers have been sorted out to the created file (Double.txt)")

        except ValueError:
            print("An Invalid Integer found in number.txt")
#store the output in double.txt
source_file("Double.txt")

#For cube of the odd integers

#create a code that will create a file for the cube of the odd integers in triple.txt
def source_file_2(file_name_2):
    #opening the source file
    with open("number.txt", "r") as file_2:
        #for identifying the even integers
        try:
            integers = [int(line.strip()) for line in file_2]
            odd_integers = [num for num in integers if num % 2 != 0]
            # create a code that will find the cube of the integers
            odd_cube = [num**3 for num in odd_integers]

            print(odd_cube)
        except ValueError:
            print("An Invalid")


source_file_2("Triple.txt")
#create a code that will find the cube of the integers
#store the output in triple.txt
