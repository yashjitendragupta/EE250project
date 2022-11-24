import socket
import soundfile as sf
import numpy
from datetime import datetime, timedelta
from playsound import playsound
import time
import sounddevice as sd

seconds = .1
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 32
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
data, samplerate = sf.read('$10 Pizza.wav')
data = (data[:,0] + data[:,1])/2
start = datetime.now()
# playsound('$10 Pizza.wav',False)


for i in range(len(data)):
	bytesToSend = str.encode(str(data[i].item()))
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	sd.play(data[i],44100)
	if(i % (seconds*44100) == 0):
		runtime = datetime.now() - start
		time.sleep(seconds - runtime.total_seconds())
		start = datetime.now()




