import numpy as np

arr = np.load("./ECG_classification.npy")
classes = {0:'N', 1:'S', 2:'V', 3:'F', 4:'Q'} 
labels = []
for i in range(arr.shape[0]):
    labels.append(classes[arr[i]])

print(labels)