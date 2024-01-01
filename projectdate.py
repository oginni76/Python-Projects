#You need to pair your colleagues or friends for a task
#A random date shuffler for a group of friends
#Or a random way to pair your friends for a project
#Then this program is for youu

import random

#Number of pairs you want
num = int(input('Enter number of dates: '))

#list where user inputs would be stored
list_boys =[]
list_girls =[]

for i in range(num):
    #takes in user input
    boys = input('Enter name of boy: ')
    girls = input('Enter name of girl: ')

    #Adds user input to the list declared
    list_boys.append(boys)
    list_girls.append(girls)

#Shuffles the list where the user_input is stored
random.shuffle(list_boys)
random.shuffle(list_girls)

#declaring new list to store the random pairs for output
pairs_list=[]


for i in range(num):
    #Adds the new pairs of both lists to the new lists
    pairs_list.append((list_boys[i], list_girls[i]))

#I used this while testing, IGNORE
#print(list_boys)
#print(list_girls)

#Prints the new list of random pairs    
print(f'Here, have your random selection: {pairs_list}')






