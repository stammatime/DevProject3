import Orange
import random
import numpy as np
from scipy import cluster
from matplotlib import pyplot

#from matplotlib import pyplot as plt

def main():
    
  # Determine what value we should put in random.seed
  random.seed(42)
  data_input = Orange.data.Table("out.arff")  

  # Running kmeans algorithm here, need to determine what should go in # field
  km = Orange.clustering.kmeans.Clustering(data_input, 10)

  # Trying to figure out how to make a pretty plot but there's some library issues
  #Orange.clustering.kmeans.plot_silhouette(km, "kmeans-silhouette.svg")
  #print km.clusters

  # Calculate Euclidean Distance
  measure = Orange.distance.Euclidean(data_input)
  print measure(data_input[0], data_input[1])

  # Calculate Manhattan Distance
  poop = Orange.distance.Manhattan(data_input)
  print poop(data_input[0], data_input[1])

  # Transform to a distance matrix
  #matrix = Orange.distance.distance_matrix(data_input)
  #print matrix[0,1]

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


main()
