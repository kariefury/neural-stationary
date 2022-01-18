import os
import numpy as np

paths = ['noiseFirstStart/','noiseFirstStart1p3nSeries/','noiseFirstStart1p4nSeries/',
		 'noiseFirstStart1p4nSeries2Sources/',\
		'noiseFirstStart1p7nSeries8Sources/','noiseFirstStart5p7nSeries12Sources/',
		 'noiseFirstStart8p8nSeries16Sources/']

flabels = ['1n','1p3n','1p4n','1p4n','1p7n','5p7n','8p8n']
clab = ['black','blue','green','yellow','magenta','cyan','grey']


filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
label = {"a":0.1, "b":0.2,"c":0.3,"d":0.4,"e":0.5,"f":0.6,"g":0.7,"h":0.8,"i":0.9,"j":1.0,"k":1.1,"l":1.2,"m":1.3,
		 "n":1.4,"o":1.5,"p":1.6 ,"q":1.7 ,"r":1.8 }
dpi = 300
x = []
y = []
colors = []
i = 0
for p in paths:
	x.append([])
	y.append([])
	colors.append([])
	path = paths[i]
	files = os.listdir(path)
	files = os.listdir(path)
	std_dev = 0.1
	voltage = 0.2

	for name_o_file in files:
		f = open(path+name_o_file,"r")
		lab = name_o_file.split(".")[0][-1]
		found = False
		for line in f:
			if line.startswith("responsetime"):
				fVal = line.split()[2]
				fValFloat = float(fVal)
				ns = fValFloat*1000000000
				x[i].append(ns)
				y[i].append(label[lab])
				colors[i].append(clab[i])
				found = True
#		if (not found):
			#x[i].append(0)
			#colors[i].append('#0f0f0f00')
			#y[i].append(label[lab])
	print(x)
	print(y)
	i += 1
	
import matplotlib.pyplot as plt

i = 0

#'black','blue','green','yellow','magenta','cyan','grey'
plt.figure(figsize=(8, 5))
line_choices=['-k','-b','-g','-y','m--','c--','g--']
for each in paths:
	# fit least-squares with an intercept
	ynp = np.zeros(len(x[i]))
	print (ynp.shape,'ynp')
	xnp = np.zeros(len(x[i]))
	m = 0
	for isa in y[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x[i]:
		xnp[m] = isa
		m += 1
	# print(xnp.shape,'xnp')
	# #print(len(x[i]),len(yc))
	# #print(yc,x[i])
	plt.scatter(xnp, ynp, c=colors[i], label=flabels[i])
	# hs = np.hstack((xnp, ynp))
	# print(hs.shape,ynp.shape)
	# res = np.linalg.lstsq(hs, ynp)
	# 
	# print(res)
	# w = res[0]
	# 
	# xx = np.linspace(*plt.gca().get_xlim()).T
	xj = xnp
	yj = ynp
	plt.ylim(0.0,1.9)
	plt.plot(np.unique(xj), np.poly1d(np.polyfit(xj, yj, 1))(np.unique(xj)),line_choices[i])
	plt.legend()
	
	i += 1

plt.ylabel("White Noise Std Dev from 0.1V")
plt.xlabel("Time to first event (ns)")
plt.savefig('../multiple_sources.png', dpi=dpi)
plt.close()