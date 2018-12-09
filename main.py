import json
import queue
from tkinter import *
from radarview import RadarView
from aircraftRadarController import *
from aircraftDataProviders import AircraftProviderFactory
from configuration import ConfigStore

def main():
    root = Tk()
    config = ConfigStore()

    aircraftProvider = AircraftProviderFactory().getAircraftProvider(config.getAircraftDataSourceType(), config.getAircraftDataSourceDestination())
    
    controller = AircraftRadarController(aircraftProvider, root)
    controller.showAircraftRadar()
    root.mainloop()
    print("Exit mainloop")
    
if __name__ == "__main__":
    main()