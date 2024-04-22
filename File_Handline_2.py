#Create a txt file with lists of 20 students with GWA


#Create a code that will open the txt file
# Read the file
with open('GWA.txt', 'r') as gwa_file:
    students = {}
    for line in gwa_file:
        name, gwa = line.strip().split(' - GWA: ')
        students[name] = float(gwa)
        print(name)
        print(gwa)

#Create a code that will seperate name and gwa

#Create a code that will arrange the names and GWA from highest to lowest

#Print the output