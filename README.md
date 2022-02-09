Initial setup of project. 


```
pip install nengo
```

Then move to a shell and navigate to the git folder for the project.
```
nengo
```

Wait until Nengo opens a web browser. Once the browser is open, click on **recurrent_inhibit.py** file in the file navigator on the left hand side.

Comment or uncomment code in the file editor and press the simulate button to see how it works.

Or, open a python interpeter (I use pyCharm) and open **experiment_outline.py**. Press Build and Run to create new png files for 3 new plots based on experiment_outline.py

*Most of the project is now completed with ngspice instead of nengo. 

Why? Because Nengo was going to take days to simulate at the timescales I needed, and also since it is out of the box prepackaged for biological neuron timescales, I did not want to risk accidentally missing a parameter to change. Also, ngspice was easier for me. 

TO START MAGIC from magicVLSI folder:
```
run.sh (starts the magic VLSI Docker image. Details on that not part of this project.)
tcsh
dell:/# sudo ln -s $PDK_ROOT/sky130A/libs.tech/magic/* /usr/local/lib/magic/sys/
dell:/# sudo magic -T sky130A
```
