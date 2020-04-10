#A file for functions for performing trajectory detection
import os

def trajectory_plot(infile, outfile):
    print("ploting trajectory...")

    os.system('./trajectory_detector --plot ' + infile + " " + outfile)

    print("done plotting trajectory. the output file is " + outfile)

def trajectory_convert_csv(infile, outfile):
    print("converting " + infile + " to " + outfile)

    os.system('./trajectory_detector --convert ' + infile + " " +  outfile)

    print("done converting. you can now plot the  trajectory of " + outfile)

def trajectory_convert_plot(infile, outfile):
    print("converting and plotting trajectory of " + infile)

    os.system('./trajectory_detection --convplot ' + infile + " " +  outfile)

    print("done plotting trajectory. the output file is " + outfile)

def trajectory_help():
    os.system('./trajectory_detector --help')