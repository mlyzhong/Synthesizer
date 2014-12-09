from lasp.sound import *


sine_wave = generate_sine_wave(3, 3000, 44100)

stack = generate_simple_stack(1, 440, 44100)

wf = WavFile()
wf.sample_rate = 44100
wf.data = stack
wf.log_spectrogram = False



wf.plot(min_freq=300, max_freq=3000)

plt.show()

wf.to_wav("test_1.wav", normalize = True)


