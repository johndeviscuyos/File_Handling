import pyttsx3
text_speech = pyttsx3.init()
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
        speak_even_integers=("Even integers have been sorted out to the created file (even.txt)")
        text_speech.say(speak_even_integers)
        text_speech.runAndWait()
        print(speak_even_integers)
    except ValueError:
        Invalid=("An Invalid Integer found in number.txt")
        text_speech.say(Invalid)
        text_speech.runAndWait()



#Create a code that will create a text file name odd.txt and will have the odd integers from number.txt

with open("number.txt", "r") as numbers:
    try:
        integers = [int(line.strip()) for line in numbers]

        odd_integers = [num for num in integers if num % 2 != 0]

        with open("odd.txt", "w") as odd:
            for num in odd_integers:
                odd.write(f"{num}\n")
        speak_odd_integers=("Odd integers have been sorted out to the created file (odd.txt)")
        text_speech.say(speak_odd_integers)
        text_speech.runAndWait()
        print(speak_odd_integers)

    except ValueError:
        invalid=("An Invalid Integer found in number.txt")
        text_speech.say(invalid)
        text_speech.runAndWait()
