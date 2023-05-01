import tkinter
import random
import time
import math

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
#SCALE = 2
SNOW_SIZE = 2

snow = []

window = tkinter.Tk()
window.title('snow.py')

canvas = tkinter.Canvas(window, bg='black', width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

snow.append([50, 0])

canvas.pack()

running = True
while running:
    canvas.delete('all')

    for i in range(len(snow)-1):
        if snow[i][1] < WINDOW_HEIGHT-3:
            snow[i][0] += random.randint(-5, 5)*math.pi
            snow[i][1] += 10 + random.randint(0, 3)*math.pi
        else:
            new_snow = []
            for j in range(len(snow)):
                new_snow.append(snow[j])
                if j == i and i+1 <= len(snow):
                    snow[j] = snow[i+1]

        canvas.create_oval(snow[i][0]-SNOW_SIZE, snow[i][1]-SNOW_SIZE, snow[i][0]+SNOW_SIZE, snow[i][1]+SNOW_SIZE, outline='white', fill='white')

    snow.append([random.randint(0, WINDOW_WIDTH), 0])

    canvas.update()
    time.sleep(0.1)

window.mainloop()
