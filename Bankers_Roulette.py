#import random module
import random
#get user input for names of the group
names_string = input("Give me everybody's names, separated by a comma. ")
#split the string into individual names, for individual list items
names = names_string.split(", ")
#get the number of list items after being split
num_items = (len(names))
#select a random name by the number of the list item
random_choice = random.randint(0, num_items - 1)
#print the random choice / name
print(random_choice)
#define variable of the person who will pay 
person_who_will_pay = names[random_choice]
#print the newly defined variable, confirming the indivdual responsible for the entire bill
print(person_who_will_pay + " is going to buy the meal today")
