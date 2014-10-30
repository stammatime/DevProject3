import Orange
import random
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



main()
