#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:13:31 2020

@author: michael
"""

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