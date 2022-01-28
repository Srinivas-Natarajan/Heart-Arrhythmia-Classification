# Heart-Arrhythmia-Classification

---

## Dataset
The original datasets used are the MIT-BIH Arrhythmia Dataset and The PTB Diagnostic ECG Database that were preprocessed based on the methodology described in the paper below in order to end up with samples of a single heartbeat each and normalized amplitudes.

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

## Model

<img src="https://github.com/Srinivas-Natarajan/Heart-Arrhythmia-Classification/blob/main/images/model_plot.png">
