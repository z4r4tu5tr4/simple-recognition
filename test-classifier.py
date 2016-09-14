# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 02:14:43 2016

@author: laranjeira
"""

import pickle
import os
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import extractFeatures

# Test info
project_root = '/home/laranjeira/projects/peixe-babel/simple-recognition/'
dataset_root = project_root + 'dataset/'
test_images_dir = 'test-images/'

def column(matrix, i):
    return [row[i] for row in matrix]
    
def testClassifier():
    clf = pickle.load(open( "classifier.p", "rb" ))
    classes = numpy.loadtxt(dataset_root + 'classes.txt', dtype=str)
    classes = column(classes, 0)
        
    image_files = sorted(os.listdir(os.path.join(project_root, test_images_dir)))
    for image in image_files:
       features = extractFeatures.extractFeatures( str( os.path.abspath(os.path.join(project_root, test_images_dir, image)) ) )
       prediction = clf.predict(features)
       img = mpimg.imread(str( os.path.abspath(os.path.join(project_root, test_images_dir, image)) ))
       fig = plt.figure()
       fig.suptitle(classes[int(prediction[0])], fontsize=14, fontweight='bold')
       plt.imshow(img)
    
if __name__ == "__main__":
    testClassifier()
    