import os

path = 'noiseFirstStart8p8nSeries16Sources/'

files = os.listdir(path)
filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
label = {"a":0.1, "b":0.2,"c":0.3,"d":0.4,"e":0.5,"f":0.6,"g":0.7,"h":0.8,"i":0.9,"j":1.0,"k":1.1,"l":1.2,"m":1.3,
		 "n":1.4,"o":1.5,"p":1.6 ,"q":1.7 ,"r":1.8 }
std_dev = 0.1
voltage = 0.2

x = []
y = []
colors = []
for name_o_file in files:
	f = open(path+name_o_file,"r")
	lab = name_o_file.split(".")[0][-1]
	found = False
	for line in f:
		if line.startswith("responsetime"):
			fVal = line.split()[2]
			fValFloat = float(fVal)
			ns = fValFloat*1000000000
			x.append(ns)
			colors.append('black')
			y.append(label[lab])
			found = True
        
	if (not found):
		x.append(0)
		colors.append('red')
		y.append(label[lab])
print(x)
print(y)
	
import matplotlib.pyplot as plt

plt.scatter(x, y,c=colors)
plt.ylabel("White Noise Std Dev from 0.1V")
plt.xlabel("Time to first event (ns)")
plt.show()