import matplotlib.pyplot as plt
import numpy as np

import nengo
from nengo.processes import WhiteSignal
from nengo.solvers import LstsqL2

model = nengo.Network()

num_n = 10
time_to_run = 10.0

with model:
    # a Node provides non-neural inputs to the model
    input_signal = nengo.Node(WhiteSignal(num_n, high=5), size_out=1)
    # A population of neurons, counted to num_n
    pre = nengo.Ensemble(num_n, dimensions=1)
    # A unidirectional connection between two objects (x,y) x connects to y. y does not connect to x
    # A connection can use a synapse model to include a filter, 
    # otherwise the information will be transmitted without delay in backends that support that.
    #input_connection = \
    nengo.Connection(input_signal, pre)

    post = nengo.Ensemble(num_n, dimensions=1)
    conn = nengo.Connection(pre, post, function=lambda x: np.random.random(1))
    input_signal_probe = nengo.Probe(input_signal)
    pre_p = nengo.Probe(pre, synapse=0.01)
    post_p = nengo.Probe(post, synapse=0.01)
    #pre_p = nengo.Probe(pre)
    #post_p = nengo.Probe(post)

with nengo.Simulator(model) as sim:
    sim.run(time_to_run)

plt.figure(figsize=(8, 8))
#plt.subplot(2, 1, 1)
plt.plot(sim.trange(), sim.data[input_signal_probe].T[0], c="k", label="Input")
plt.plot(sim.trange(), sim.data[pre_p].T[0], c="b", label="Pre")
plt.plot(sim.trange(), sim.data[post_p].T[0], c="r", label="Post")
plt.ylabel("Dimension 1")
plt.legend(loc="best")
plt.legend(loc="best")
plt.savefig("startupStateNumNIs"+str(num_n)+".png")

with model:
    error = nengo.Ensemble(num_n, dimensions=1)
    error_p = nengo.Probe(error, synapse=0.03)

    # Feedback connection. Comment out below line to remove feedback.
    #conn2 = nengo.Connection(post, pre,function=lambda x: np.random.random(1))
    recurrent_connection = nengo.Connection(post, pre, synapse= 0.01)
    
    # Error = actual - target = post - pre
    nengo.Connection(post, error)
    # Connections can support a transform, to map the presynaptic to post synaptic dimensionality.
    nengo.Connection(pre, error, transform=-1)

    # Add the learning rule to the connection
    conn.learning_rule_type = nengo.PES(pre_synapse=0.05)

    # Connect the error into the learning rule
    nengo.Connection(error, conn.learning_rule)

with nengo.Simulator(model) as sim:
    sim.run(time_to_run)


plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(sim.trange(), sim.data[input_signal_probe].T[0], c="k", label="Input")
plt.plot(sim.trange(), sim.data[pre_p].T[0], c="b", label="Pre")
plt.plot(sim.trange(), sim.data[post_p].T[0], c="r", label="Post")
plt.ylabel("Dimension 1")
plt.legend(loc="best")
plt.legend(loc="best")
plt.subplot(2, 1, 2)
plt.plot(sim.trange(), sim.data[error_p], c="b")
plt.ylim(-1, 1)
plt.legend(("Error[0]", "Error[1]"), loc="best")
plt.savefig("LearnErrorStateNumNIs"+str(num_n)+".png")

def inhibit(t):
    return 2.0 if t > time_to_run else 0.0

with model:
    inhib = nengo.Node(inhibit)
    nengo.Connection(inhib, error.neurons, transform=[[-1]] * error.n_neurons)

with nengo.Simulator(model) as sim:
    sim.run(time_to_run + 6.0)

plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(sim.trange(), sim.data[input_signal_probe].T[0], c="k", label="Input")
plt.plot(sim.trange(), sim.data[pre_p].T[0], c="b", label="Pre")
plt.plot(sim.trange(), sim.data[post_p].T[0], c="r", label="Post")
plt.ylabel("Dimension 1")
plt.legend(loc="best")
plt.subplot(2, 1, 2)
plt.plot(sim.trange(), sim.data[error_p], c="b")
plt.ylim(-1, 1)
plt.legend(("Error[0]", "Error[1]"), loc="best")
plt.savefig("stopErrorStateNumNIs"+str(num_n)+".png")