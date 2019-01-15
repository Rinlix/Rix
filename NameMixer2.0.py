#NameMixer.py

import random
import time
while True:
    true = True
    def rigged():
        print('DToo much cringe and toxic, cannot survive...')
        true = False
    names = []
    while true:
        name = input('Enter A Name: [q] to randomize all names ')
        if name == 'q':
            num = len(names)
            true = False
        elif name == 'DonaldTrump':
            rigged()
        else:
            names.append(name)

    for a in range(num):
        output = random.choice(names)
        names.remove(output)
        ordinal = a + 1
        if ordinal == 1:
            ordinal1 = '1st'
        elif ordinal == 2:
            ordinal1 = '2nd'
        elif ordinal == 3:
            ordinal1 = '3rd'
        else:
            ordinal = str(ordinal)
            ordinal1 = (ordinal + 'th')
        for i in range(6):
            time.sleep(0.001)
            print('=', end='')
        print('', end='\n')
        print('')
        print(ordinal1,'is', ': ', output)
        print('')
