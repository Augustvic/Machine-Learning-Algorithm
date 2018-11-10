from KNN import KNN
from Clustering import DensityBasedClustering
from Clustering import HierarchicalClustering
from Clustering import KMeansAlgorithm
from Clustering import LearningVectorQuantization
from Clustering import MixtureOfGaussianAlgorithm

if __name__ == '__main__':
    print("1. KNN")
    print("2. Density Based Clustering")
    print("3. Hierarchical Clustering")
    print("4. K-means Clustering")
    print("5. Learning Vector Quantization Clustering")
    print("6. Mixture of Gaussian Clustering")
    print("-------------------------------------------------------")
    num = input("Enter the number of the algorithm:")
    if num == str(1):
        algorithm = KNN.KNN()
        algorithm.execute()
    elif num == str(2):
        algorithm = DensityBasedClustering.DensityBasedClustering()
        algorithm.execute()
    elif num == str(3):
        algorithm = HierarchicalClustering.HierarchicalClustering()
        algorithm.execute()
    elif num == str(4):
        algorithm = KMeansAlgorithm.KMeansAlgorithm()
        algorithm.execute()
    elif num == str(5):
        algorithm = LearningVectorQuantization.LearningVectorQuantization()
        algorithm.execute()
    elif num == str(6):
        algorithm = MixtureOfGaussianAlgorithm.MixtureOfGaussianAlgorithm()
        algorithm.execute()
    else:
        print("Error num!")
        exit(-1)
