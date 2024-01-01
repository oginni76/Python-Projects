#22/12/23
#This program stores user inputed names in a list and sorts them alphabetically



#Accepts user input of how many names to be stored
number_of_names = int(input('Enter no of total names to input: '))

#Declaration of empty list to store each name after each iteration
allnames_list = []


#Loop to request user input, range is dependent on how many names user wishes to store
for i in range(number_of_names):   
    #Accepts user input
    firstname = input('Enter first name: ').capitalize() #.capitalize changes first letter in word to Caps
    lastname = input('Enter last name: ').capitalize()
    
    print(f'Stored') #Just to alert user that name has beeen saved
    fullname = f"{firstname} {lastname}"  #f string that joins(concatenates) firstname and lastname together into new variable fullname

    #adds each fullname to already declared list
    allnames_list.append(fullname)


#sorts out the list alphabetically 
allnames_list.sort()

#prints the output
print(allnames_list)


#Challenges
#1. List was storing only the name of the last loop

# I was able to solve that by checking help from chatgpt
# i just had to simply use the append method to add every outcome to the list aftr each iteration.

#2. Making the letter of the firstname capital

# I forgot to add () to the .upper method. Very silly mistake
# well it didn't work instead firstname was returning only the first capital letter of the user's input'

# I later solved this by using .capitalize() as that is it's specific function
#.upper makes the whole word in caps while .title()- makes the first letter of every word present in capital

#3. Arranging alphabetically by first name
# I actually thought this would be an issue but i was surprised python already had a .sort method for that
# .sort() - sorts the list while .sorted()- sorts the list but in a new list
