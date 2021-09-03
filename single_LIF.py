import matplotlib.pyplot as plt
import numpy as np
import nengo
from nengo.dists import Uniform
from nengo.processes import WhiteSignal
from nengo.utils.matplotlib import rasterplot

simt = 2

model = nengo.Network(label="A Single Neuron")
with model:
    neuron = nengo.Ensemble(
        1,
        dimensions=1,  # Represent a scalar
        # Set intercept to 0.5
        intercepts=Uniform(-0.5, -0.5),
        # Set the maximum firing rate of the neuron to 100hz
        max_rates=Uniform(2, 2),
        # Set the neuron's firing rate to increase for positive input
        encoders=[[1]],
    )
with model:
    #cos = nengo.Node(lambda t: np.cos(8 * t))
    #
    input_signal = nengo.Node(WhiteSignal(1, high=10,rms=0.2,y0=0.1,seed=5), size_out=1)
with model:
    # Connect the input signal to the neuron
    nengo.Connection(input_signal, neuron)

with model:
    # The original input
    input_signal_probe = nengo.Probe(input_signal)
    # The raw spikes from the neuron
    spikes = nengo.Probe(neuron.neurons)
    # Subthreshold soma voltage of the neuron
    voltage = nengo.Probe(neuron.neurons, "voltage")
    # Spikes filtered by a 10ms post-synaptic filter
    filtered = nengo.Probe(neuron, synapse=0.1)


with nengo.Simulator(model) as sim:  # Create the simulator
    sim.run(simt)  # Run it for 10 second

# Plot the decoded output of the ensemble
plt.figure()
plt.ylabel("signal")
plt.xlabel("Time (s)")
plt.plot(sim.trange(), sim.data[filtered])
plt.plot(sim.trange(), sim.data[input_signal_probe])
plt.xlim(0, simt)
plt.savefig("signals.png")
# Plot the spiking output of the ensemble
plt.figure(figsize=(8, 4))
plt.subplot(221)
rasterplot(sim.trange(), sim.data[spikes])
plt.ylabel("Neuron")
plt.xlabel("Time (s)")
plt.xlim(0, simt)

# Plot the soma voltages of the neurons
plt.subplot(222)

plt.plot(sim.trange(), sim.data[voltage][:, 0], "r")
plt.xlabel("Time (s)")
plt.xlim(0, simt)
plt.savefig("neuron.png")
#plt.show()