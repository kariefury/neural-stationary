import os
import numpy as np
import statistics
import matplotlib.pyplot as plt
import statistics

#paths_a1_to_a4 = ['circuit2/','circuit3/','circuit4/','circuit5/','circuit6/','circuit7/','circuit8/','circuit9/']
paths_a1_to_a4 = ['circuit3/','circuit4/','circuit6/','circuit7/']
iavg_a1_to_a4_meas_cir_labels = ['iavg_from_response_a1_to_response_a4','iavg_from_response_a1_to_response_a4',
						 'iavg_from_response_a1_to_response_a4',
						'iavg_from_response_a1_to_response_a4']
#paths_b1_to_b4 = ['circuit2/','circuit3/','circuit4/','circuit5/','circuit6/','circuit7/','circuit8/','circuit9/']
paths_b1_to_a1 = ['circuit3/','circuit4/','circuit6/','circuit7/']
iavg_b1_to_b4_meas_cir_labels = ['iavg_from_response_b1_to_response_b4','iavg_from_response_b1_to_response_b4',
						'iavg_from_response_b1_to_response_b4',
						'iavg_from_response_b1_to_response_b4']

paths_start_to_a1 = ['circuit3/','circuit4/','circuit6/','circuit7/']
iavg_start_to_a1_meas_cir_labels = ['iavg_start_to_response_a1',
								   'iavg_start_to_response_a1','iavg_start_to_response_a1',
						'iavg_start_to_response_a1']

paths_start_to_b1 = ['circuit3/','circuit4/','circuit6/','circuit7/']
iavg_start_to_b1_meas_cir_labels = ['iavg_start_to_response_b1',
								   'iavg_start_to_response_b1',
						 'iavg ','iavg_start_to_response_b1',
						'iavg_start_to_response_b1']

circuit_marker = ["d", "x", "h", "^"]

filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
label = {"a":0.1, "b":0.2,"c":0.3,"d":0.4,"e":0.5,"f":0.6,"g":0.7,"h":0.8,"i":0.9,"j":1.0,"k":1.1,"l":1.2,"m":1.3,
		 "n":1.4,"o":1.5}
label_to_index = {"0.1":0, "0.2": 1, "0.3": 2, "0.4": 3, "0.5": 4, "0.6": 5, "0.7": 6, "0.8": 7, "0.9": 8, "1.0": 9,
					"1.1":10, "1.2":11,"1.3": 12, "1.4": 13, "1.5": 14}

datapoints = 15

def energy_plot_avg_and_std_deviation(energy_x, energy_y,paths,title,plot_file_name):
	energy_avg_y = []
	energy_avg_scatter_y = []
	energy_avg_x = []
	energy_samples_x = []
	energy_samples_count = []
	energy_std_dev = []
	
	i = 0
	energy_sets_y = []
	while i < len(energy_y):
		#print(energy_y[i])
		j = 0
		energy_sets_y.append( set() )
		energy_avg_x.append([])
		energy_avg_scatter_y.append([])
		while j < len(energy_y[i]):
			energy_sets_y[i].add(energy_y[i][j])
			j += 1
		i += 1
	
	i = 0
	while i < len(energy_y):
		for e in energy_sets_y[i]:
			#energy_avg_x[i].append([])
			energy_avg_scatter_y[i].append([])
		i += 1
	
	i = 0
	while i < len(energy_y):
		energy_avg_y.append([])
		energy_std_dev.append([])
		energy_samples_x.append([])
		energy_samples_count.append([])
		for e in sorted(energy_sets_y[i]):
			energy_avg_y[i].append(e)
			energy_samples_x[i].append([])
			energy_samples_count[i].append(0)
		i += 1
		
	#print("a",energy_avg_y)
	i = 0
	while i < len(energy_x):
		energy_avg_y_key = {}
		j = 0
		for each in energy_avg_y[i]:
			energy_avg_y_key[each] = j
			j += 1
		#print("boo",energy_avg_y_key)
		j = 0
		while j < len( energy_y[i] ):
			#print(energy_y[i][j])
			#print(energy_samples_x)
			energy_samples_x[i][ energy_avg_y_key[energy_y[i][j]] ].append( energy_x[i][j])
			#print(energy_samples_count[i][ energy_avg_y_key[energy_y[i][j]] ])
			energy_samples_count[i][ energy_avg_y_key[energy_y[i][j]] ] += 1
			energy_avg_scatter_y[i][ energy_avg_y_key[energy_y[i][j]] ].append(energy_y[i][j])
			j += 1
		j = 0
		while j < len(energy_avg_y[i]):
			energy_avg_x[i].append(sum(energy_samples_x[i][j]) / energy_samples_count[i][j])
			j += 1
		j = 0
		while j < len(energy_avg_y[i]):
			#print(energy_samples_x[i][j])
			energy_std_dev[i].append(statistics.stdev(energy_samples_x[i][j]))
			j += 1
		i += 1
	#print(energy_avg_x)
	#print(energy_avg_y)
	#print(energy_std_dev)
	fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=False, sharey=True)
	i = 0
	print(len(energy_avg_x),len(energy_avg_y))
	while i < len(energy_avg_x):
		print('len(energy_avg_x[i])',len(energy_avg_x[i]))
		print(energy_avg_x[i])
		print('len(energy_avg_y[i])',len(energy_avg_y[i]))
		print(energy_avg_y[i])
		print('len(energy_avg_scatter_y[i])',len(energy_avg_scatter_y[i]))
		print('len(circuit_marker)',len(circuit_marker))
		print(i)
		axs[0].scatter(energy_avg_x[i], energy_avg_y[i], alpha=0.5, marker=circuit_marker[i], s=80)
		axs[0].errorbar(energy_avg_x[i], energy_avg_y[i], label=paths[i], xerr=energy_std_dev[i], 
		fmt=circuit_marker[i])
		
		axs[1].scatter(energy_avg_x[i], energy_avg_y[i], alpha=0.5, marker=circuit_marker[i], s=80)
		axs[1].errorbar(energy_avg_x[i], energy_avg_y[i], label=paths[i], xerr=energy_std_dev[i],fmt=circuit_marker[i])
		axs[1].set_xlim(0, 2.5e-13)
		i += 1
	axs[0].legend()
	axs[0].set_ylabel("sNoise Std Dev from 0.1V")
	axs[1].set_ylabel("sNoise Std Dev from 0.1V")
	axs[0].set_xlabel("Energy (j)")
	axs[1].set_xlabel("Energy (j)")
	fig.suptitle(title)
	plt.savefig('../avg_error_bar_' + plot_file_name, dpi=300)
	plt.close()
		
	
