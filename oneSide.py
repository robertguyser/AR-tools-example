import artools
import numpy as np
import matplotlib.pyplot as plt
import os
import pprint

model = artools.Model()
model.set_frequency_sweep(0., 300., units='ghz')
model.add_layer(material='vacuum', category='source')
model.add_layer(material='alumina', category='terminator')  

##### Standard fts trilayer ptfe
model.add_layer(material='eptfe', thickness=15.0)
model.add_layer(material='ldpe', thickness=1.)
model.add_layer(material='ro3035', thickness=5.0)
model.add_layer(material='ldpe', thickness=1.)
model.add_layer(material='ro3006', thickness=5.0)

packed = model.package_model()

sim_model = artools.Simulate(packed)

sim_results = sim_model.results['angle_set_0']

sim_f = sim_model.results['model_parameters']['frequencies']/1e9 # sim freq converted to GHz!

sim_t = sim_results['T']

(79.4, 107.2),(127.7, 168.9),(196.2, 247.5)

fig, ax = plt.subplots()
ax.set_ylabel('Fractional transmittance')
ax.set_xlabel('Frequency [GHz]')

plt.axvspan(79.4, 107.2, edgecolor='None', facecolor='k', alpha=.1)
plt.axvspan(127.7, 168.9, edgecolor='None', facecolor='k', alpha=.1)
plt.axvspan(196.2, 247.5, edgecolor='None', facecolor='k', alpha=.1)
ax.plot(sim_f, np.poly1d(np.polyfit(sim_f, sim_t, 100))(sim_f))

plt.show()