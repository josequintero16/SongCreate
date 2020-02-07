import numpy as np
import soundfile as sf

def freq(a):
    return 440*2**((a-49)/12)

i=0
tnotes = int(input("Enter total notes: "))
song = np.zeros((4000 * tnotes),)
x=np.arange(0,.5,(1/8000))

while i < tnotes:
    note = int(input("Enter note: "))
    f = freq(note)
    song[i*4000:(i+1)*4000]=np.cos(2*np.pi*f*x)
    i+=1

sf.write('mySong.wav',song,8000)
