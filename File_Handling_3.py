


#create a function
def creating_file(file_name):
#create a code to open filename
    with open(file_name, 'w') as file:
#Ask user to enter a line of text
        while True:
            text_line=input("Enter line")
            file.write(text_line)
#Ask user if he/she will input more line of text
#call the function to put it in a file