# Gather data points from results files (format data.txt)
def energy_plot_by_circuit(iavg_meas_cir_labels,plot_file_name,paths,title):
	energy_tap_a_cross1_to_cross4_x = []
	energy_tap_a_cross1_to_cross4_y = []
	iavg_x = []
	iavg_y = []
	l_cnt = 0
	for path in paths:
		energy_tap_a_cross1_to_cross4_x.append([])
		energy_tap_a_cross1_to_cross4_y.append([])
		circuit_label = path.strip("/")
		iavg_meas_cir_label = iavg_meas_cir_labels[l_cnt]
		iavg_x.append([])
		iavg_y.append([])
		files = os.listdir(path)
		for name_o_file in files:
			f = open(path+name_o_file,"r")
			lab = name_o_file.split(".")[0][-1]
			for line in f:
				if line.startswith(iavg_meas_cir_label):
					line_split = line.split()
					if (len(line_split) == 6):
						iavg_float = float(line_split[1])
						iavg_from_float_ns = float(line_split[3]) * 1000000000.0
						iavg_to_float_ns = float(line_split[5]) * 1000000000.0
						iavg_tdiff_float = (iavg_to_float_ns - iavg_from_float_ns) / 1000000000.0
						iavg_x[l_cnt].append(iavg_float)
						iavg_y[l_cnt].append(label[lab])
						energy_in_joules = abs(1.8 * iavg_float * iavg_tdiff_float)
						energy_tap_a_cross1_to_cross4_x[l_cnt].append(energy_in_joules)
						energy_tap_a_cross1_to_cross4_y[l_cnt].append(label[lab])
						print(circuit_label, name_o_file, iavg_float, iavg_tdiff_float, 'energy:', energy_in_joules)
		l_cnt += 1
	
	fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=False, sharey=True)
	i = 0
	while i < len(paths):
		axs[0].set_ylim(0, 1.6)
		axs[0].scatter(energy_tap_a_cross1_to_cross4_x[i], energy_tap_a_cross1_to_cross4_y[i], alpha=0.5,
					   label=paths[i].strip("/"), marker=circuit_marker[i], s=80)
		#axs[0].set_xlim(0, 1e-12)
		axs[1].scatter(energy_tap_a_cross1_to_cross4_x[i], energy_tap_a_cross1_to_cross4_y[i], alpha=0.5,
					   label=paths[i].strip("/"),marker=circuit_marker[i], s=80)
		axs[1].set_xlim(1e-18, 1e-12)
		i += 1
	axs[0].legend()
	axs[0].set_ylabel("sNoise Std Dev from 0.1V")
	axs[0].set_xlabel("Energy (j)")
	axs[1].set_xlabel("Energy (j)")
	fig.suptitle(title)
	plt.savefig('../'+plot_file_name, dpi=300)
	plt.close()

	energy_plot_avg_and_std_deviation(energy_tap_a_cross1_to_cross4_x, energy_tap_a_cross1_to_cross4_y, paths,title,
									  plot_file_name)


energy_plot_by_circuit(iavg_a1_to_a4_meas_cir_labels,
					   'exp_mixing_time_energy_tapa_cross1_tapa_cross4.png',
					   paths_a1_to_a4,
					   'Mixing Time Energy Tap A Cross 1 to Cross 4')

energy_plot_by_circuit(iavg_b1_to_b4_meas_cir_labels,
					   'exp_mixing_time_energy_tapb_cross1_tapb_cross4.png',
					   paths_a1_to_a4,
					   'Mixing Time Energy Tap B Cross 1 to Cross 4')

energy_plot_by_circuit(iavg_start_to_a1_meas_cir_labels,
					   'exp_mixing_time_energy_start_to_a1.png',
					   paths_start_to_a1,
					   'Mixing Time Energy Tap A. start to Cross 1')

energy_plot_by_circuit(iavg_start_to_b1_meas_cir_labels,
					   'exp_mixing_time_energy_start_to_b1.png',
					   paths_start_to_b1,
					   'Mixing Time Energy Tap B. start to Cross 1')