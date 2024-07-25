# Moon Phas – Functions

'''
Why are there so many Moon emojis? Each one represents a different Moon phase, the shape of the Moon's sunlit portion as viewed from the Earth.

Write a moon_phase() function that takes in a phase parameter of the moon phase name given below and returns the correct moon emoji for it:

New Moon → 🌑
Waxing Crescent → 🌒
First Quarter → 🌓
Waxing Gibbous → 🌔
Full Moon → 🌕
Waning Gibbous → 🌖
Last Quarter → 🌗
Waning Crescent → 🌘

# Output: 🌑
'''

def moon_phase(phase):
    if phase == 'New Moon':
        return '🌑'
    elif phase == 'Waxing Crescent':
        return '🌒'
    elif phase == 'First Quarter':
        return '🌓'
    elif phase == 'Waxing Gibbous':
        return '🌔'
    elif phase == 'Full Moon':
        return '🌕'
    elif phase == 'Waning Gibbous':
        return '🌖'
    elif phase == 'Last Quarter':
        return '🌗'
    elif phase == 'Waning Crescent':
        return '🌘'
    else:
        return 'Invalid Moon Phase'

answer = moon_phase('New Moon')
print(answer)      

