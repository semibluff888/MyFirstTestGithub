"""
官网代码：监听鼠标
https://pypi.org/project/pynput/

"""
from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# 方法一：阻塞版！
# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()  # 等待直到该线程结束(比如，上面的方法return false)

# 方法二：非阻塞版！
# ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()

"""
When using the non-blocking version above, the current thread will continue executing. This might be necessary 
when integrating with other GUI frameworks that incorporate a main-loop, but when run from a script, this will 
cause the program to terminate immediately.
"""