
header = "*PulseLoop\n \
.include sky130nm.lib\n \
Xpg sNoise1 sNoise2 sNoise3 sNoise4 sNoise5 sNoise6 sNoise7 sNoise8 out pg\n \
.measure tran responseTime WHEN v(out)=1.2 CROSS=1\n \
.measure tran secondrTime WHEN v(out)=1.2 CROSS=2\n"

footer = ".control \n" 


footer2 = "*quit\n \
.endc\n \
\n \
\n \
*PG\n \
.subckt pg A B C D E F G H x\n \
\n \
xm1 1 reset_loop critical_node 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm16 0 D Ha 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
xm15 0 D Ga Ha sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
xm14 0 D Fa Ga sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
xm13 0 E Ea Fa sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
xm11 0 D Da Ea sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
xm12 0 C Ca Da sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
xm2 0 A critical_node Ca sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
xm10 1 B critical_node 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
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

filenames = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]

std_dev = 0.1
voltage = 0.1
time = 14.5
for n in filenames:
    name_o_file = "PreLayout/noise_pulsegate8in_1p7nSeries8Sources"+n+".cir"
    f = open(name_o_file,"w")
    f.write(header)
    f.write("v2 sNoise1 0 dc 0 trrandom (2 20p 0 "+str(std_dev)+ " " + str(voltage) + ")\n")
    f.write("v3 sNoise2 0 dc 0 trrandom (2 20p 0 "+str(std_dev)+ " " + str(voltage) + ")\n")
    f.write("v4 sNoise3 0 dc 0 trrandom (2 20p 0 " + str(std_dev) + " " + str(voltage) + ")\n")
    f.write("v5 sNoise4 0 dc 0 trrandom (2 20p 0 " + str(std_dev) + " " + str(voltage) + ")\n")
    f.write("v6 sNoise5 0 dc 0 trrandom (2 20p 0 " + str(std_dev) + " " + str(voltage) + ")\n")
    f.write("v7 sNoise6 0 dc 0 trrandom (2 20p 0 " + str(std_dev) + " " + str(voltage) + ")\n")
    f.write("v8 sNoise7 0 dc 0 trrandom (2 20p 0 " + str(std_dev) + " " + str(voltage) + ")\n")
    f.write("v9 sNoise8 0 dc 0 trrandom (2 20p 0 " + str(std_dev) + " " + str(voltage) + ")\n")
    std_dev += 0.1
    f.write(footer)
    #f.write("hardcopy plot1"+n+" v(out)+2 v(sNoise) \n")
    f.write("tran 10ps " +str(time)+"ns \n ")
    f.write(footer2)
    time = time - 0.5
    
name_o_sh = "run_exp_noise_first_event_time_8input1p7nSeries8Sources.sh"
f = open(name_o_sh,"w")
n = 0
for a in filenames:
    n = 0
    while n < 50:
        f.write("ngspice -b -o noiseFirstStart1p7nSeries8Sources/data" +str(n) + a + ".txt "
                                                                        "PreLayout/noise_pulsegate8in_1p7nSeries8Sources"+a+".cir\n")
        n += 1