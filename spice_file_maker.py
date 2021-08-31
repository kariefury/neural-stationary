
header = "*PulseLoop\n \
.include sky130nm.lib\n \
Xpg sNoise out pg\n"

footer = ".control \n \
tran 10ps 100ns \n "

footer2 = "quit\n \
.endc\n \
\n \
\n \
*PG\n \
.subckt pg A x\n \
\n \
xm1 1 reset_loop critical_node 1 sky130_fd_pr__pfet_01v8 l=150n w=720n\n \
\n \
xm2 0 A critical_node 0 sky130_fd_pr__nfet_01v8 l=150n w=360n\n \
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
for n in filenames:
    name_o_file = "PreLayout\pulsegate1"+n+".cir"
    f = open(name_o_file,"w")
    f.write(header)
    f.write("v2 sNoise 0 dc 0 trrandom (2 20p 0 "+str(std_dev)+" .2)\n")
    std_dev += 0.1
    f.write(footer)
    f.write("hardcopy plot1"+n+" v(out)+2 v(sNoise) \n")
    f.write(footer2)