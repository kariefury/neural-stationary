import matplotlib.pyplot as plt
import numpy as np
import nengo
from nengo.dists import Uniform
from nengo.processes import WhiteNoise
from nengo.utils.matplotlib import rasterplot

simt = 0.00001

model = nengo.Network(label="A Single Neuron",seed=91195)
with model:
    neuron = nengo.Ensemble(
        1,
        dimensions=1,  # Represent a scalar
        # Set intercept to 0.5
        intercepts=Uniform(-0.5, 0.5),
        neuron_type=nengo.LIF(min_voltage=0,tau_ref=0.00000000005,tau_rc=0.001), # Set tau_ref= or tau_rc = here to 
        # change those 
        # parms 
        # for the 
        # neurons.
        # Set the maximum firing rate of the neuron to 100hz
        max_rates=Uniform(20000000, 20000000),
        # Set the neuron's firing rate to increase for positive input
        encoders=[[1]],
    )
    
with model:
    print(neuron.max_rates)
    print(neuron.intercepts)
    print(neuron.neurons.ensemble.neuron_type.tau_ref)
    print(neuron.neurons.ensemble.neuron_type.tau_rc)
   # neuron.neurons.ensemble.neuron_type.state = {'voltage':[0.5], 'refractory_time':[0.0]}
with model:
    #cos = nengo.Node(lambda t: np.cos(8 * t))
    #
    input_signal = nengo.Node(WhiteNoise(dist=nengo.dists.Gaussian(0.0, 0.1), seed=1))
    #WhiteSignal(1, high=10,rms=0.2,y0=0.1,seed=5), size_out=1)
with model:
    # Connect the input signal to the neuron
    nengo.Connection(input_signal, neuron)

syn = 0.001

with model:
    # The original input
    input_signal_probe = nengo.Probe(input_signal)
    # The raw spikes from the neuron
    spikes = nengo.Probe(neuron.neurons)
    # Subthreshold soma voltage of the neuron
    voltage = nengo.Probe(neuron.neurons, "voltage")
    # Spikes filtered by a 10ms post-synaptic filter
    filtered = nengo.Probe(neuron, synapse=syn)


with nengo.Simulator(model,dt=0.0000000001) as sim:  # Create the simulator
    sim.run(simt)  # Run it for simt seconds
    #print(neuron.neurons.ensemble.neuron_type.state)
    print('\n'.join(f"* {op}" for op in sim.step_order))
    
with model:
    print(neuron.neurons.ensemble.neuron_type.state)
# Plot the decoded output of the ensemble
plt.figure(figsize=(8,4))
plt.subplot(121)
plt.title("Post Syn Filter " + str(syn) +" Max Rate = 200MHz")
plt.ylabel("signal (Post Syn Filtered)")
plt.xlabel("Time (s)")


#plt.plot(sim.trange(),sim.data[spikes])
plt.plot(sim.trange(), sim.data[input_signal_probe])
plt.plot(sim.trange(), (sim.data[filtered]))
#plt.plot(sim.trange(), (sim.data[filtered])*10000)
plt.xlim(0, simt)

plt.subplot(122)
#plt.title("Post Syn Filter " + str(syn) +" Max Rate = 200MHz")
plt.ylabel("signal (soma spike)")
plt.xlabel("Time (s)")

plt.plot(sim.trange(), sim.data[input_signal_probe])
plt.plot(sim.trange(),sim.data[spikes])

#plt.plot(sim.trange(), (sim.data[filtered]))
#plt.plot(sim.trange(), (sim.data[filtered])*10000)
plt.xlim(0, simt)

plt.savefig("signals_short_time.png")
plt.clf()
# Plot the spiking output of the ensemble
plt.figure(figsize=(8, 4))
plt.subplot(121)
rasterplot(sim.trange(), sim.data[spikes])
plt.ylabel("Neuron")
plt.xlabel("Time (s)")
plt.xlim(0, simt)

# Plot the soma voltages of the neurons
plt.subplot(122)

plt.plot(sim.trange(), sim.data[voltage][:, 0], "r")
plt.ylabel("Soma Voltage")
plt.xlabel("Time (s)")
plt.xlim(0, simt)
plt.savefig("short_time_neuron.png")
#plt.show()