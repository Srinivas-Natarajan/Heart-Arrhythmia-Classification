# Heart-Arrhythmia-Classification

---

## Dataset
The original datasets used are the <a href="https://www.physionet.org/content/mitdb/1.0.0/">MIT-BIH Arrhythmia Dataset</a> and that are preprocessed based on the methodology described in the paper below in order to end up with samples of a single heartbeat each and normalized amplitudes.

> Kachuee, M., Fazeli, S., & Sarrafzadeh, M. (2018). ECG Heartbeat Classification: A Deep Transferable Representation. 2018 IEEE International Conference on Healthcare Informatics (ICHI). https://doi.org/10.1109/ichi.2018.00092 (https://arxiv.org/pdf/1805.00794.pdf)

### The process followed is:

1. Splitting the continuous ECG signal to 10s windows and select a 10s window from an ECG signal. <br>
2. Normalizing the amplitude values to the range of between zero and one. <br>
3. Finding the set of all local maximums based on zerocrossings of the first derivative. <br>
4. Finding the set of ECG R-peak candidates by applying a threshold of 0.9 on the normalized value of the local maximums. <br>
5. Finding the median of R-R time intervals as the nominal heartbeat period of that window (T). <br>
6. For each R-peak, selecting a signal part with the length equal to 1.2T. <br>
7. Padding each selected part with zeros to make its length equal to a predefined fixed length. <br>

MIT-BIH Arrhythmia dataset :

* Number of Categories: 5
* Number of Samples: 109446
* Sampling Frequency: 125Hz
* Data Source: Physionet’s MIT-BIH Arrhythmia Dataset
* Classes: [’N’: 0, ‘S’: 1, ‘V’: 2, ‘F’: 3, ‘Q’: 4]

<br>

### Class distribution in the dataset

* Before Resampling
<img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/distribution_before_resample.png" height=500>

* After Resampling
<img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/distribution_after_resample.png">

<br>

## Model

![](https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/model_plot.png) <br>
Figure 1: Model Structure

<br>

## Results

* **Accuracy:** 73%

<br>

![](https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/model_result_plot.png) 
<p align="center">Figure 2: Accuracy and Loss Plot</p>

<br> <br>

![](https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/confusion_matrix.png)
<p align="center">Figure 3: Confusion Matrix</p>

<br> <br>

![](https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/classification_report.png)
<p align="center">Figure 4: Classification Report</p>

<br> <br>
