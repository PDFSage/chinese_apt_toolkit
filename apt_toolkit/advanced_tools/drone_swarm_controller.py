import time

class Drone:
    def __init__(self, id):
        self.id = id

    def takeoff(self):
        print(f"Drone {self.id} taking off")

    def land(self):
        print(f"Drone {self.id} landing")

def main():
    drones = [Drone(i) for i in range(5)]
    for drone in drones:
        drone.takeoff()
        time.sleep(1)
    for drone in drones:
        drone.land()
        time.sleep(1)

if __name__ == "__main__":
    main()
