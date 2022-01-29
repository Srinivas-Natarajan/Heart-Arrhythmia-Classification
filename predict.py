import numpy as np
import sys 
import os
import tensorflow as tf

import warnings
warnings.filterwarnings('ignore')

from preprocessing import edftocsv

def predict_class(edf_file_path):
    df = edftocsv(edf_file_path, "ECG")
    loaded_model = tf.keras.models.load_model('./my_model_30')
    X = df.iloc[:,:186].values
    X = X.reshape(len(X), X.shape[1],1)
    y_pred = loaded_model.predict(X, batch_size=1000)
    prediction = np.argmax(y_pred,axis=1)
    np.save('./ECG_classification', prediction)
    return prediction


EDF_PATH = "./files/100.edf"   #Add path to the EDF file without the ".edf" extension

print("\n\nThe classes are: \n",predict_class(EDF_PATH))

#print(os.path.dirname(sys.executable))
#print("\nArguments", sys.argv[0])

