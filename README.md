
# Entropy Denoising Method Showcase

This code is a python implementation of the entropy denoising method proposed in the paper: Unveiling Cetacean Voices: Entropy-Powered Spectrogram Denoising for Deep Learning Applications.


![image](https://github.com/user-attachments/assets/7a17e894-4a2f-4825-b956-5542a23af16f)



The main.py file shows both an original and denoised spectrogram taken from whistle.wav.
The fileName variable can be changed to try diferent audio files.


EntropyDenoiser.py has the main method implementation.
The method can be called with the 'denoise' function.
It receives a spectrogram magnitude matrix and returns a denoised version of that matrix.
The following optional arguments can be used:

- window_height, window_width: Define the size of the window used by the method (default = 16).
- entropy_threshold: Define the entropy threshold that affects the denoising sensitivity (default = 0.85)
- magnitude_threshold: Define the magnitude threshold that affects the cleaning effect (should be a value betwen 0 and 1, default = 0.2)
- output:  String that defines the output type. If '' does not change the values. If 'original' convert the preserved data into its original magnitude values. If 'mask' returns a binary mask where empty is indicated by 0 and data is indicated by 1. If 'entropy' will show the entropy values for each window (default = '').

The whistle audio sample provided is from the [Watkins Marine Mammal Sound Database](https://whoicf2.whoi.edu/science/B/whalesounds/bestOf.cfm?code=BD15C)




## Example

```python
denoised matrix = denoise(matrix)
or
denoised matrix = denoise(matrix, output="original", window_height=32, window_width=32, entropy_threshold=0.95, magnitude_threshold=0.35)
```

