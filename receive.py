import socket
import numpy as np
import scipy


localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
seconds = .1
samplerate = 44100
window_size = samplerate*seconds
logbase = 2
bands = 10

# frequency bands for visualizer
bounds = [int(window_size/2)]
for i in range(bands-1):
	bounds.insert(0,int(np.ceil(bounds[0]/logbase)))
bounds.insert(0,0)
# print(bounds)


audio = []

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

while(True):

	# takes audio string sent by client and puts it in audio list
	bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
	audio.append(float(bytesAddressPair[0]))

	# when there are enough samples to do an FFT, perform the FFT
	if(len(audio) == samplerate*seconds):
		audioarray = np.array(audio)
		freq = scipy.fft(audio)
		freq = abs(freq)
		N = len(freq)
		freqsmall = []

		# spaces out equalizer
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

		# prints frequency bands
		for i in range(bands):
			freqsmall.append(10*np.log10(np.average(freq[bounds[i]:bounds[i+1]])))
			pr = ""
			for j in range(np.ceil(freqsmall[i]).astype(int)):
				pr += '='
			print('{:6d}'.format(int(np.ceil(bounds[i+1]/seconds))) + "hz:" + pr)
		

		audio = []
		
	
UDPServerSocket.close()
