import Orange
import random
from matplotlib import pyplot as plt
from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import vq, kmeans, whiten
# What is the point of these below? 
import math
import sys
import orngClustering
from Orange import statc
#from matplotlib import pyplot as plt


def main():
    
  # Determine what value we should put in random.seed
  random.seed(42)
  data_input = Orange.data.Table("out.arff")

  # Running kmeans algorithm here, need to determine what should go in # field
  km = Orange.clustering.kmeans.Clustering(data_input, 3)
  print km.clusters[-1000:]

  # Calculate Euclidean Distance
  measure = Orange.distance.Euclidean(data_input)
  print measure(data_input[0], data_input[1])

  # Calculate Manhattan Distance
  poop = Orange.distance.Manhattan(data_input)
  print poop(data_input[0], data_input[1])

  # Transform to a distance matrix
  matrix = Orange.distance.distance_matrix(data_input)
  #print matrix[0,1]



  # Data Generation (rand(150,2) + array([.5,.5]),rand(150,2))
  dat = vstack(matrix)

  # Computing k means with K = 3
  centroids,_ = kmeans(dat, 3)
  # Assign each sample to a cluster
  idx,_ = vq(dat, centroids)

  # Some plotting using numpy's logical indexing
  plot(dat[idx==0,0],dat[idx==0,1], 'ob',
       dat[idx==1,0],dat[idx==1,1], 'or',
       dat[idx==2,0],dat[idx==2,1], 'og')
  plot(centroids[:,0],centroids[:,1], 'sg', markersize=8)
  show()
  # Need to close the figure window after it closes


  # Hierarchical clustering (average linkage)
  sim_matrix = Orange.misc.SymMatrix(len(data_input))
  sim_matrix = Orange.distance.distance_matrix(data_input, Orange.distance.Euclidean)
  hier = Orange.clustering.hierarchical.HierarchicalClustering()
  hier.linkage = Orange.clustering.hierarchical.AVERAGE
  root = hier(sim_matrix)
  root.mapping.objects = data_input

  # Make the dendrogram.  Not sure if we need all of the lines below or what,
  # BUT IT WORKS!!!!
  sample = data_input.select(Orange.data.sample.SubsetIndices2(data_input, 40), 0)
  root = Orange.clustering.hierarchical.clustering(sample)
  labels = [str(d.get_class()) for d in sample]
  Orange.clustering.hierarchical.dendrogram_draw("hclust-dendrogram.svg", root, labels=labels)

  
#def callback(km):
 #   print "Iteration: %d, changes: %d, score: %8.6f" % (km.iteration, km.nchanges, km.score)

main()


