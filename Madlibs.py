"""
This program generates passages that are generated in mad-lib format
Author: Den
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print ("The madlibs game has started!")


name = input("Enter a name: ")



print ("Please input 3 adjectives: ")

adj1 = input("Enter first adjective: ")
adj2 = input("Enter second adjective: ")
adj3 = input("Enter third adjective: ")



print ("Please input a verb: ")

verb1 = input("Enter a verb: ")


print ("Please input a couple of nouns: ")

noun1 = input("Enter first noun: ")

noun2 = input("Enter second noun: ")


animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")


print (STORY % (name, adj1, adj2, animal, food, verb1, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))