
from collections import deque

import matplotlib.pyplot as plt
import numpy as np

import nengo
from nengo.utils.filter_design import cont2discrete

# parameters of LMU
theta = 2.0  # length of window (in seconds)
order = 8  # number of Legendre polynomials representing window

# parameters of input signal
freq = 2  # frequency limit
rms = 0.30  # amplitude of input (set to keep within [-1, 1])
delay = 0.5  # length of time delay network will learn

# simulation parameters
dt = 0.001  # simulation timestep
sim_t = 100  # length of simulation
seed = 0  # fixed for deterministic results

# compute the A and B matrices according to the LMU's mathematical derivation
# (see the paper for details)
Q = np.arange(order, dtype=np.float64)
R = (2 * Q + 1)[:, None] / theta
j, i = np.meshgrid(Q, Q)

A = np.where(i < j, -1, (-1.0) ** (i - j + 1)) * R
B = (-1.0) ** Q[:, None] * R
C = np.ones((1, order))
D = np.zeros((1,))

A, B, _, _, _ = cont2discrete((A, B, C, D), dt=dt, method="zoh")

class IdealDelay(nengo.synapses.Synapse):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay

    def make_state(self, shape_in, shape_out, dt, dtype=None, y0=None):
        return {}

    def make_step(self, shape_in, shape_out, dt, rng, state):
        # buffer the input signal based on the delay length
        buffer = deque([0] * int(self.delay / dt))

        def delay_func(t, x):
            buffer.append(x.copy())
            return buffer.popleft()

        return delay_func


with nengo.Network(seed=seed) as net:
    # create the input signal
    stim = nengo.Node(
        output=nengo.processes.WhiteSignal(
            high=freq, period=sim_t, rms=rms, y0=0, seed=seed
        )
    )

    # probe input signal and an ideally delayed version of input signal
    p_stim = nengo.Probe(stim)
    p_ideal = nengo.Probe(stim, synapse=IdealDelay(delay))

# run the network and display results
with nengo.Simulator(net) as sim:
    sim.run(10)

    plt.figure(figsize=(16, 6))
    plt.plot(sim.trange(), sim.data[p_stim], label="input")
    plt.plot(sim.trange(), sim.data[p_ideal], label="ideal")
    plt.legend()
    plt.show()