import json
import queue
from tkinter import *
from radarview import RadarView
from aircraftRadarController import *
from aircraftDataProviders import FileDataProvider

def main():
    root = Tk()
    aircraftProvider = FileDataProvider('/Users/Kuppi/Desktop/Raspi/aircraft.json')
    controller = AircraftRadarController(aircraftProvider, root)
    controller.showAircraftRadar()
    root.mainloop()
    print("Exit mainloop")
    
if __name__ == "__main__":
    main()