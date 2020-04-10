CC = g++
CFLAGS = -std=c++11 -g 
LFLAGS = -lboost_iostreams -lboost_system -lboost_filesystem
DEPS = DistanceOutlier.h MDPoint.h Outlier.h OutlierDetector.h TrajData.h Trajectory.h Param.h csv_parser.hpp

all: trajectory_detector

trajectory_detector: main.o Trajectory.o MDPoint.o OutlierDetector.o DistanceOutlier.o Measure.o Outlier.o csv_parser.o TrajData.o
	$(CC) $(CFLAGS) -o $@ $^ $(LFLAGS)

clean:
	-@rm *.o trajectory_detector

%.o: %.cpp $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<
    

