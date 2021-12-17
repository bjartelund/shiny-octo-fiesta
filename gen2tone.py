#!/usr/bin/python
from struct import pack
from math import pi,sin
toner = {"a":440,"t":550,"c":500,"g":625}
def gen2tone(gen=[
"caggaccccaccccccggcgcgacccgatgcacgagctgatttcgaccatcctctcgcagt",
"------------------cgcgacccgatgcacgagctg----------------------"],
volume=0.1):
	duration = len(gen[0]) * 2000
	print duration
	fil = open("test.au","w")
	fil.write(".snd" + pack(">5L",24,8*duration,2,8000,1))
	counter = 0
	print len(gen[0])
	print duration/len(gen[0])*8
	while len(gen[0]) > counter:
		koder = [x[counter] for x in gen]
		for i in range(duration/len(gen[0])):
			sin_i = sum([sin(i*2*pi*toner[x]/8000) for x in koder if x in toner.keys()])
			fil.write(pack("b",volume*127*sin_i))
		counter+=1
	fil.close()


