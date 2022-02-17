import os
import numpy as np
import statistics
import matplotlib.pyplot as plt
import statistics

paths = ['circuit2/','circuit3/', 'circuit4/', 'circuit6/', 'circuit7/','circuit9/']

circuit_marker = ["|","d", "x", "h", "^","."]

filenames = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"]
label = {"a": 0.1, "b": 0.2, "c": 0.3, "d": 0.4, "e": 0.5, "f": 0.6, "g": 0.7, "h": 0.8, "i": 0.9, "j": 1.0, "k": 1.1,
         "l": 1.2, "m": 1.3,
         "n": 1.4, "o": 1.5}
label_to_index = {"0.1": 0, "0.2": 1, "0.3": 2, "0.4": 3, "0.5": 4, "0.6": 5, "0.7": 6, "0.8": 7, "0.9": 8, "1.0": 9,
                  "1.1": 10, "1.2": 11, "1.3": 12, "1.4": 13, "1.5": 14}

datapoints = 15


def tau_plot_avg_and_std_deviation(tau_x, tau_y, paths, title, plot_file_name):
    tau_avg_y = []
    tau_avg_scatter_y = []
    tau_avg_x = []
    tau_samples_x = []
    tau_samples_count = []
    tau_std_dev = []

    i = 0
    tau_sets_y = []
    while i < len(tau_y):
        # print(tau_y[i])
        j = 0
        tau_sets_y.append(set())
        tau_avg_x.append([])
        tau_avg_scatter_y.append([])
        while j < len(tau_y[i]):
            tau_sets_y[i].add(tau_y[i][j])
            j += 1
        i += 1

    i = 0
    while i < len(tau_y):
        for e in tau_sets_y[i]:
            # tau_avg_x[i].append([])
            tau_avg_scatter_y[i].append([])
        i += 1

    i = 0
    while i < len(tau_y):
        tau_avg_y.append([])
        tau_std_dev.append([])
        tau_samples_x.append([])
        tau_samples_count.append([])
        for e in sorted(tau_sets_y[i]):
            tau_avg_y[i].append(e)
            tau_samples_x[i].append([])
            tau_samples_count[i].append(0)
        i += 1

    # print("a",tau_avg_y)
    i = 0
    while i < len(tau_x):
        tau_avg_y_key = {}
        j = 0
        for each in tau_avg_y[i]:
            tau_avg_y_key[each] = j
            j += 1
        # print("boo",tau_avg_y_key)
        j = 0
        while j < len(tau_y[i]):
            # print(tau_y[i][j])
            # print(tau_samples_x)
            tau_samples_x[i][tau_avg_y_key[tau_y[i][j]]].append(tau_x[i][j])
            # print(tau_samples_count[i][ tau_avg_y_key[tau_y[i][j]] ])
            tau_samples_count[i][tau_avg_y_key[tau_y[i][j]]] += 1
            tau_avg_scatter_y[i][tau_avg_y_key[tau_y[i][j]]].append(tau_y[i][j])
            j += 1
        j = 0
        while j < len(tau_avg_y[i]):
            tau_avg_x[i].append(sum(tau_samples_x[i][j]) / tau_samples_count[i][j])
            j += 1
        j = 0
        while j < len(tau_avg_y[i]):
            # print(tau_samples_x[i][j])
            tau_std_dev[i].append(statistics.stdev(tau_samples_x[i][j]))
            j += 1
        i += 1
    # print(tau_avg_x)
    # print(tau_avg_y)
    # print(tau_std_dev)
    fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=False, sharey=True)
    i = 0
    while i < len(tau_avg_x):
        axs[0].scatter(tau_avg_x[i], tau_avg_y[i], alpha=0.5, marker=circuit_marker[i], s=80)
        axs[0].errorbar(tau_avg_x[i], tau_avg_y[i], label=paths[i], xerr=tau_std_dev[i],
                        fmt=circuit_marker[i])

        axs[1].scatter(tau_avg_x[i], tau_avg_y[i], alpha=0.5, marker=circuit_marker[i], s=80)
        axs[1].errorbar(tau_avg_x[i], tau_avg_y[i], label=paths[i], xerr=tau_std_dev[i], fmt=circuit_marker[i])
        axs[1].set_xlim(0.010, 0.120)
        i += 1
    axs[0].legend()
    axs[0].set_ylabel("sNoise Std Dev from 0.1V")
    axs[1].set_ylabel("sNoise Std Dev from 0.1V")
    axs[0].set_xlabel("tau (ns)")
    axs[1].set_xlabel("tau (ns)")
    fig.suptitle(title)
    plt.savefig('../avg_error_bar_' + plot_file_name, dpi=300)
    plt.close()


