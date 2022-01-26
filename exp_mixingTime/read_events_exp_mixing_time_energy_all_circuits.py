import os
import numpy as np
import statistics
import matplotlib.pyplot as plt

paths = ['circuit2/','circuit3/','circuit4/','circuit5/','circuit6/','circuit7/','circuit8/','circuit9/']
iavg_meas_cir_labels = ['iavg ','iavg ','iavg ','iavg ','iavg ',
						'iavg ','iavg ',"iavg "]

circuit_marker = ["|","d","x","+","h","^","*","."]

filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
label = {"a":0.1, "b":0.2,"c":0.3,"d":0.4,"e":0.5,"f":0.6,"g":0.7,"h":0.8,"i":0.9,"j":1.0,"k":1.1,"l":1.2,"m":1.3,
		 "n":1.4,"o":1.5}
label_to_index = {"0.1":0, "0.2": 1, "0.3": 2, "0.4": 3, "0.5": 4, "0.6": 5, "0.7": 6, "0.8": 7, "0.9": 8, "1.0": 9,
					"1.1":10, "1.2":11,"1.3": 12, "1.4": 13, "1.5": 14}

datapoints = 15
energy_tap_a_cross1_to_cross4_x = []
energy_tap_a_cross1_to_cross4_y = []
iavg_x = []
iavg_y = []

# Gather data points from results files (format data.txt)
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
		ra1_float_ns = 0.0
		ra4_float_ns = 0.0
		tdiff_check = 0.0
		ra1_bool = False
		ra4_bool = False
		tdiff_float = 0.0
		iavg_float = 0.0
		iavg_from_float_ns = 0.0
		iavg_to_float_ns = 0.0
		iavg_tdiff_float_ns = 0.0
		for line in f:
			if line.startswith("responsetimea1"):
				line_split = line.split()
				#print(circuit_label, name_o_file, line_split, len(line_split))
				ra1_float_ns = float(line_split[2]) * 1000000000.0
				ra1_bool = True
			if line.startswith("responsetimea4"):
				line_split = line.split()
				#print(circuit_label, name_o_file, line_split, len(line_split))
				ra4_float_ns = float(line_split[2]) * 1000000000.0
				ra4_bool = True
			if line.startswith("tdiff "):
				line_split = line.split()
				#print(circuit_label, name_o_file, line_split, len(line_split))
				tdiff_float_ns = float(line_split[2]) * 1000000000.0
				tdiff_float = float(line_split[2])
			if line.startswith("tdiffb"):
				line_split = line.split()
				#print(circuit_label, name_o_file, line_split, len(line_split))
			if line.startswith(iavg_meas_cir_label):
				line_split = line.split()
				#print(circuit_label, name_o_file, line_split, len(line_split))
				if (len(line_split) == 7):
					iavg_float = float(line_split[2])
					iavg_from_float_ns = float(line_split[4]) * 1000000000.0
					iavg_to_float_ns = float(line_split[6]) * 1000000000.0
					iavg_tdiff_float_ns = iavg_to_float_ns - iavg_from_float_ns
					iavg_x[l_cnt].append(iavg_float)
					iavg_y[l_cnt].append(label[lab])
		#print(circuit_label, name_o_file,ra1_bool, ra4_bool)
		if ra1_bool and ra4_bool:
			if tdiff_float == 0.0:
				tdiff_float = abs((ra4_float_ns-ra1_float_ns)) /  1000000000.0
			energy_in_joules =  abs(1.8*iavg_float*tdiff_float)
			energy_tap_a_cross1_to_cross4_x[l_cnt].append(energy_in_joules)
			energy_tap_a_cross1_to_cross4_y[l_cnt].append(label[lab])
			print(circuit_label, name_o_file, iavg_float, tdiff_float, 'energy:',energy_in_joules)
	l_cnt += 1

circuit_marker = ["|","d","x","+","h","^","*","."]
fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=False, sharey=True)
i = 0
while i < len(circuit_label):
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
fig.suptitle('Mixing Time Energy Tap A Cross 1 to Cross 4')
plt.savefig('../exp_mixing_time_energy_tapa_cross1_tapa_cross4.png', dpi=300)
plt.close()