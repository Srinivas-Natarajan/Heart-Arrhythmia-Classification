import numpy as np
import sys 
import tensorflow as tf

import warnings
warnings.filterwarnings('ignore')

from preprocessing import edftocsv

def predict_class(edf_file_path):
    df = edftocsv(edf_file_path, "ECG")
    classes = {0:'N', 1:'S', 2:'V', 3:'F', 4:'Q'} 
    loaded_model = tf.keras.models.load_model('./my_model_30')

    X = df.iloc[:,:186].values
    X = X.reshape(len(X), X.shape[1],1)

    y_pred = loaded_model.predict(X, batch_size=1000)
    prediction = np.argmax(y_pred,axis=1)
    labels = []
    for i in range(prediction.shape[0]):
        labels.append(classes[prediction[i]])
    np.savetxt('./ECG_classification.txt', labels, fmt='%s')
    return labels


#EDF_PATH = "./files/100.edf"   #Add path to the EDF file without the ".edf" extension

print("\n\nThe classes are: \n", predict_class(sys.argv[1]))

