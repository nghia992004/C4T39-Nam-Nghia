import pyglet
import datetime
x = True
music = pyglet.resource.media('Alarm.wav')
while x:
    time = datetime.datetime.now()
    if time.minute == 20:
        music.play()
        x = False
pyglet.app.run()