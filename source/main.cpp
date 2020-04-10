#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include "TrajData.h"
#include "OutlierDetector.h"
#include "csv_parser.hpp"
#include <iomanip>
#include <limits>
#include <vector>
#include <map>

using namespace std;

//function prototypes
void plot_trajectory(const string, const string);
void convert_data(const string, const string);


int main (int argc, char** argv) {

	if(argc>1){ // check if there are arguments

		for(int i=1; i<argc; i++){

			if( !strcmp(argv[i], "--plot") || !strcmp(argv[i], "-p") ){

				const string infile = argv[++i];
				const string outfile = argv[++i];

				plot_trajectory(infile, outfile);

			}else if( !strcmp(argv[i], "--convert") || !strcmp(argv[i], "-c") ){

				const string infile = argv[++i];
				const string outfile = argv[++i];

				convert_data(infile, outfile);
				
			}else if( !strcmp(argv[i], "--convplot") || !strcmp(argv[i], "-cp") ){
				//combination of the above two processes
				const string infile = argv[++i];
				const string outfile = argv[++i];

				const string temp = "temp.tra";

				convert_data(infile, temp);
				plot_trajectory(temp, outfile);

				//delete temp file
				system("rm temp.tra");

			}else if( !strcmp(argv[i], "--help") || !strcmp(argv[i], "-h") ){

				cout << "Trajectory_Detector: \n" << endl;

				cout << "	--plot or -c <file location of .tra file> <output file name of .eps extension> \n" << endl;

				cout << "	--convert or -c <file location of input file> <output file name of .tra file> \n" << endl;

				cout << "	--help or -p to show this message\n" << endl; 

			}else{
				cout << "Wrong use of arguments, please try		trajectory_detector --help		for further clarity \n\n" << endl;
				break;
			}
		}

	}else{ // if there aren't any arguments

		//print description message
		cout << " " << endl;
	}

    return 0;
}

void plot_trajectory(const string infile, const string outfile){
	// TrajData reads in data and holds trajectory information
	TrajData data;
	data.readFile(infile);

	// COutlierDetector will find outliers in the provided dataset
	COutlierDetector outlierDetector(&data);
	outlierDetector.PartitionTrajectory();
	outlierDetector.DetectOutlier();
	cout << "Size of trajectory outlierList: " << data.m_outlierList.size() << "\n";
	cout << "Finished partitioning and finding outliers!\n";

	// Output plot of trajectories and outliers
	data.OutputTrajectoryPlot(outfile);
}

void convert_data(const string infile, const string outfile){
	const string filename(infile);

	const char field_terminator = ',';
	const char line_terminator = '\n';
	const double m_per_lon = 85417;
	const double m_per_lat = 111030;

	csv_parser file_parser;

	file_parser.set_skip_lines(1);
	file_parser.init(filename.c_str());
	file_parser.set_field_term_char(field_terminator);
	file_parser.set_line_term_char(line_terminator);

	unsigned int row_count = 1U;

	struct point {
		int id;
		double lat;
		double lon;
		int frame;
	};

	double min_lat = 90;
	double min_lon = 180;

	map<int, vector<point> > points;

	while(file_parser.has_more_rows()){
		
		csv_row row = file_parser.get_row();

		int id = atoi(row[0].c_str());
		double lat = atof(row[1].c_str());
		double lon = atof(row[2].c_str());
		int frame = atoi(row[6].c_str());

		if(frame > 400)
			continue;

		if( lat < min_lat ) { min_lat = lat; }
		if( lon < min_lon ) { min_lon = lon; }

		point new_point;
		new_point.id = id; new_point.lat = lat; new_point.lon = lon; new_point.frame = frame;

		points[id].push_back(new_point);


		if(row_count % 10000 == 0){
			cout << "Row " << row_count << "\n";
		}

        row_count++;
	}

	// remove short paths
	for( auto iter = points.begin(); iter != points.end(); iter++){
		if(iter->second.size() < 20){
			points.erase(iter++);
		}
	}

	ofstream ofile;
	ofile.open(outfile);
	ofile << "2\n";
	ofile << points.size() << "\n";

	for( auto map_pair : points){
		ofile << map_pair.first - 1 << " " << map_pair.second.size();
		for( auto p : map_pair.second){
			ofile << " " << (p.lon - min_lon) * m_per_lon << " " << (p.lat - min_lat) * m_per_lat;
		}
		ofile << "\n";
	}
	ofile.close();

}
