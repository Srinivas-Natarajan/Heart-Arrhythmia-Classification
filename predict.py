import numpy as np
import tensorflow as tf

from preprocessing import edftocsv

def predict_class(edf_file_path):
    df = edftocsv(edf_file_path, "ECG")
    loaded_model = tf.keras.models.load_model('./my_model_30')
    X = df.iloc[:,:186].values
    X = X.reshape(len(X), X.shape[1],1)
    y_pred = loaded_model.predict(X, batch_size=1000)
    prediction = np.argmax(y_pred,axis=1)
    print(prediction)
    np.save('./ECG_classification', prediction)
