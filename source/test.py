import os

os.system('make')
os.system('rm *.o')

os.system('./trajectory_detector -h')

os.system('./trajectory_detector -p hurricane2000_2006.tra output1.eps')

os.system('./trajectory_detector -cp hurricanes.csv output2.eps')

os.system('./trajectory_detector -cp fishingvessels.csv output3.eps')
