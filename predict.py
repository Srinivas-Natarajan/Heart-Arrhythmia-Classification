import numpy as np
import sys 
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings
warnings.filterwarnings('ignore')

from preprocessing import edftocsv

def predict_class(edf_file_path):
    """
        Input
            edf_file_path - Path to the EDF file
        Output
            labels - List containing labels of each R-peak
    """
    #Load data and model
    df = edftocsv(edf_file_path, "ECG")
    classes = {0:'N', 1:'S', 2:'V', 3:'F', 4:'Q'} 
    loaded_model = tf.keras.models.load_model('./my_model_30')

    #Format loaded EDF file
    X = df.iloc[:,:186].values
    X = X.reshape(len(X), X.shape[1],1)

    #Predict values and save to the local system
    y_pred = loaded_model.predict(X, batch_size=1000)
    prediction = np.argmax(y_pred,axis=1)
    labels = []
    for i in range(prediction.shape[0]):
        labels.append(classes[prediction[i]])
    np.savetxt('./files/ECG_classification.txt', labels, fmt='%s')
    np.save('./files/ECG_classification', labels)

    return labels



print("\n\nThe classes are: \n", predict_class(sys.argv[1]))

