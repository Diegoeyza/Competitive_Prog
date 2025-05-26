import numpy as np
import matplotlib.pyplot as plt

def kmeans(X,k=3,n_iter=10):
    C= X[np.random.choice(len(X),k,replace=False)]
    for iteration in range (n_iter):
        labels=np.argmin(((X[:,None]-C)**2).sum(2), axis=1)
        C=np.array([X[labels==i].mean(0) for i in range(k)])
    return C,labels


def plot_kmeans(X, labels, centroids, title="K-Means Clustering"):
    k = len(centroids)
    colors = plt.cm.get_cmap("tab10", k)

    plt.figure(figsize=(8, 6))
    for i in range(k):
        points = X[labels == i]
        plt.scatter(points[:, 0], points[:, 1], s=30, color=colors(i), label=f'Cluster {i}')

    plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=100, marker='X', label='Centroids')
    plt.title(title)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

X=np.random.rand(100,2)
centroids,labels=kmeans(X,3)
plot_kmeans(X, labels, centroids)