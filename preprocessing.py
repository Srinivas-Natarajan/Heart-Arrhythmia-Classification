import numpy as np
import pandas as pd
import wfdb as wf
from scipy import signal
from biosppy.signals import ecg


def edftocsv(edf_file_path, csv_name):
    """
        Input:
            edf_file_path - Path to the EDF file to convert. (e.g. "./100.edf")
            csv_name - Name of the CSV file which will be created
        Output:
            CSV file containing the processes ECG data in 188 columns
    """
    edf_record = wf.edf2mit(edf_file_path)
    record = edf_record.p_signal
    data = record.transpose()

    for channelid, channel in enumerate(data):

        out = ecg.ecg(signal=channel, sampling_rate=360, show=False)
        rpeaks = np.zeros_like(channel, dtype='float')
        rpeaks[out['rpeaks']] = 1.0

        beatstoremove = np.array([0])
        beats = np.split(channel, out['rpeaks'])

        #(index,val) pairs of rpeak locations
        for idx, idxval in enumerate(out['rpeaks']): 
            firstround = idx == 0
            lastround = idx == len(beats) - 1

            # Skip first and last beat.
            if (firstround or lastround):
                continue

            # Get the classification value that is on
            # or near the position of the rpeak index.
            fromidx = 0 if idxval < 10 else idxval - 10
            toidx = idxval + 10

            # Append some extra readings from next beat.
            beats[idx] = np.append(beats[idx], beats[idx+1][:40])

            # Normalize the readings to a 0-1 range for ML purposes.
            beats[idx] = (beats[idx] - beats[idx].min()) / beats[idx].ptp()

            # Resample from 360Hz to 125Hz
            newsize = int((beats[idx].size * 125 / 360) + 0.5)
            beats[idx] = signal.resample(beats[idx], newsize)

            # Skipping records that are too long.
            if (beats[idx].size > 187):
                beatstoremove = np.append(beatstoremove, idx)
                continue

            # Pad with zeroes.
            zerocount = 187 - beats[idx].size
            beats[idx] = np.pad(beats[idx], (0, zerocount), 'constant', constant_values=(0.0, 0.0))

            # Append the classification to the beat data.
            beats[idx] = np.append(beats[idx], 0)
        
    beatstoremove = np.append(beatstoremove, len(beats)-1) #Removing unnecessary beats
    beats = np.delete(beats, beatstoremove) # Remove first and last beats and the ones without classification.
    savedata = np.array(list(beats[:]), dtype=np.float)
    outfn = './files/' + csv_name + '.csv'
    with open(outfn, "wb") as fin:
        np.savetxt(fin, savedata, delimiter=",", fmt='%f')
    
    return pd.read_csv('./files/' + csv_name + '.csv', header=None)
