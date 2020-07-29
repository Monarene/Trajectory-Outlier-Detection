#A file for functions for performing trajectory detection
import os
import io

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num-1] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def trajectory_plot(infile, outfile):
    os.system('make')
    print("ploting trajectory...")

    os.system('./trajectory_detector --plot ' + infile + " " + outfile)

    print("Done plotting trajectory. the output file is " + outfile)

def trajectory_convert_csv(infile, outfile):
    os.system('make')
    print("converting " + infile + " to " + outfile)

    os.system('./trajectory_detector --convert ' + infile + " " +  outfile)

    print("Done converting. you can now plot the  trajectory of " + outfile)

def trajectory_convert_plot(infile, outfile):
    os.system('make')
    print("converting and plotting trajectory of " + infile)

    os.system('./trajectory_detection --convplot ' + infile + " " +  outfile)

    print("Done plotting trajectory. the output file is " + outfile)

def set_g_fraction(param_value):
    replace_line("Param.h", 22, "const float g_FRACTION_PARAMETER = (float)" + str(param_value) + ";\n")

def set_g_distance(param_value):
    replace_line("Param.h", 23, "const float g_DISTANCE_PARAMETER = (float)" + str(param_value) + ";\n")

def set_g_min_outlier(param_value):
    replace_line("Param.h", 24, "const float g_MINIMUM_OUTLYING_PROPORTION = (float)" + str(param_value) + ";\n")

def set_mdl_cost(param_value):
    replace_line("Param.h", 26, "const int MDL_COST_ADVANTAGE = " + str(param_value) + ";\n")

def set_min_lineseg(param_value):
    replace_line("Param.h", 27, "const float MIN_LINESEGMENT_LENGTH = " + str(param_value) + ";\n")

def set_max_lineseg(param_value):
    replace_line("Param.h", 28, "const float MAX_LINESEGMENT_LENGTH = " + str(param_value) + ";\n")

def set_default_parameters():
    replace_line("Param.h", 22, "const float g_FRACTION_PARAMETER = (float)0.95;\n")
    replace_line("Param.h", 23, "const float g_DISTANCE_PARAMETER = (float)82.0;\n")
    replace_line("Param.h", 24, "const float g_MINIMUM_OUTLYING_PROPORTION = (float)0.50;\n")
    replace_line("Param.h", 26, "const int MDL_COST_ADVANTAGE = 20;\n")
    replace_line("Param.h", 27, "const float MIN_LINESEGMENT_LENGTH = 1.0;\n")
    replace_line("Param.h", 28, "const float MAX_LINESEGMENT_LENGTH = 10000.0;\n")

    os.system('make')

def trajectory_help():
    os.system('./trajectory_detector --help')

set_max_lineseg(100)
set_g_fraction(90)
#set_default_parameters()



