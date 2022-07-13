# affinity-propagation-entity-types
This repository contains the code and subsequent analysis for discovering entity types in variables logges in software code. 

## Data
Data used for clustering variables' names can be found under `data/`.

## Entity types
```html
No. |     Method      |                          Example(s)                               |
-------------------------------------------------------------------------------------------
 1  |   Generic Type  |            specs, range, targetAddr, nnc, kvstart, avg            |
 2  |      Path       |   basePath, dataPath, filePath, filePath2, fileSrcPath, fullPath  |    
 3  |       Id        |   reduceId, resID1, responseId, , results, , shellId, threadId    |
 4  |      File       |   destFiles, editFile, hostsFile, keytabFile, outputFile          |
 5  |     Priority    |   avgRespTimePriority, callVolumePriority, appPriority, priority  |
```

## Affinity propagation algorithm
<img width="1581" alt="affinity_propagation" src="https://user-images.githubusercontent.com/60047427/178629718-06e0af30-34a0-439f-a416-62c5f934b057.png">

## Results
Running `python affinity_propagation_analysis.py` results in the figure below. The algorithmic complexity of __Affinity propagation__ is quadratic in the number of points. For example, running the algorithm with 2k variables takes 259 seconds (4:19 minutes).
<img width="617" alt="affinity_propagation_clustering" src="https://user-images.githubusercontent.com/60047427/178629858-316aa09c-31ab-41be-b073-408837f11154.png">
