import pyttsx3
text_speech=pyttsx3.init()


#create a function
def creating_file(file_name):
#create a code to open filename
    with open(file_name, 'w') as file:
#Ask user to enter a line of text
        while True:
            text_line=input("Enter line: ")
            file.write(text_line + "\n")

            text_speech.say(text_line)
            text_speech.runAndWait()

#Ask user if he/she will input more line of text
            add_lines = input("Are there more lines? y/n: ")
            if add_lines.lower() != 'y':
                break

    line_speech=("Thank you for writing your lines")
    text_speech.say(line_speech)
    text_speech.runAndWait()
    print("Thank you for writing your lines")
#call the function to put it in a file
creating_file('mylife.txt')
