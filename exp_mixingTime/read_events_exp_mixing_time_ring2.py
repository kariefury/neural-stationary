import os
import numpy as np

paths = ['ring2/']#,'ring2phase/']
crosses = ['Cross 1', 'Cross 2', 'Cross 3', 'Cross 4']
clab = ['red', 'green', 'blue', 'black']#['black','blue','gray','red']


filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
label = {"a":0.1, "b":0.2,"c":0.3,"d":0.4,"e":0.5,"f":0.6,"g":0.7,"h":0.8,"i":0.9,"j":1.0,"k":1.1,"l":1.2,"m":1.3,
		 "n":1.4,"o":1.5,"p":1.6 ,"q":1.7 ,"r":1.8 }

x_responsetimea = []
y_responsetimea = []
colors = []
i = 0
for p in paths:
	j = 0
	while j < 4:
		x_responsetimea.append([])
		y_responsetimea.append([])
		colors.append([])
		j += 1
	path = paths[i]
	files = os.listdir(path)

	for name_o_file in files:
		f = open(path+name_o_file,"r")
		lab = name_o_file.split(".")[0][-1]
		found = False
		cross_count_a = 1
		cross_count_b = 1
		for line in f:
			if line.startswith("responsetimea"):
				fVal = line.split()[2]
				fValFloat = float(fVal)
				if cross_count_a <= 4:
					ns = fValFloat * 1000000000.0
					print(name_o_file, ns, cross_count_a)
					x_responsetimea[cross_count_a-1].append(ns)
					y_responsetimea[cross_count_a-1].append(label[lab])
					colors[cross_count_a-1].append(clab[cross_count_a-1])
				cross_count_a += 1
	i += 1

import matplotlib.pyplot as plt

i = 3

#'black','blue','green','yellow','magenta','cyan','grey'
line_choices= ['-r','-g','-b','-k']#['-k','-b','-g','-y','m--','c--','g--']
while i > -1:
	# fit least-squares with an intercept
	print(i)
	ynp = np.zeros(len(x_responsetimea[i]))
	print (ynp.shape,'ynp')
	xnp = np.zeros(len(x_responsetimea[i]))
	m = 0
	for isa in y_responsetimea[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimea[i]:
		xnp[m] = isa
		m += 1
	# print(xnp.shape,'xnp')
	# #print(len(x[i]),len(yc))
	# #print(yc,x[i])
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25)
	plt.xlim(0, 2)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_cross1through4_2ns.png', dpi=dpi)
plt.close()
i = 3
while i > -1:
	# fit least-squares with an intercept
	print(i)
	ynp = np.zeros(len(x_responsetimea[i]))
	print (ynp.shape,'ynp')
	xnp = np.zeros(len(x_responsetimea[i]))
	m = 0
	for isa in y_responsetimea[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimea[i]:
		xnp[m] = isa
		m += 1
	# print(xnp.shape,'xnp')
	# #print(len(x[i]),len(yc))
	# #print(yc,x[i])
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25)
	plt.xlim(0, 10)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_10ns.png', dpi=dpi)
plt.close()
i = 3
while i > -1:
	# fit least-squares with an intercept
	print(i)
	ynp = np.zeros(len(x_responsetimea[i]))
	print (ynp.shape,'ynp')
	xnp = np.zeros(len(x_responsetimea[i]))
	m = 0
	for isa in y_responsetimea[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimea[i]:
		xnp[m] = isa
		m += 1
	# print(xnp.shape,'xnp')
	# #print(len(x[i]),len(yc))
	# #print(yc,x[i])
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25)
	plt.xlim(0, 20)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_20ns.png', dpi=dpi)
plt.close()
i = 3
while i > -1:
	# fit least-squares with an intercept
	print(i)
	ynp = np.zeros(len(x_responsetimea[i]))
	print (ynp.shape,'ynp')
	xnp = np.zeros(len(x_responsetimea[i]))
	m = 0
	for isa in y_responsetimea[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimea[i]:
		xnp[m] = isa
		m += 1
	# print(xnp.shape,'xnp')
	# #print(len(x[i]),len(yc))
	# #print(yc,x[i])
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25)
	plt.xlim(2, 10)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_2to10ns.png', dpi=dpi)
plt.close()
i = 3
while i > -1:
	# fit least-squares with an intercept
	print(i)
	ynp = np.zeros(len(x_responsetimea[i]))
	print (ynp.shape,'ynp')
	xnp = np.zeros(len(x_responsetimea[i]))
	m = 0
	for isa in y_responsetimea[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimea[i]:
		xnp[m] = isa
		m += 1
	# print(xnp.shape,'xnp')
	# #print(len(x[i]),len(yc))
	# #print(yc,x[i])
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25)
	plt.xlim(10, 20)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_10to20ns.png', dpi=dpi)