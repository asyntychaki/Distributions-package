#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:40:31 2020

@author: asyntychaki
"""

import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution # The '.' id required only for Python 3


class Gaussian(Distribution):
    """ A Gaussian distribution class for calculating and 
	visualizing a Gaussian distribution.
    It inherits from the general distribution class.
	
	Attributes:
	mean (float) representing the mean value of the distribution
	stdev (float) representing the standard deviation of the distribution
	data_list (list of floats) a list of floats extracted from the data file
	"""
    
    def __init__(self, mu=0, sigma=1):
        
        Distribution.__init__(self, mu, sigma)
        
    
    def calculate_mean(self):
        """Method to calculate the mean of the data set.
		
        Args: None
        
		Returns: 
		float: mean of the data set
		"""
					
        self.mean = sum(self.data) / len(self.data)
        
        return self.mean
    
    
    
    def calculate_stdev(self, sample=True):
        """Method to calculate the standard deviation of the data set.
        
        Args: 
        sample (bool): whether the data represents a sample or population
        
        Returns: 
        float: standard deviation of the data set
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        
        sigma = 0
        for num in self.data:
            sigma += (num - self.mean)**2
        
        self.stdev = math.sqrt( sigma / n)
        
        return self.stdev
    
    
    def read_data_file(self, file_name, sample=True):
        """Method to read in data from a txt file. 
        It overwrites the read_data_file method of the parent general distribution class.
        After reading in the file, the mean and standard deviation are calculated      
        
        Args:
            file_name (string): name of a file to read from
        
        Returns: None
        """
        
        # This code opens a data file and appends the data to a list called data_list
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
    
        self.data = data_list
        # Update self.mean with the mean of the data_list. 
        self.mean = self.calculate_mean()
        # Update self.stdev with the standard deviation of the data_list.
        self.stdev = self.calculate_stdev(sample)
    
    
    
    
    def plot_histogram(self):
        """Method to output a histogram of the instance variable data.
        Args:  None    
        Returns: None
        """

        plt.hist(self.data)
        plt.xlabel = 'Count'
        plt.ylabel = 'Data'
        plt.title = 'Histogram of Data'
        
        
        
    
    
    
    
    