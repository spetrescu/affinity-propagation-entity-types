import numpy as np
from sklearn.cluster import AffinityPropagation
import distance
from matplotlib import pyplot as plt

variables = []

with open('data/variables_names.csv') as f:
    lines = f.readlines()

for line in lines:
    line = line.rstrip()
    variables.append(line)

num_of_variables = len(variables)
print("Number of variables subjected to analysis: ", num_of_variables)
variables = list(set(variables))
variables = variables[:100]
num_of_variables = len(variables)
print("Number of variables (no duplicates) subjected to analysis: ", num_of_variables, "\n")
words = np.asarray(variables)
lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])

affprop = AffinityPropagation(affinity="precomputed", damping=0.5, max_iter=200, random_state=5)
affprop.fit(lev_similarity)
no_of_examplars = 1
cluster_sizes = []
for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)
    no_of_examplars += 1
    print("%s - *%s:* %s" % (cluster_id, exemplar, cluster_str))
    cluster_sizes.append(len(cluster))

print(f"\nTotal exemplars found: {no_of_examplars}")

plt.hist(cluster_sizes, bins=np.arange(min(cluster_sizes), max(cluster_sizes)+2)-0.5, edgecolor='black', color='mediumturquoise', linewidth=0.5)
element_that_appears_the_most = max(cluster_sizes,key=cluster_sizes.count)

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
freq_element_that_appears_the_most = countX(cluster_sizes, element_that_appears_the_most)
cluster_sizes.sort(reverse=True)

print("Exemplar sizes, from highest to lowest: ", cluster_sizes)
cluster_sizes_no_duplicates = list(set(cluster_sizes))
cluster_sizes_no_duplicates.sort(reverse=True)
print("\nExemplar sizes (no duplicates), from highest to lowest: ", cluster_sizes_no_duplicates)

# select the largest 30 clusters
cluster_sizes = cluster_sizes[:30]

for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)

plt.xlabel("Exemplar size")
plt.ylabel("Number of occurences")
plt.xticks([el for el in range(max(cluster_sizes)+2) if el % 2 == 0])
plt.yticks([el for el in range(freq_element_that_appears_the_most+4) if el % 4 == 0])
plt.title("Affinity propagation clustering")
# plt.savefig('affinity_propagation_clustering_hist.pdf')
plt.show()