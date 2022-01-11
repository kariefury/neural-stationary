import os
import numpy as np
import statistics
import matplotlib.pyplot as plt

paths = ['ring2/']#,'ring2phase/']
crosses = ['Cross 1', 'Cross 2', 'Cross 3', 'Cross 4']
crossesMarker = ["2", "3", "1", "4"]
clab = ['black', 'green', 'black', 'blue']#['black','blue','gray','red']


filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
label = {"a":0.1, "b":0.2,"c":0.3,"d":0.4,"e":0.5,"f":0.6,"g":0.7,"h":0.8,"i":0.9,"j":1.0,"k":1.1,"l":1.2,"m":1.3,
		 "n":1.4,"o":1.5}
label_to_index = { "0.2": 0, "0.3": 1, "0.4": 2, "0.5": 3, "0.6": 4, "0.7": 5, "0.8": 6, "0.9": 7, "1.0": 8,
					"1.1":9, "1.2":10,"1.3": 11, "1.4": 12, "1.5": 13}
datapoints = 14

x_responsetimea = []
y_responsetimea = []

x_responsetimeb = []
y_responsetimeb = []
colors = []
colorsb = []

tap_a_x_values_avg = [[], [], [], []]
tap_b_x_values_avg = [[], [], [], []]
tap_a_x_values = [[], [], [], []]
tap_b_x_values = [[], [], [], []]
tap_a_y_values = [[], [], [], []]
tap_b_y_values = [[], [], [], []]
tap_a_x_sample_count = [[], [], [], []]
tap_b_x_sample_count = [[], [], [], []]
tap_a_x_err = [[], [], [], []]
tap_b_x_err = [[], [], [], []]
tap_a_x_err_std_dev = [[], [], [], []]
tap_b_x_err_std_dev = [[], [], [], []]
i = 3
while i >= 0:
	j = 0
	while j < datapoints:
		tap_a_x_values_avg[i].append(0.0)
		tap_b_x_values_avg[i].append(0.0)
		tap_a_x_values[i].append(0.0)
		tap_b_x_values[i].append(0.0)
		tap_a_y_values[i].append(0.0)
		tap_b_y_values[i].append(0.0)
		tap_a_x_sample_count[i].append(0.0)
		tap_b_x_sample_count[i].append(0.0)
		tap_a_x_err[i].append([])
		tap_b_x_err[i].append([])
		j += 1
	i = i - 1


i = 0
for p in paths:
	j = 0
	while j < 4:
		# response time a
		x_responsetimea.append([])
		y_responsetimea.append([])
		# response time b
		x_responsetimeb.append([])
		y_responsetimeb.append([])
		colors.append([])
		colorsb.append([])
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
			if line.startswith("responsetimeb"):
				fVal = line.split()[2]
				fValFloat = float(fVal)
				if cross_count_b <= 4:
					ns = fValFloat * 1000000000.0
					print(name_o_file, ns, cross_count_b)
					x_responsetimeb[cross_count_b-1].append(ns)
					y_responsetimeb[cross_count_b-1].append(label[lab])
					colorsb[cross_count_b-1].append(clab[cross_count_b-1])
				cross_count_b += 1
	i += 1


i = 3

