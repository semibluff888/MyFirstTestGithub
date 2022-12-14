import time
import ghub_mouse as ghub
import random

import pynput


mouse = pynput.mouse.Controller()
# Read pointer position
print('The current pointer position is {0}'.format(mouse.position))


a = random.random()
print(a)

print(random.random())
print(random.random())


t0 = time.time()

for _ in range(10):

    ghub.mouse_xy(int(20*random.random()), int(20*random.random()))
    # time.sleep(0.001)

print('total time costs:', (time.time() - t0))

print('The current pointer position is {0}'.format(mouse.position))
