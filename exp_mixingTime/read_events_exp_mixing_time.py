import os
import numpy as np
import statistics
import matplotlib.pyplot as plt

paths = ['circuit3/']
responsea_cir_label = "responsetimea"  # , circuits 2 - 8
#responsea_cir_label = "responsetimeupa" # Remember for circuit9 the cross is measured here
responseb_cir_label = "responsetimeb"  # circuits 2 - 8
#responseb_cir_label = "responsetimeupb"  # Remember for circuit9, the crossing is measured here
circuit_label = paths[0].strip("/")
crosses = ['Cross 1', 'Cross 2', 'Cross 3', 'Cross 4']
crossesMarker = ["2", "3", "1", "4"]
clab = ['black', 'green', 'black', 'blue']#['black','blue','gray','red']


filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
label = {"a":0.1, "b":0.2,"c":0.3,"d":0.4,"e":0.5,"f":0.6,"g":0.7,"h":0.8,"i":0.9,"j":1.0,"k":1.1,"l":1.2,"m":1.3,
		 "n":1.4,"o":1.5}
label_to_index = {"0.1":0, "0.2": 1, "0.3": 2, "0.4": 3, "0.5": 4, "0.6": 5, "0.7": 6, "0.8": 7, "0.9": 8, "1.0": 9,
					"1.1":10, "1.2":11,"1.3": 12, "1.4": 13, "1.5": 14}
datapoints = 15

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


# Gather data points from results files (format data.txt)
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
			if line.startswith(responsea_cir_label):
				fVal = line.split()[2]
				fValFloat = float(fVal)
				if cross_count_a <= 4:
					ns = fValFloat * 1000000000.0
					print(name_o_file, ns, cross_count_a)
					x_responsetimea[cross_count_a-1].append(ns)
					y_responsetimea[cross_count_a-1].append(label[lab])
					colors[cross_count_a-1].append(clab[cross_count_a-1])
				cross_count_a += 1
			if line.startswith(responseb_cir_label):
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


