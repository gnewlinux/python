import simplegui

def time_handler():
    print('ola')

timer = simplegui.create_timer(500,time_handler)
timer.start()
