# Planet Weights – Control Flow

'''
    The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

    Create a weight conversion program that:

    Asks the user what their Earth weight is (as a float).
    Asks the user for a planet number (as an int).
    Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

    To calculate the user's weight:

    destination weight = Earth weight × relative gravity
    Number	Planet	Relative Gravity
    1	Mercury	0.38
    2	Venus	0.91
    3	Mars	0.38
    4	Jupiter	2.53
    5	Saturn	1.07
    6	Uranus	0.89
    7	Neptune	1.14
    If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.
'''
# Codedex Version

earth_weight = float(input("What is your Earth weight? "))

planet = int(input("Enter a planet number: "))

if planet == 1:
    destination_weight = earth_weight * 0.38
    print(f'Weight on Mercury: {destination_weight}')
elif plannet == 2:
    destination_weight = earth_weight * 0.91
    print(f'Weight on Venus: {destination_weight}')
elif planet == 3:
    destination_weight = earth_weight * 0.38
    print(f'Weight on Mars: {destination_weight}')
elif planet == 4:
    destination_weight = earth_weight * 2.53
    print(f'Weight on Jupiter: {destination_weight}')
elif planet == 5:
    destination_weight = earth_weight * 1.07
    print(f'Weight on Saturn: {destination_weight}')
elif planet == 6:
    destination_weight = earth_weight * 0.89
    print(f'Weight on Uranus: {destination_weight}')
elif planet == 7:
    destination_weight = earth_weight * 1.14
    print(f'Weight on Neptune: {destination_weight}')
else:
    print('Invalid planet number.')