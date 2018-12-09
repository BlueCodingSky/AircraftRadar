from tkinter import *
import queue
import threading
import math

class RadarView(Frame):

    def __init__(self, parent, q, controller):
        super(RadarView, self).__init__(parent)
        parent.protocol("WM_DELETE_WINDOW", self.exitAction)
        self.parent = parent
        self.q = q
        self.controller = controller
        self.screen_width = 480
        self.screen_height = 800
        self.canvas = Canvas(parent, width=self.screen_width, height=self.screen_height,bg='black')
        self.canvas.pack()
        self.drawBackground(self.screen_width)
        self.read_queue()

    def exitAction(self):
        self.controller.stop()
        self.parent.destroy()

    def drawBackground(self, screen_width):
        width = 30
        r1 = width

        while r1 < screen_width/2:
            oval = self.canvas.create_oval(r1, r1, screen_width-r1, screen_width-r1, fill='gray10', outline='gray20')
            r1 = r1 + 30

        line_v = self.canvas.create_line(screen_width / 2, width, screen_width / 2, screen_width - width, width=1, fill='gray20')
        line_h = self.canvas.create_line(  width, screen_width / 2, screen_width - width, screen_width / 2, width=1, fill='gray20')
        line_l = self.canvas.create_line(92, 92, screen_width - 92, screen_width -92, width=1, fill='gray20')
        line_r = self.canvas.create_line(screen_width - 92, 92, 92, screen_width -92, width=1, fill='gray20')

    def read_queue(self):
        try:
            self.process(self.q.get(False))
        except queue.Empty:
            print("keine Daten")
        self.after(100, self.read_queue)
           
    def process(self,item):
        #self.circle(240, 240, 5)
        for x in item:
            self.drawAircraft(x)

    def drawAircraft(self, aircraft):
        if aircraft.distance < 7000 :
            print('distance: ' + str(aircraft.distance) + ' Bearing: ' + str(aircraft.bearing))
            radius = aircraft.distance * 210 / 7000
            x = radius * math.cos(aircraft.bearing) + 240
            y = radius * math.sin(aircraft.bearing) + 240
            self.circle(x, y, 5)

    def circle(self, x, y, r):
        id = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill='sea green')
        return id