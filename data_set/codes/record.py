# import the needed libraries
import pyaudio
import wave
import numpy as np
#from matplotlib import pyplot as plt
import random
import soundfile as sf
from python_speech_features import mfcc

fel = "forward"
fle = fel + "/"+fel
CHUNK = 1024 
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 1
RATE = 8000 #sample rate
RECORD_SECONDS = 2
#k=1
for j in range(1,81):
	WAVE_OUTPUT_FILENAME = fle+str(j)+".wav"
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK) #buffer
	print("* recording")
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data) # 2 bytes(16 bits) per channel
	print("* done recording")
	stream.stop_stream()
	stream.close()
	p.terminate()
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	
	# ~ b= "back/back"+str(k)+".wav"
	# ~ data, samplerate = sf.read(b) #reading audio file using soundfile library
	# ~ print (len(data), samplerate)
	# ~ p = len(data) + 25
	# ~ new_data = np.empty([p,])
	# ~ y1 = np.empty([p],)	

	# ~ x= len(data)
	
	# ~ for y in range(1 ,25):   
		# ~ for i in range(0,y-1):      #adding empty elements in the array in the start
			# ~ new_data[i] =y1[i]
		# ~ for i in range(y,p-x+y-1):
			# ~ new_data[i] =data[i-y]
		# ~ for i in range(p-x+y , p-1):    #adding empty elements in the array in the end 
			# ~ new_data[i] = y1[i]	
		# ~ a = "back/back"+str(k+y)+".wav"    #total length becomes 25000
		# ~ sf.write(a, new_data, samplerate)  #audio files are written back to harddisk
	print(j)
	input()
	#k = k +25
	
