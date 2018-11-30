import json
import queue
from aircraftParser import *
from tkinter import *
from radarview import RadarView
from aircraftRadarController import *

def main():
    root = Tk()
    controller = AircraftRadarController(root)
    controller.showAircraftRadar()
    root.mainloop()
    
if __name__ == "__main__":
    main()