#each note is a fourth of a second

import numpy as np
import soundfile as sf

def freq(a):
    return 440*2**((a-49)/12)

i=0
tnotes = int(input("Enter total notes: "))
song = np.zeros((2000 * tnotes),)
x=np.arange(0,.5,(1/4000))

while i < tnotes:
    note = int(input("Enter note: "))
    f = freq(note)
    song[i*2000:(i+1)*2000]=np.cos(2*np.pi*f*x)
    i+=1

sf.write('mySong.wav',song,8000)
