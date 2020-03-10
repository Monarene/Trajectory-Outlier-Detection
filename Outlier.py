#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:02:41 2020

@author: michael
"""

#importing the necesary import
import MDPoint
import Trajectory

#These are the necessary Parameters
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
    m_coordinate = [0.0,0.0]
    
    def __init__(self, nDimensions):
        self.nDimensions = nDimensions
        
    def GetNDimensions(self):
        return self.m_ndimensions
    
    def GetCoordinate(self, nth):
        return self.m_coordinate[nth]
    
    def SetCoordinate(self, nth, value):
        self.m_coordinate[nth] = value
        
#This is implementing the TrajData
class TrajData:
    m_inputFilePath = ""
    m_nDimensions = 0
    m_nTrajectories = 0
    m_nOutliers = 0
    m_nOutlyingPartitions = 0
    m_trajectoryList = [] #check out for this, it is of the type CTrajectory
        
#This is implementing Outlier File
pTrajectory = CTrajectory()
LineSegment = []

class COutlier(COutlierDetector):
    
    m_outlierId = -1
    m_nDimensions = 2 
    m_trajectoryId =-1
    m_nOutlyingPartitions = 0
    m_outlyingPartitionArray = []
    m_outlyingRatio = 0.0
    m_nPenWidth = 3
    
    
    def __init__(self, id, trajectoryId, nDimensions):
        self.id = id
        self.trajectoryId = trajectoryId
        self.nDimensions  = nDimensions
        
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
            aPartition = pTrajectory.GetOutlyingPartition(i)
            startPoint = CMPoint(2)
            endPoint = CMDPoint(2)
            for j in range(0, m_nDimensions):
                startPoint.SetCoordinate(j, aPartition[0].GetCoordinate(j))
                endPoint.SetCoordinate(j, aPartitition[1].GetCoordinate(j))
            Linesegment.append([startPoint, endPoint])
        self.m_outlyingRatio = pTrajectory.GetOutlyingLength() / pTrajectory.GetLength()
        

        
    
    