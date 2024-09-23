import numpy as np
import scipy.signal as signal

np.random.seed(42);

base_pm25=np.random.normal(loc=50,scale=20,size=1440)

rush_hours=[420,480,1080,1140]

for rh in rush_hours:
    base_pm25[rh:rh+60]+=np.random.normal(loc=30,scale=10,size=60)

sensor_noise=np.random.normal(loc=0,scale=5,size=1440)
base_pm25+=sensor_noise

signal_error=np.random.normal(loc=0,scale=2,size=1440)
base_pm25+=signal_error

pollution_data=np.clip(base_pm25,0, None);

print(pollution_data[:10])

def lowpassfilter(data,cutoff_freq,sampling_rate,order=2):
    nyquist=0.5*sampling_rate
    normal_cutoff=cutoff_freq/nyquist
    b,a=signal.butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data=signal.filtfilt(b,a,data)
    return filtered_data

sampling_rate=1
cutoff_frequency=0.01

filtered_pollution_data=lowpassfilter(pollution_data, cutoff_frequency, sampling_rate)

print(filtered_pollution_data[:10])
