

#create a function
def source_file(file_name):
    # create a code that will open source file of 20 integers
    with open("number.txt", "r") as file:
        #source file used was the number.txt that is used in File_Handling
        try:
            integers = [int(line.strip()) for line in file]

            even_integers = [num for num in integers if num % 2 == 0]

            print(even_integers)
        except ValueError:
            print("Invalid")

source_file("Double.txt")
#create a code that will Find the square of the even integers in the source file
#store the output in double.txt

#create a code that will create a file for the cube of the odd integers in double.txt
#create a code that will find the cube of the integers
#store the output in triple.txt
