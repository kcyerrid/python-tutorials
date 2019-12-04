#Gather the information from the user and format into an expected value.
print('What is your name?')
name = str(input())
print('How old are you?')
age = int(input())

#If the person is Alice, print her name; otherwise print the inputted name (bad code design)
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hi, ' + name + '!')
    
#Test for age appropriateness and print as appropriate.
if age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, Grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
