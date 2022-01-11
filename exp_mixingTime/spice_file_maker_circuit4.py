# Experiment Overview
# Mixing Time Experiment.

# Part 1. Write a spice file to describe the connections
# Part 2. Write a Shell script to run the spice file and save a result.
header = "*PulseLoop\n \
.include sky130nm.lib\n \
* Circuit 4, 2 pulse gate in ring\n\
Xpg1 sNoise outB outA pgNeg\n \
Xpg2 outA outB pgNeg1\n \
.measure tran responseTimeA WHEN v(outA)=1.2 CROSS=1\n \
.measure tran responseTimeA WHEN v(outA)=1.2 CROSS=2\n \
.measure tran responseTimeA WHEN v(outA)=1.2 CROSS=3\n \
.measure tran responseTimeA WHEN v(outA)=1.2 CROSS=4\n \
.measure tran responseTimeB WHEN v(outB)=1.2 CROSS=1\n \
.measure tran responseTimeB WHEN v(outB)=1.2 CROSS=2\n \
.measure tran responseTimeB WHEN v(outB)=1.2 CROSS=3\n \
.measure tran responseTimeB WHEN v(outB)=1.2 CROSS=4\n "

footer = ".control \n \
tran 10ps 100ns \n "

footer2 = "*quit\n \
.endc\n \
\n \
\n \
*PG\n \
.subckt pgNegPos Aneg Bpos x\n \
\n \
xm1 1 reset_loop critical_node 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 0 Aneg critical_node 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm10 1 Bpos critical_node 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm3 1 critical_node invO 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 0 critical_node invO 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm4 1 invO reset_loop 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 0 invO reset_loop 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 1 invO xe 1 sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 0 invO xe 0 sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 1 xe x 1 sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 0 xe x 0 sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
\n \
v1 1 0 1.8 \n \
\n \
.ends pg \n \
\n \
.subckt pgNeg Aneg Bneg x \n \
\n \
xm1 1 reset_loop critical_node 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 0 Aneg critical_node 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm10 1 Bneg critical_node 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm3 1 critical_node invO 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 0 critical_node invO 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm4 1 invO reset_loop 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 0 invO reset_loop 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 1 invO xe 1 sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 0 invO xe 0 sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 1 xe x 1 sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 0 xe x 0 sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
\n \
v1 1 0 1.8 \n \
\n \
.ends pg \n \
\n \
.subckt pgNeg1 Aneg x \n \
\n \
xm1 1 reset_loop critical_node 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 0 Aneg critical_node 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm3 1 critical_node invO 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 0 critical_node invO 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm4 1 invO reset_loop 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 0 invO reset_loop 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 1 invO xe 1 sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 0 invO xe 0 sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 1 xe x 1 sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 0 xe x 0 sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
\n \
v1 1 0 1.8 \n \
\n \
.ends pg \n \
"

filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

std_dev = 0.1
voltage = 0.1
name_o_file = "PreLayout/exp_mixing_time_circuit4_"
for n in filenames:
    sim_name_o_file = "../" + name_o_file + n + ".cir"
    f = open(sim_name_o_file,"w")
    f.write(header)
    f.write("v2 sNoise 0 dc 0 trrandom (2 20p 0 "+str(std_dev)+ " " + str(voltage) + ")\n")
    std_dev += 0.1
    f.write(footer)
    #f.write("hardcopy plot1"+n+" v(out)+2 v(sNoise) \n")
    f.write(footer2)


name_o_sh = "run_exp_mixing_time_circuit4.sh"
f = open(name_o_sh,"w")
q = 0
for n in filenames:
    q = 0
    while q < 100:
        f.write("ngspice -b -o exp_mixingTime/circuit4/data" +str(q) + n + ".txt "+ name_o_file + n + ".cir\n")
        q += 1