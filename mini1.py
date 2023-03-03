

def templ_1():
   number1=input("input a number/measure of time:")
   transport=input("input a Mode of Transportation:")
   adj1=input("input an adjective:")
   adj2=input("input an adjective:")
   noun=input("input a noun:")
   color=input("input a color:")
   body_part=input("input a part of the body:")
   verb=input("input a verb:")
   number2=input("input a number:")
   noun2=input("input a noun:")
   noun3=input("input a noun:")
   body_part2=input("input a part of the body:")
   noun4=input("input a noun:")
   adj3=input("input an adjective:")
   silly=input("input a silly word:")

  
   print(
   f" It was about {number1} ago when I arrived at the hospital in a {transport}.\
     The hospital is a/an {adj1} place there are a lot of {adj2} {noun} here.\
     There are nurses here who have {color} {body_part}. If someone wants to come\
     into my room I told them that they have to {verb} first. I’ve decorated my room \
     with {number2}{noun2}. Today I talked to a doctor and they were wearing a {noun3} on\
      their {body_part2}. I heard that all doctors {verb} {noun4} every day for breakfast. \
     The most{adj3}thing about being in the hospital is the {silly} {noun} !")


def templ_2():
   person_name=input("input a Proper Noun (Person’s Name):")
   noun=input("input a noun:")
   adj=input("input an adjective(feeling):")
   verb=input("input a verb:")
   adj2=input("input an adjective(feeling):")
   animal=input("input an animal")
   verb2=input("input a verb:")
   color=input("input a color:")
   verb3=input("input a verb(ending in ing):")
   adverb=input("input an adverb ending in ly):")
   number=input("input a number:")
   mtime=input("input a measure of time:")
   silly=input("input a silly word:")
   noun2=input("input a noun:")
 
  
   print(
   f" This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag,\
     and {noun}. I am so {adj} to {verb} in a tent. I am {adj2} we might see a(n)\
     {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I\
     ihave heard that the {color} lake is great for {verb3}. Then we will {adverb} hike\
     through the forest for {number}{mtime}. If I see a {color} {animal} while hiking, I am going to bring\
      it home as a pet! At night we will tell {number} {silly} stories and roast{noun2} around the campfire!!")



def templ_3():
    person_name=input("input a person's name:")
    adjective=input("input an adjective:")
    color=input("input a color:")
    animal=input("input an animal:")
    place=input("input a place:")
    adjective2=input("input an adjective:")
    magical_creature=input("input a magical creature:")
    adjective3=input("input an adjective:")
    magical_creature2=input("input a magical creature:")
    room=input("input a room:")
    noun=input("input a noun:")
    noun2=input("input a noun:")
    noun3=input("input a noun:")
    adjective4=input("input an adjective:")
    noun4=input("input a noun:")
    number=input("inout a number:")
    measure_of_time=input("input measure of time:")
    verb=input("input a verb(ending in ing):")
    adjective5=input("input an adjective:")
    noun5=input("input a noun:")
   
    print(f"Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest.\
    I found myself here one day after going for a ride on a {color} {animal} in {place}.\
    There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here!\
    In the {room} there is a pool full of {noun}.\
    I fall asleep each night on a {noun2} of {noun3} and dream of {adjective4} {noun4}.\
    It feels as though I have lived here for {number} {measure_of_time}.\
    I hope one day you can visit, although the only way to get here now is {verb} on a {adjective5} {noun5}!!")
   


import random  
num = random.randint(1, 3)  
print(num)

if num==1:
   templ_1()
elif num==2:
   templ_2()   
elif num==3:
   templ_3()
   