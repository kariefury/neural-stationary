# Experiment Overview
# Mixing Time Experiment.

# Part 1. Write a spice file to describe the connections
# Part 2. Write a Shell script to run the spice file and save a result.
header = "*PulseLoop\n \
.include sky130nm.lib\n \
* Circuit 5, 2 pulse gate in ring, sNoise input to PMOS\n\
Xpg1 outA sNoise outB pos_supply neg_supply pgNegPos\n \
Xpg2 outB outA pos_supply neg_supply pgNeg1\n \
v3 pos_supply 0 1.8\n \
v4 neg_supply 0 0.0\n "

footer = ".control \n \
*plot v(outA) v(outB) v(sNoise)\n \
*plot i(v3)\n \
tran 10ps "

meas_footer = "ns \n \
meas tran responseTimeA1 WHEN v(outA)=1.2 CROSS=1 \n \
meas tran responseTimeA2 WHEN v(outA)=1.2 CROSS=2\n \
meas tran responseTimeA3 WHEN v(outA)=1.2 CROSS=3\n \
meas tran responseTimeA4 WHEN v(outA)=1.2 CROSS=4\n \
meas tran responseTimeB1 WHEN v(outB)=1.2 CROSS=1\n \
meas tran responseTimeB2 WHEN v(outB)=1.2 CROSS=2\n \
meas tran responseTimeB3 WHEN v(outB)=1.2 CROSS=3\n \
meas tran responseTimeB4 WHEN v(outB)=1.2 CROSS=4\n \
let tdiff = responsetimea4-responsetimea1\n \
print tdiff\n \
meas tran iavg avg i(v3) FROM=responsetimea1 TO=responsetimea4 \n \
print iavg\n "


footer2 = "*quit\n \
.endc\n \
\n \
\n \
.subckt pgNeg2PosSeries Aneg Bpos Cpos x pow_supply gnd_supply\n \
\n \
xm1 pow_supply reset_loop critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 gnd_supply Aneg critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm11 pow_supply Cpos critical_node bc sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm10 bc Bpos critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm3 pow_supply critical_node invO pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 gnd_supply critical_node invO gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm14 pow_supply invO reset_loop pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 gnd_supply invO reset_loop gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 pow_supply invO xe pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 gnd_supply invO xe gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 pow_supply xe x pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 gnd_supply xe x gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
.ends pgNeg2PosSeries \n \
\n \
.subckt pgNegPos Aneg Bpos x pow_supply gnd_supply\n \
\n \
xm1 pow_supply reset_loop critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 gnd_supply Aneg critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm10 pow_supply Bpos critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm3 pow_supply critical_node invO pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 gnd_supply critical_node invO gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm14 pow_supply invO reset_loop pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 gnd_supply invO reset_loop gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 pow_supply invO xe pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 gnd_supply invO xe gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 pow_supply xe x pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 gnd_supply xe x gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
.ends pgNegPos \n \
\n \
.subckt pgNeg Aneg Bneg x pow_supply gnd_supply\n \
\n \
xm1 pow_supply reset_loop critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 gnd_supply Aneg critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm10 gnd_supply Bneg critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm3 pow_supply critical_node invO pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 gnd_supply critical_node invO gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm14 pow_supply invO reset_loop pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 gnd_supply invO reset_loop gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 pow_supply invO xe pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 gnd_supply invO xe gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 pow_supply xe x pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 gnd_supply xe x gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
.ends pgNeg \n \
\n \
\n \
.subckt pgNeg2Series Aneg Bneg BnegSeries x pow_supply gnd_supply\n \
\n \
xm1 pow_supply reset_loop critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 gnd_supply Aneg critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm10 gnd_supply Bneg critical_node bs sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm11 bs BnegSeries critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm3 pow_supply critical_node invO pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 gnd_supply critical_node invO gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm14 pow_supply invO reset_loop pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 gnd_supply invO reset_loop gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 pow_supply invO xe pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 gnd_supply invO xe gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 pow_supply xe x pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 gnd_supply xe x gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
.ends pgNeg2Series \n \
\n \
.subckt pgNegSeries Bneg BnegSeries x pow_supply gnd_supply\n \
\n \
xm1 pow_supply reset_loop critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 gnd_supply Aneg critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm10 gnd_supply Bneg critical_node bs sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm11 bs BnegSeries critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm3 pow_supply critical_node invO pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 gnd_supply critical_node invO gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm14 pow_supply invO reset_loop pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 gnd_supply invO reset_loop gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 pow_supply invO xe pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 gnd_supply invO xe gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 pow_supply xe x pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 gnd_supply xe x gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
.ends pgNegSeries \n \
\n \
.subckt pgNeg1 Aneg x pow_supply gnd_supply\n \
\n \
xm1 pow_supply reset_loop critical_node pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 gnd_supply Aneg critical_node gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm3 pow_supply critical_node invO pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm4 gnd_supply critical_node invO gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm14 pow_supply invO reset_loop pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
xm5 gnd_supply invO reset_loop gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
\n \
xm6 pow_supply invO xe pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm7 gnd_supply invO xe gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
\n \
xm8 pow_supply xe x pow_supply sky130_fd_pr__pfet_01v8 l=150n w=720n \n \
xm9 gnd_supply xe x gnd_supply sky130_fd_pr__nfet_01v8 l=150n w=360n \n \
.ends pgNeg1 \n \
"

filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]

std_dev = 0.1
voltage = 0.1
name_o_file = "PreLayout/exp_mixing_time_circuit5_"
for n in filenames:
    sim_name_o_file = "../" + name_o_file + n + ".cir"
    f = open(sim_name_o_file,"w")
    f.write(header)
    f.write("v2 sNoise 0 dc 0 trrandom (2 20p 0 "+str(std_dev)+ " " + str(voltage) + ")\n")
    std_dev += 0.1
    f.write(footer)
    f.write(str(30.0/(std_dev*std_dev*2.6)))
    f.write(meas_footer)
    #f.write("hardcopy plot1"+n+" v(out)+2 v(sNoise) \n")
    f.write(footer2)


name_o_sh = "run_exp_mixing_time_circuit5.sh"
f = open(name_o_sh,"w")
q = 0
for n in filenames:
    q = 0
    while q < 100:
        f.write("ngspice -b -o exp_mixingTime/circuit5/data" +str(q) + n + ".txt "+ name_o_file + n + ".cir\n")
        q += 1