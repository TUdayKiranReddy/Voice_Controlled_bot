import numpy as np
import soundfile as sf
# ~ new_data = np.empty([25000,]) #creating an empty array for new file to be generated from original file
# ~ y1 = np.empty([25000,])
for j in range(1,81):
	b= "stop"+str(j)+".wav"
	data, samplerate = sf.read(b) #reading audio file using soundfile library
	print (len(data), samplerate)
	new_data = np.empty([len(data)+25,])
	y1 = np.empty([len(data)+25],)
	x= len(data)
	p = 25
	for y in range(1 ,p):   
		for i in range(0,y-1):      #adding empty elements in the array in the start
			new_data[i] =y1[i]
		for i in range(y,len(data)+25-x+y-1):
			new_data[i] =data[i-y]
		for i in range(len(data)+25-y , len(data)+25-1):    #adding empty elements in the array in the end 
			new_data[i] = y1[i]	
		a = "stop__"+str(j) +"_"+str(y)+".wav"    #total length becomes 25000
		sf.write(a, new_data, samplerate)  #audio files are written back to harddisk
		print (len(new_data))
 
