# Sum or Squares - Loops

number = int(input('Enter a number: '))
total = 0

for i in range(number + 1):
    square = i ** 2
    total = total + square
    print(f'{i}^2 = {square}')
    print(f'Total: {total}')