line_choices= ['-r','-g','-b','-k']#['-k','-b','-g','-y','m--','c--','g--']
while i > -1:
	ynp = np.zeros(len(x_responsetimea[i]))
	xnp = np.zeros(len(x_responsetimea[i]))
	m = 0
	for isa in y_responsetimea[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimea[i]:
		xnp[m] = isa
		m += 1
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(0, 2)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_cross1through4_2ns.png', dpi=dpi)
plt.close()

# Average Response Time for Response A and B with Cross 1, 2, 3,4 for each
i = 3
line_choices = ['-r', '-g', '-b', '-k']  # ['-k','-b','-g','-y','m--','c--','g--']
while i > -1:
	ynp = np.zeros(len(x_responsetimea[i]))
	xnp = np.zeros(len(x_responsetimea[i]))
	m = 0
	for isa in y_responsetimea[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimea[i]:
		xnp[m] = isa
		tap_a_x_err[i][label_to_index[str(y_responsetimea[i][m])]].append(isa)
		m += 1
	
	j = 0
	while j < len(x_responsetimea[i]):
		print(j)
		voltage = y_responsetimea[i][j]
		print(voltage)
		tap_a_y_values[i][label_to_index[str(voltage)]] += y_responsetimea[i][j]
		tap_a_x_values[i][label_to_index[str(voltage)]] += x_responsetimea[i][j]
		tap_a_x_sample_count[i][label_to_index[str(voltage)]] += 1
		j += 1
	j = 0
	for total in tap_a_x_values[i]:
		if( tap_a_x_sample_count[i][j] > 0.0):
			tap_a_x_values_avg[i][j] = total / tap_a_x_sample_count[i][j]
		j += 1
	j = 0
	for total in tap_a_y_values[i]:
		if (tap_a_x_sample_count[i][j] > 0.0):
			tap_a_y_values[i][j] = total / tap_a_x_sample_count[i][j]
		j += 1
	
	j = 0
	while j < len(x_responsetimeb[i]):
		voltage = y_responsetimeb[i][j]
		tap_b_y_values[i][label_to_index[str(voltage)]] += y_responsetimeb[i][j]
		tap_b_x_values[i][label_to_index[str(voltage)]] += x_responsetimeb[i][j]
		tap_b_x_sample_count[i][label_to_index[str(voltage)]] += 1
		j += 1
	j = 0
	for total in tap_b_x_values[i]:
		if( tap_b_x_sample_count[i][j] > 0.0):
			tap_b_x_values_avg[i][j] = total / tap_b_x_sample_count[i][j]
		j += 1
	i -= 1

i = 0
j = 0
while i < 4:
	j = 0
	while j < datapoints:
		if (len(tap_a_x_err[i][j]) > 1):
			tap_a_x_err_std_dev[i].append(statistics.stdev(tap_a_x_err[i][j]))
		else:
			tap_a_x_err_std_dev[i].append(0.0)
		j += 1
	i += 1

i = 0
while i < 4:
	plt.scatter(tap_a_x_values_avg[i], tap_a_y_values[i],alpha=0.5,marker=crossesMarker[i],s=80)
	plt.errorbar(tap_a_x_values_avg[i], tap_a_y_values[i],label=crosses[i], xerr=tap_a_x_err_std_dev[i], \
																				 fmt=crossesMarker[i])
	i += 1
#plt.scatter(tap_b_x_values_avg, tap_b_y_values)
plt.xlim(0, 2)
plt.ylim(0,1.7)
plt.legend()
plt.ylabel("White Noise Std Dev from 0.1V")
plt.xlabel("Time to cross 1.2V event (ns)")
dpi = 300
plt.savefig('../exp_mixing_time_averages.png', dpi=dpi)
plt.close()

# Avg Response time B with error bars
i = 3
line_choices= ['-r','-g','-b','-k']
while i > -1:
	ynpb = np.zeros(len(x_responsetimeb[i]))
	xnpb = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynpb[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnpb[m] = isa
		tap_b_x_err[i][label_to_index[str(y_responsetimeb[i][m])]].append(isa)
		m += 1
	
	j = 0
	while j < len(x_responsetimeb[i]):
		voltage = y_responsetimeb[i][j]
		tap_b_y_values[i][label_to_index[str(voltage)]] += y_responsetimeb[i][j]
		tap_b_x_values[i][label_to_index[str(voltage)]] += x_responsetimeb[i][j]
		tap_b_x_sample_count[i][label_to_index[str(voltage)]] += 1
		j += 1
	j = 0
	for total in tap_b_x_values[i]:
		if( tap_b_x_sample_count[i][j] > 0.0):
			tap_b_x_values_avg[i][j] = total / tap_b_x_sample_count[i][j]
		j += 1
	j = 0
	for total in tap_b_y_values[i]:
		if (tap_b_x_sample_count[i][j] > 0.0):
			tap_b_y_values[i][j] = total / tap_b_x_sample_count[i][j]
		j += 1
	i -= 1

i = 0
j = 0
while i < 4:
	j = 0
	while j < datapoints:
		if (len(tap_b_x_err[i][j]) > 1):
			tap_b_x_err_std_dev[i].append(statistics.stdev(tap_b_x_err[i][j]))
		else:
			tap_b_x_err_std_dev[i].append(0.0)
		j += 1
	i += 1

i = 0
while i < 4:
	plt.scatter(tap_b_x_values_avg[i], tap_b_y_values[i],alpha=0.5,marker=crossesMarker[i],s=80)
	plt.errorbar(tap_b_x_values_avg[i], tap_b_y_values[i],label=crosses[i], xerr=tap_b_x_err_std_dev[i], \
																				 fmt=crossesMarker[i])
	i += 1
#plt.scatter(tap_b_x_values_avg, tap_b_y_values)
plt.xlim(0, 2)
plt.ylim(0,1.7)
plt.legend()
plt.ylabel("White Noise Std Dev from 0.1V")
plt.xlabel("Time to cross 1.2V event (ns)")
dpi = 300
plt.savefig('../exp_mixing_time_averages_ResB.png', dpi=dpi)
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
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(0, 10)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_10ns.png', dpi=dpi)
plt.close()


i = 3
line_choices= ['-r','-g','-b','-k']
while i > -1:
	ynpb = np.zeros(len(x_responsetimeb[i]))
	xnpb = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynpb[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnpb[m] = isa
		m += 1
	plt.scatter(xnpb, ynpb, c=colorsb[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(0, 2)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_ResB_cross1through4_2ns.png', dpi=dpi)
plt.close()


i = 3
line_choices= ['-r','-g','-b','-k']
while i > -1:
	ynpb = np.zeros(len(x_responsetimeb[i]))
	xnpb = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynpb[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnpb[m] = isa
		m += 1
	plt.scatter(xnpb, ynpb, c=colorsb[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(0, 10)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_ResB_cross1through4_10ns.png', dpi=dpi)
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
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(0, 20)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_20ns.png', dpi=dpi)
plt.close()

i = 3
line_choices= ['-r','-g','-b','-k']
while i > -1:
	ynpb = np.zeros(len(x_responsetimeb[i]))
	xnpb = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynpb[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnpb[m] = isa
		m += 1
	plt.scatter(xnpb, ynpb, c=colorsb[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(0, 20)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_ResB_cross1through4_20ns.png', dpi=dpi)
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
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	plt.xlim(2, 10)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_2to10ns.png', dpi=dpi)
plt.close()

i = 3
line_choices= ['-r','-g','-b','-k']
while i > -1:
	ynpb = np.zeros(len(x_responsetimeb[i]))
	xnpb = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynpb[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnpb[m] = isa
		m += 1
	plt.scatter(xnpb, ynpb, c=colorsb[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(2, 10)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_ResB_cross1through4_2to10ns.png', dpi=dpi)
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
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	plt.xlim(10, 20)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4_10to20ns.png', dpi=dpi)
plt.close()

i = 3
line_choices= ['-r','-g','-b','-k']
while i > -1:
	ynpb = np.zeros(len(x_responsetimeb[i]))
	xnpb = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynpb[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnpb[m] = isa
		m += 1
	plt.scatter(xnpb, ynpb, c=colorsb[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.xlim(10, 20)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_ResB_cross1through4_10to20ns.png', dpi=dpi)
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
	plt.scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	#plt.xlim(10, 20)
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1

plt.savefig('../exp_mixing_time_cross1through4.png', dpi=dpi)
plt.close()

i = 3
line_choices= ['-r','-g','-b','-k']
while i > -1:
	ynpb = np.zeros(len(x_responsetimeb[i]))
	xnpb = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynpb[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnpb[m] = isa
		m += 1
	plt.scatter(xnpb, ynpb, c=colorsb[i], label=crosses[i],alpha=0.25,marker=crossesMarker[i])
	plt.legend()
	plt.ylabel("White Noise Std Dev from 0.1V")
	plt.xlabel("Time to cross 1.2V event (ns)")
	i -= 1
dpi=300
plt.savefig('../exp_mixing_time_ResB_cross1through4.png', dpi=dpi)
plt.close()