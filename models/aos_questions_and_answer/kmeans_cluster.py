# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:28:06 2018

@author: Eleam Emmanuel
"""

# This is to clear and reset and use CTRL+L in console to clear console
# %reset -f

import matplotlib
import pandas as pd

matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


class Clustering(object):
    def __init__(self, csv, ymeans_1=None, ymeans_2=None):
        self.csv = csv
        self.ymeans_1 = ymeans_1
        self.ymeans_2 = ymeans_2

        # importing the dataset with pandas
        # 'dataset/clustering/system_eng_cluster.csv'
        self.dataset_loader = pd.read_csv(self.csv)
        self.X1 = self.dataset_loader.iloc[:, [2, 4]].values
        self.X2 = self.dataset_loader.iloc[:, [3, 4]].values

    @staticmethod
    def process_wcss(x_column_for_wcss):
        wcss_to_process = []
        for i in range(1, 11):
            kmeans_1 = KMeans(n_clusters=i, init='k-means++', max_iter=300,
                              n_init=10, random_state=0)
            kmeans_1.fit(x_column_for_wcss)
            wcss_to_process.append(kmeans_1.inertia_)

        return wcss_to_process

    @staticmethod
    def plot_wcss(wcss_list, course_title):
        plt.plot(range(1, 11), wcss_list)
        plt.title("The Elbow Method For Test")
        plt.xlabel("Number of clusters")
        plt.ylabel("wcss for {}".format(course_title))
        plt.show()
        plt.imsave()

    def predict_data(self):
        # applying k-means to the mall dataset
        kmeans_predict = KMeans(n_clusters=6, init='k-means++', max_iter=300,
                                n_init=10, random_state=0)
        self.ymeans_1 = kmeans_predict.fit_predict(self.X1)
        self.ymeans_2 = kmeans_predict.fit_predict(self.X2)
        return self.ymeans_1, self.ymeans_2

    @staticmethod
    def visualise_clusters(x_column_to_visualize, y_column_to_visualise, test_title):
        kmeans_clusters = KMeans(n_clusters=6, init='k-means++', max_iter=300,
                                 n_init=10, random_state=0)
        kmeans_clusters.fit(x_column_to_visualize)
        # Visualizing the clusters
        plt.scatter(x_column_to_visualize[y_column_to_visualise == 0, 0],
                    x_column_to_visualize[y_column_to_visualise == 0, 1],
                    s=10, c='red', label='Cluster 1')
        plt.scatter(x_column_to_visualize[y_column_to_visualise == 1, 0],
                    x_column_to_visualize[y_column_to_visualise == 1, 1],
                    s=10, c='blue', label='Cluster 2')
        plt.scatter(x_column_to_visualize[y_column_to_visualise == 2, 0],
                    x_column_to_visualize[y_column_to_visualise == 2, 1],
                    s=10, c='green', label='Cluster 3')
        plt.scatter(x_column_to_visualize[y_column_to_visualise == 3, 0],
                    x_column_to_visualize[y_column_to_visualise == 3, 1],
                    s=10, c='cyan', label='Cluster 4')
        plt.scatter(x_column_to_visualize[y_column_to_visualise == 4, 0],
                    x_column_to_visualize[y_column_to_visualise == 4, 1],
                    s=10, c='magenta', label='Cluster 5')
        plt.scatter(x_column_to_visualize[y_column_to_visualise == 5, 0],
                    x_column_to_visualize[y_column_to_visualise == 5, 1],
                    s=10, c='black', label='Cluster 6')
        plt.scatter(kmeans_clusters.cluster_centers_[:, 0], kmeans_clusters.cluster_centers_[:, 1],
                    s=50, c='yellow', label='Centroids')
        plt.title("Clusters OF Students Performance Based On Test Score")
        plt.xlabel("{} SCORE".format(test_title))
        plt.ylabel("Test score")
        plt.legend()
        plt.show()
