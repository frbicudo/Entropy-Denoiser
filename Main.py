import librosa
import EntropyDenoiser
import matplotlib.pyplot as plt
import numpy as np


# Audio file path
fileName = "Whistle.wav"

target_sr = 94000

# Spectrogram Parameters
mel_bins = 256
hop = 736
fft = 2048
# Frequency range
fmin = 4000
fmax = 44000

# open file
audio, sr = librosa.load(fileName, sr=target_sr)

# fourier transform into matrix
matrix = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=mel_bins, hop_length=hop, n_fft=fft,
                                        fmin=fmin,
                                        fmax=fmax)

print(matrix.shape)
# apply entropy denoiser
filtered_matrix = EntropyDenoiser.denoise(matrix)

# apply log scale to original matrix
matrix = np.log10(matrix)

# Display the original spectrogram
plt.figure()
img = librosa.display.specshow(matrix, x_axis='time', y_axis='mel', sr=sr,
                               hop_length=hop, shading="gouraud", cmap='viridis')
plt.title("Original")
plt.show()

# Display the filtered spectrogram
plt.figure()
img = librosa.display.specshow(filtered_matrix, x_axis='time', y_axis='mel', sr=sr,
                               hop_length=hop, shading="gouraud", cmap='viridis')
plt.title("Filtered")
plt.show()
