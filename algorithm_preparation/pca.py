import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pickle

# Load in the data
df = pd.read_csv('../datasets/drop_low_entries_dataset_smote.csv')
# Standardize the data to have a mean of ~0 and a variance of 1
X_std = StandardScaler().fit_transform(df)
# Create a PCA instance: pca
pca = PCA(n_components=90)
principalComponents = pca.fit_transform(X_std)
X_re_orig = pca.inverse_transform(principalComponents)  ###############################3
#print(X_re_orig)  ##########################3
# Plot the explained variances
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_ratio_, color='black')
#print(sum(pca.explained_variance_ratio_))
plt.xlabel('PCA features')
plt.ylabel('variance %')
plt.xticks(features)
# Save components to a DataFrame
PCA_components = pd.DataFrame(principalComponents)
plt.savefig('../img/pca.png')
plt.show()

ks = range(1, 10)
inertias = []
for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)

    # Fit model to samples
    model.fit(PCA_components.iloc[:, :3])

    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)

plt.plot(ks, inertias, '-o', color='black')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.savefig('../img/elbow_method.png')
plt.show()

with open('pca.pkl', 'wb') as pickle_file:
    pickle.dump(pca, pickle_file)

with open('pca.pkl', 'rb') as pickle_file:
    pca = pickle.load(pickle_file)
scaled_data = pca.fit_transform(X_std)

kmeans = KMeans(n_clusters=4, random_state=10).fit(principalComponents)

print(kmeans.cluster_centers_)
print(kmeans.labels_)

plt.scatter(principalComponents[:,0], principalComponents[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.savefig('../img/clustering_2.png')
plt.show()
#print("AQUI", principalComponents)
#print("ALI", scaled_data)
