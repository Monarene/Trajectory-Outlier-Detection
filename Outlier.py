#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:02:41 2020

@author: michael
"""

#importing the necesary import
import numpy as np
import MDPoint
import Trajectory

#These are the necessary Parameters
COMBO_II = True
USE_CONVENTIONAL_PARTITIONING = True
USE_NO_PARTITIONING = False
PARTITION_PRUNING_OPTIMIZATION = True
SHOW_TRAJECTORY_PARTITION = False
INCORPORATE_DENSITY = True
PRECOMPUTE_DENSITY = True
VISUALIZE_DEBUG_INFO = False

#the parameters
g_FRACTION_PARAMETER = 0.95
g_DISTANCE_PARAMETER = 82.0
g_MINIMUM_OUTLYING_PROPORTION = 0.50
MDL_COST_ADVANTAGE = 20
MIN_LINSEGMENT_LENGTH = 1.0
MAX_LINESEGMENT_LENGTH = 10000.0

def WEIGHTED_DISTANCE(x, y, z):
    return (1.0 * x + 1.0 * y + 10.0 * z)

RESULT_FILE = "results.txt"

#This is the code from the MDPoint
class CMDPoint:
    
    m_nDimensions = 2
    m_coordinate = np.array([0.0,0.0])
    
    def __init__(self, nDimensions):
        self.nDimensions = nDimensions
        
    def GetNDimensions(self):
        return self.m_ndimensions
    
    def GetCoordinate(self, nth):
        return self.m_coordinate[nth]
    
    def SetCoordinate(self, nth, value):
        self.m_coordinate[nth] = value
        
#implementing Trajectory file
class PartitionInfo:
    maxPerpDist = 0.0
    minLength = 0.0
    maxLength = 0.0
    maxTheta = 0.0
    
class CTajectory(COutlierDetector, CDistanceOutlier):
    
    m_trajectoryId = -1
    m_nDimensions = 2
    m_nPoints = 0
    m_pointArray = np.array([])
    m_nPartitionPoints = 0
    m_partitionPointArray = []
    m_partitionIndexArray = []
    m_partitionInfoArray = []
    m_totalPartitionLength = 0.0
    m_outlyingPartitionLength = 0.0
    m_nOutlyingPartitions = 0
    m_outlyingPartitionArray = []
    m_nPenWidth = 1
    m_containOutlier = False
    
    def __init__(self, id, nDimensions):
        self.m_trajectoryId = id
        self.m_nDimensions = nDimensions
        
    def SetId(self, id):
        self.m_trajectoryId = id
        
    def GetId(self):
        return self.m_trajectoryId
    
    def AddPointToArray(self, point):
        self.m_pointArray.append(point)
        self.m_nPoints++
        
    def AddPartitionPointToArray(self, point, index):
        self.m_partitionPointArray.append(point)
        self.m_partitionIndexArray.append(index)
        self.m_nPartitionPoints++
        
    def StorePartitionInfo(self, info):
        self.m_partitionInfoArray.append(info)
        
    def SetLength(self, length):
        self.m_totalPartitionLength = length
        
    def GetLength(self):
        return self.m_totalPartitionLength
    
    def SetOutlyingLength(self, length):
        self.m_outlyingPartitionLength = length
        
    def GetOutlyingLength(self):
        return self.m_outlyingPartitionLength
    
    def GetNumOutlyingPartitions(self):
        return self.m_nOutlyingPartitions
    
    def GetPointArray(self):
        return self.m_pointArray
    
    def GetPartitionPointArray(self):
        return self.m_partitionPointArray
    
    def AddOutlyingPartition(self, index):
        self.m_outlyingPartitionArray.append(index)
        self.m_nOutlyingPartitions++
        
    def GetOutlyingPartition(self, nth):
        index = self.m_outlyingPartitionArray[nth]
        if (USE_CONVENTIONAL_PARTITIONING) and (not PARTITION_PRUNING_OPTIMIZATION):
            value_1 = self.m_partitionPointArray[index]
            value_2 = self.m_partitionPointArray[index + 1]
        else:
            value_1 = self.m_pointArray[index]
            value_2= self.m_pointArray[index + 1]
        return value_1, value_2
    
    def __del__(self):
        self.m_nPoints = 0
        self.m_containOutlier = False
    
        
#This is implementing the TrajData
class TrajData:
    m_inputFilePath = ""
    m_nDimensions = 0
    m_nTrajectories = 0
    m_nOutliers = 0
    m_nOutlyingPartitions = 0
    m_trajectoryList = [] #check out for this, it is of the type CTrajectory
    m_outlierList = [] #check and ensure that this is a list of outliers
    m_paramFraction = g_FRACTION_PARAMETER
    M_paramDistance = g_DISTANCE_PARAMETER
    m_nLineSegments = 0
    m_nTrajectoryPartitions = 0
    readFile = True
    n_maxNPoints = 0
       
#This is implementing Outlier File
pTrajectory = CTrajectory()
LineSegment = [0,0]

class COutlier(COutlierDetector):
    
    m_outlierId = -1
    m_nDimensions = 2 
    m_trajectoryId =-1
    m_nOutlyingPartitions = 0
    m_outlyingPartitionArray = []
    m_outlyingRatio = 0.0
    m_nPenWidth = 3
    
    
    def __init__(self, id, trajectoryId, nDimensions):
        self.m_outlierId = id
        self.m_trajectoryId = trajectoryId
        self.m_nDimensions  = nDimensions
        
    def SetId(self):
        m_outlierId = self.id
        
    def GetId(self):
        return self.m_outlierId
    
    def GetTrajectoryId(self):
        return self.m_ttrajectoryId
    
    def GetNOutlyingPartitions(self):
        return self.m_nOutlyingPartitions
    
    def GetOutlyingPartitionsArray(self):
        return self.m_outlyingPartitionArray 
    
    def GetOutlyingRatio(self):
        return self.m_outlyingRatio
    
    def SetUpInfo(self, pTrajectory):
        self.m_nOutlyingPartitions = pTrajectory.GetNumOutlyingPartition()
        for i in range(0, self.m_nOutlyingPartitions):
            value_1, value_2 = pTrajectory.GetOutlyingPartition(i)
            startPoint = CMPoint(2)
            endPoint = CMDPoint(2)
            for j in range(0, m_nDimensions):
                startPoint.SetCoordinate(j, value_1.GetCoordinate(j))
                endPoint.SetCoordinate(j, value_2.GetCoordinate(j))
            self.m_outlylineSegment[0]ingPartitionArray.append([startPoint, endPoint])
        self.m_outlyingRatio = pTrajectory.GetOutlyingLength() / pTrajectory.GetLength()
        
    def __del__(self):
        self.m_nOutlyingPartitions = 0
        

        
    
    