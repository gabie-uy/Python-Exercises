# Planet Weights – Control Flow v2

earth_weight = float(input("What is your Earth weight? "))

print('''
    1. Mercury
    2. Venus
    3. Mars
    4. Jupiter
    5. Saturn
    6. Uranus
    7. Neptune
''')

planet = int(input("Enter a planet number: "))

if planet == 1:
    print(f'Weight on Mercury: {earth_weight * 0.38}')
elif planet == 2:
  print(f'Weight on Venus: {earth * 0.91}')
elif planet == 3:
  print(f'Weight on Mars: {earth * 0.38}')
elif planet == 4:
  print(f'Weight on Jupiter: {earth * 2.53}')
elif planet == 5:
  print(f'Weight on Saturn: {earth * 1.07}')
elif planet == 6:
  print(f'Weight on Uranus: {earth * 0.89}')
elif planet == 7:
  print(f'Weight on Neptune: {earth * 1.14}')
else:
  print('Invalid planet number.')