# Data points for Response A
fig, axs = plt.subplots(2, 3, figsize=(8, 5), sharex=False, sharey=True)
dpi = 300
i = 3
line_choices = ['-r', '-g', '-b', '-k']
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
	axs[0,0].scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[0, 0].set_xlim(0, 2)

	axs[0, 1].scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[0, 1].set_xlim(0, 10)

	axs[0, 2].scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[0, 2].set_xlim(0, 20)

	axs[1, 0].scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[1, 0].set_xlim(0, 100)

	axs[1, 1].scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[1, 1].set_xlim(2, 10)

	axs[1, 2].scatter(xnp, ynp, c=colors[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[1, 2].set_xlim(10, 20)
	axs[0, 2].legend()
	axs[0 , 0].set_ylim(0, 1.6)
	axs[1, 0].set_ylim(0, 1.6)
	axs[0, 0].set_ylabel("sNoise Std Dev from 0.1V")
	axs[1, 0].set_ylabel("sNoise Std Dev from 0.1V")
	axs[1, 0].set_xlabel("Time (ns) cross 1.2V")
	axs[1, 1].set_xlabel("Time (ns) cross 1.2V")
	axs[1, 2].set_xlabel("Time (ns) cross 1.2V")
	i -= 1

fig.suptitle(circuit_label+' Tap A ' + responsea_cir_label)
plt.savefig('../exp_mixing_time_'+circuit_label+'_cross1through4_resA.png', dpi=dpi)
plt.close()

# Response B
i = 3
line_choices = ['-r', '-g', '-b', '-k']  # ['-k','-b','-g','-y','m--','c--','g--']
fig, axs = plt.subplots(2, 3, figsize=(8, 5), sharex=False, sharey=True)
while i > -1:
	ynp = np.zeros(len(x_responsetimeb[i]))
	xnp = np.zeros(len(x_responsetimeb[i]))
	m = 0
	for isa in y_responsetimeb[i]:
		ynp[m] = isa
		m += 1
	m = 0
	for isa in x_responsetimeb[i]:
		xnp[m] = isa
		m += 1
	axs[0, 0].set_ylim(0, 1.6)
	axs[1, 0].set_ylim(0, 1.6)
	axs[0, 0].scatter(xnp, ynp, c=colorsb[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[0, 0].set_xlim(0, 2)

	axs[0, 1].scatter(xnp, ynp, c=colorsb[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[0, 1].set_xlim(0, 10)

	axs[0, 2].scatter(xnp, ynp, c=colorsb[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[0, 2].set_xlim(0, 20)

	axs[1, 0].scatter(xnp, ynp, c=colorsb[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[1, 0].set_xlim(0, 100)

	axs[1, 1].scatter(xnp, ynp, c=colorsb[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[1, 1].set_xlim(2, 10)

	axs[1, 2].scatter(xnp, ynp, c=colorsb[i], label=crosses[i], alpha=0.25, marker=crossesMarker[i])
	axs[1, 2].set_xlim(10, 20)
	axs[0, 2].legend()
	axs[0, 0].set_ylabel("sNoise Std Dev from 0.1V")
	axs[1, 0].set_ylabel("sNoise Std Dev from 0.1V")
	axs[1, 0].set_xlabel("Time (ns) cross 1.2V")
	axs[1, 1].set_xlabel("Time (ns) cross 1.2V")
	axs[1, 2].set_xlabel("Time (ns) cross 1.2V")
	i -= 1

fig.suptitle(circuit_label+' Tap B ' + responseb_cir_label)
plt.savefig('../exp_mixing_time_'+circuit_label+'_cross1through4_resB.png', dpi=dpi)
plt.close()


# Average Response Time for Response A (and Response B in next section) with Cross 1, 2, 3,4 for each
fig, axs = plt.subplots(1, 2, figsize=(8, 4), sharex=False, sharey=True)
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
		#print(j)
		voltage = y_responsetimea[i][j]
		#print(voltage)
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
		if tap_b_x_sample_count[i][j] > 0.0:
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
	axs[0].set_ylim(0, 1.6)
	axs[0].scatter(tap_a_x_values_avg[i], tap_a_y_values[i], alpha=0.5, marker=crossesMarker[i], s=80)
	axs[0].errorbar(tap_a_x_values_avg[i], tap_a_y_values[i], label=crosses[i], xerr=tap_a_x_err_std_dev[i], \
																				 fmt=crossesMarker[i])
	axs[0].set_xlim(0, 10)
	axs[1].scatter(tap_a_x_values_avg[i], tap_a_y_values[i], alpha=0.5, marker=crossesMarker[i], s=80)
	axs[1].errorbar(tap_a_x_values_avg[i], tap_a_y_values[i], label=crosses[i], xerr=tap_a_x_err_std_dev[i], \
					   fmt=crossesMarker[i])
	axs[1].set_xlim(0, 100)
	i += 1
axs[0].legend()
axs[0].set_ylabel("sNoise Std Dev from 0.1V")
axs[0].set_xlabel("Time (ns) cross 1.2V")
axs[1].set_xlabel("Time (ns) cross 1.2V")
fig.suptitle(circuit_label+' Tap A ' + responsea_cir_label)
plt.savefig('../exp_mixing_time_'+circuit_label+'_averages_resA.png', dpi=dpi)
plt.close()

# Avg Response time B with error bars
fig, axs = plt.subplots(1, 2, figsize=(8, 4), sharex=False, sharey=True)

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
	axs[0].set_ylim(0,1.6)
	axs[0].scatter(tap_b_x_values_avg[i], tap_b_y_values[i], alpha=0.5, marker=crossesMarker[i], s=80)
	axs[0].errorbar(tap_b_x_values_avg[i], tap_b_y_values[i], label=crosses[i], xerr=tap_b_x_err_std_dev[i], \
																				 fmt=crossesMarker[i])
	axs[0].set_xlim(0, 10)
	axs[1].scatter(tap_b_x_values_avg[i], tap_b_y_values[i], alpha=0.5, marker=crossesMarker[i], s=80)
	axs[1].errorbar(tap_b_x_values_avg[i], tap_b_y_values[i], label=crosses[i], xerr=tap_b_x_err_std_dev[i], \
					   fmt=crossesMarker[i])
	axs[1].set_xlim(0, 100)
	i += 1
axs[0].legend()
axs[0].set_ylabel("sNoise Std Dev from 0.1V")
axs[0].set_xlabel("Time (ns) cross 1.2V")
axs[1].set_xlabel("Time (ns) cross 1.2V")
fig.suptitle(circuit_label+' Tap B ' + responseb_cir_label)
plt.savefig('../exp_mixing_time_'+circuit_label+'_averages_resB.png', dpi=dpi)
