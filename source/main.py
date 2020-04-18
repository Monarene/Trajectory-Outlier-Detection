#this example application shows how the trajectory.py and trajectory_detector files can be used

from trajectory import trajectory_plot, trajectory_convert_plot, trajectory_convert_csv, trajectory_help

def main():
    print("Welcome to the test of trajectory.py and trajectory_detector")

    print("This example plots the trajectory of hurricane2000_2006.tra")

    trajectory_plot("hurricane2000_2006.tra", "hurricane2000_2006.eps")

main()