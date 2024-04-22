import pyttsx3
text_speech = pyttsx3.init()
#Create a txt file with lists of 20 students with GWA



#Create a code that will open the txt file
# Read the file
with open('GWA.txt', 'r') as gwa_file:
    students = {}
    for line in gwa_file:
        # Create a code that will seperate name and gwa
        name, gwa = line.strip().split(' - GWA: ')
        students[name] = float(gwa)

#Create a code that will arrange the names and GWA from highest to lowest
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

#Print the output
for name, gwa in sorted_students:
    print(f"{name} - GWA: {gwa}")

    text_speech.say(f"{name} has a GWA of {gwa}")
    text_speech.runAndWait()



