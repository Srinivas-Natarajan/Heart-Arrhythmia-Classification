# Heart-Arrhythmia-Classification

---

<br>

## Instructions to run
1. #### Note down the location of the ".edf" file and enter it into the cmd line.
2. #### Use the command where 
   * PATH_TO_EDF_FILE - Location of your EDF file
   * SAVE_FILE_NAME - Name of the text and npy file which will be generated
   * MODEL_NUMBER - 
      * 0 - Model from the paper
      * 1 - Simplified CNN model

```python
   python predict.py PATH_TO_EDF_FILE SAVE_FILE_NAME MODEL_NUMBER
```

<br>

For example, the command below will generate a file called "ECG_100.txt" which will contain the classifications

```python
    python predict.py ./files/100.edf ECG_100 
```

---

<br>

## Dataset
The original datasets used are the <a href="https://www.physionet.org/content/mitdb/1.0.0/">MIT-BIH Arrhythmia Dataset</a> and that are preprocessed based on the methodology described in the paper below in order to end up with samples of a single heartbeat each and normalized amplitudes.

> Kachuee, M., Fazeli, S., & Sarrafzadeh, M. (2018). ECG Heartbeat Classification: A Deep Transferable Representation. 2018 IEEE International Conference on Healthcare Informatics (ICHI). https://doi.org/10.1109/ichi.2018.00092 (https://arxiv.org/pdf/1805.00794.pdf)

<br>

### The process followed is:

1. Splitting the continuous ECG signal to 10s windows and select a 10s window from an ECG signal. <br>
2. Normalizing the amplitude values to the range of between zero and one. <br>
3. Finding the set of all local maximums based on zerocrossings of the first derivative. <br>
4. Finding the set of ECG R-peak candidates by applying a threshold of 0.9 on the normalized value of the local maximums. <br>
5. Finding the median of R-R time intervals as the nominal heartbeat period of that window (T). <br>
6. For each R-peak, selecting a signal part with the length equal to 1.2T. <br>
7. Padding each selected part with zeros to make its length equal to a predefined fixed length. <br>

<br>

MIT-BIH Arrhythmia dataset :

* Number of Categories: 5
* Number of Samples: 109446
* Sampling Frequency: 125Hz
* Data Source: Physionet’s MIT-BIH Arrhythmia Dataset
* Classes: [’N’: 0, ‘S’: 1, ‘V’: 2, ‘F’: 3, ‘Q’: 4]

<br>

### Class distribution in the dataset

---

* Before Resampling
<img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/distribution_before_resample.png" height=400>

<br>

* After Resampling
<img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/distribution_after_resample.png" height=400>

---

<br> <br>

## Model and Results

<br>

### A. Paper based model

<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/paper%20model/model_plot.png" style="height: 500;"> <br>
  <b>Figure 1:</b> Model Structure
</p>

<br>
<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/paper%20model/model_result_plot.png"> <br>
  <b>Figure 2:</b> Accuracy and Loss Plot
</p>

<br> <br>

<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/paper%20model/confusion_matrix.png"> <br>
  <b>Figure 3:</b> Confusion Matrix
</p>

<br> <br>

<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/paper%20model/classification_report.png"> <br>
  <b>Figure 4:</b> Classification Report
</p>

<br> <br>

<br>

### B. Simplified model

---

<br>

<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/simplified%20model/simple_model_plot.png"> <br>
  <b>Figure 5:</b> Simplified Model Structure
</p>

<br>
<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/simplified%20model/simple_model_result_plot.png" style="height: 700;"> <br>
  <b>Figure 6:</b> Accuracy and Loss Plot
</p>

<br> <br>

<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/simplified%20model/confusion_matrix_simple_model.png"> <br>
  <b>Figure 7:</b> Confusion Matrix
</p>

<br> <br>

<p align="center">
  <img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/simplified%20model/classification_report_simple_model.png"> <br>
  <b>Figure 8:</b> Classification Report
</p>

<br> <br>

