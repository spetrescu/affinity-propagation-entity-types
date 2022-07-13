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

## Example output
```html
Number of variables subjected to analysis:  3881
Number of variables (no duplicates) subjected to analysis:  50 

0 - *datanodeThreshold:* datanodeThreshold
1 - *successfulProxy:* successfulProxy
2 - *nextHeartBeatInterval:* nextHeartBeatInterval
3 - *outputDirPathForEntity:* outputDirPathForEntity
4 - *workDirPath:* BASE_DIR_NAME, blockListDirPath, committedTaskPath, copySourcePath, doneAppPath, envBinaryPath, homeDirectory, targetPath, workDirPath
5 - *DFS_NAMENODE_SNAPSHOT_DELETION_ORDERED:* DFS_NAMENODE_SNAPSHOT_DELETION_ORDERED
6 - *stripedFileChecksum2Recon:* stripedFileChecksum2Recon
7 - *selectCandidatesForResevedContainers:* selectCandidatesForResevedContainers
8 - *expectedTotalSpace:* expectedNodesList, expectedTotalSpace
9 - *maintenanceMinRepl:* maintenanceMinRepl
10 - *pe:* , basePort, blk, c, data, ipPath, node, ns, pe, resID3, skipCleanup, true, uploadId
11 - *retries:* absPathToRemove, curRetries, deadline, deleteDir, inMemBytes, lastLogFile, mergeOutputSize, nextBlockId, perDirFileLimit, priority, replica, retries, rootPath, startTimesCount, storeType, subDir, totalFileSize
12 - *expectedMovementFinishedBlocksCount:* expectedMovementFinishedBlocksCount

Total exemplars found: 14
Exemplar sizes, from highest to lowest:  [17, 13, 9, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Exemplar sizes (no duplicates), from highest to lowest:  [17, 13, 9, 2, 1]
```
Resulting histogram: <br>
<img width="564" alt="example_aff_propg" src="https://user-images.githubusercontent.com/60047427/178755258-e0e0b852-bcac-4dce-a5b6-256308572423.png">
