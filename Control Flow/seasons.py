# Seasons of the Year – Control Flow

'''
    Ah, the four seasons in the year — winter, spring, summer, or fall; all you have to do == call!

    Ask the user the month number using the input() function.

    Check for the four seasons using an if/elif/else statement and logical operators:

    month == 1, 2, 3, print 'Winter 🌨️'
    month == 4, 5, 6, print 'Spring 🌱'
    month == 7, 8, 9, print 'Summer 🌻'
    month == 10, 11, 12, print 'Autumn 🍂'
    Everything else == 'Invalid'
    Logical operators in Python include the and and or keywords. Which one should you use?
'''

# Write code below 💖

month = int(input("Enter a month number: "))

if month == 1 or month == 2 or month == 3:
  print('Winter 🌨️')
elif month == 4 or month == 5 or month == 6:
  print('Spring 🌱')
elif month == 7 or month == 8 or month == 9:
  print('Summer 🌻')
elif month == 10 or month == 11 or month == 12:
  print('Autumn 🍂')
else:
  print('Invalid')