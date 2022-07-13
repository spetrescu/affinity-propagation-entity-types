import numpy as np
from sklearn.cluster import AffinityPropagation
import distance
from matplotlib import pyplot as plt


variables = []

with open('data/variables_names.csv') as f:
    lines = f.readlines()

for line in lines:
    variables.append(line)

#vars = Discover_Variables(path_to_dir_containing_codebase=path_to_dir_containing_codebase, path_to_log_dataset=path_to_log_dataset, language=language)
#vars.find_variables_in_a_given_directory()
#words = "job.getJobID server.getNumOpenConnections subClusterId count numOpsRequired timestampedDirList.size oldFile".split(" ") #Replace this line
num_of_variables = len(variables)
print(num_of_variables)
variables = list(set(variables))
#variables = variables[:100]
num_of_variables = len(variables)
print(num_of_variables)
words = np.asarray(variables) #So that indexing with a list will work
lev_similarity = -1*np.array([[distance.levenshtein(w1,w2) for w1 in words] for w2 in words])

affprop = AffinityPropagation(affinity="precomputed", damping=0.5, max_iter=200, random_state=5)
affprop.fit(lev_similarity)
no_of_examplars = 0
cluster_sizes = []
for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)
    print(" - *%s:* %s" % (exemplar, cluster_str))
    no_of_examplars += 1
    cluster_sizes.append(len(cluster))
    print(f"No exemplars: {no_of_examplars}; Cluster size: {len(cluster)}")

print(cluster_sizes)
#plt.hist(cluster_sizes, len(cluster_sizes))
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
cluster_sizes = cluster_sizes[:30]

for cluster_id in np.unique(affprop.labels_):
    exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
    cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
    cluster_str = ", ".join(cluster)
    #cluster_sizes.append(len(cluster))
    if len(cluster) >= min(cluster_sizes):
        print(" - *%s:* %s" % (exemplar, cluster_str))
    #print(f"No exemplars: {no_of_examplars}; Cluster size: {len(cluster)}")
plt.xlabel("Exemplar size")
plt.ylabel("Number of occurences")
#plt.xticks([1, 2, 3, 4, 5, 6, 7], ['10', '50', '100', '200', '300', '500', '1000'])
plt.xticks([el for el in range(max(cluster_sizes)+2) if el % 2 == 0])
plt.yticks([el for el in range(freq_element_that_appears_the_most+4) if el % 4 == 0])
#[x for x in range(100) if x % 2 != 0]
plt.title("Affinity propagation clustering")
# plt.savefig('affinity_propagation_clustering_hist.pdf')
plt.show()