# Gather data points from results files (format data.txt)
def tau_plot_by_circuit(plot_file_name, paths, title):
    tau_tap_a_cross1_to_cross2_x = []
    tau_tap_a_cross1_to_cross2_y = []
    l_cnt = 0
    for path in paths:
        tau_tap_a_cross1_to_cross2_x.append([])
        tau_tap_a_cross1_to_cross2_y.append([])
        circuit_label = path.strip("/")
        files = os.listdir(path)
        for name_o_file in files:
            f = open(path + name_o_file, "r")
            lab = name_o_file.split(".")[0][-1]
            res_a1 = 0.0
            res_a2 = 0.0
            a1_bool = False
            a2_bool = False
            for line in f:
                mes_label = 'responsetimeb1'
                if (circuit_label == 'circuit9'):
                    mes_label = 'responsetimeupb1'
                if line.startswith(mes_label):
                    line_split = line.split()
                    print("A1", line_split)
                    res_a1 = float(line_split[2]) * 1000000000.0
                    a1_bool = True
                mes_label = 'responsetimeb2'
                if (circuit_label == 'circuit9'):
                    mes_label = 'responsetimeupb2'
                if line.startswith(mes_label):
                    line_split = line.split()
                    print("A2", line_split)
                    a2_bool = True
                    res_a2 = float(line_split[2]) * 1000000000.0
            if (a1_bool and a2_bool == True):
                tau_tap_a_cross1_to_cross2_x[l_cnt].append(res_a2-res_a1)
                tau_tap_a_cross1_to_cross2_y[l_cnt].append(label[lab])
        l_cnt += 1
        
    fig, axs = plt.subplots(2, 1, figsize=(8, 8), sharex=False, sharey=True)
    i = 0
    while i < len(paths):
        axs[0].set_ylim(0, 1.6)
        axs[0].scatter(tau_tap_a_cross1_to_cross2_x[i], tau_tap_a_cross1_to_cross2_y[i], alpha=0.5,
                       label=paths[i].strip("/"), marker=circuit_marker[i], s=80)
        #axs[0].set_xlim(0, 1e-9)
        axs[1].scatter(tau_tap_a_cross1_to_cross2_x[i], tau_tap_a_cross1_to_cross2_y[i], alpha=0.5,
                       label=paths[i].strip("/"), marker=circuit_marker[i], s=80)
        axs[1].set_xlim(0, 0.2)
        i += 1
    axs[0].legend()
    axs[0].set_ylabel("sNoise Std Dev from 0.1V")
    axs[0].set_xlabel("tau (ns)")
    axs[1].set_xlabel("tau (ns)")
    fig.suptitle(title)
    plt.savefig('../' + plot_file_name, dpi=300)
    plt.close()

    tau_plot_avg_and_std_deviation(tau_tap_a_cross1_to_cross2_x, tau_tap_a_cross1_to_cross2_y, paths, title,
                                      plot_file_name)


tau_plot_by_circuit('exp_mixing_time_tau_tapb_cross1_tapb_cross2.png',
                       paths,
                       'Tap B, Cross 1 to Cross 2')
