import artools
import numpy as np
import matplotlib.pyplot as plt
import os
import pprint
import matplotlib.patches as patches

##### Standard fts trilayer ptfe
porex1 = artools.Model()
porex1.set_frequency_sweep(0., 300., units='ghz')
porex1.add_layer(material='vacuum', category='source')
porex1.add_layer(material='alumina', category='terminator')
porex1.add_layer(material='eptfe', thickness=14.75)
porex1.add_layer(material='ldpe', thickness=0.5)
porex1.add_layer(material='ro3035', thickness=5.0)
porex1.add_layer(material='ldpe', thickness=0.5)
porex1.add_layer(material='ro3006', thickness=5.0)
porex1.add_layer(material='ldpe', thickness=0.5)

porex1packed = porex1.package_model()
porex1sim_model = artools.Simulate(porex1packed)
porex1sim_results = porex1sim_model.results['angle_set_0']
porex1sim_f = porex1sim_model.results['model_parameters']['frequencies']/1e9 # sim freq converted to GHz!
porex1sim_t = porex1sim_results['T']

##### Standard fts trilayer ptfe
porex2 = artools.Model()
porex2.set_frequency_sweep(0., 300., units='ghz')
porex2.add_layer(material='vacuum', category='source')
porex2.add_layer(material='alumina', category='terminator')
porex2.add_layer(material='eptfe', thickness=13.29)
porex2.add_layer(material='ldpe', thickness=0.5)
porex2.add_layer(material='ro3035', thickness=5.0)
porex2.add_layer(material='ldpe', thickness=0.5)
porex2.add_layer(material='ro3006', thickness=5.0)
porex2.add_layer(material='ldpe', thickness=0.5)

porex2packed = porex2.package_model()
porex2sim_model = artools.Simulate(porex2packed)
porex2sim_results = porex2sim_model.results['angle_set_0']
porex2sim_f = porex2sim_model.results['model_parameters']['frequencies']/1e9 # sim freq converted to GHz!
porex2sim_t = porex2sim_results['T']

##### Standard fts trilayer ptfe
zitex1 = artools.Model()
zitex1.set_frequency_sweep(0., 300., units='ghz')
zitex1.add_layer(material='vacuum', category='source')
zitex1.add_layer(material='alumina', category='terminator')
zitex1.add_layer(material='eptfe', thickness=15.25)
zitex1.add_layer(material='ldpe', thickness=0.5)
zitex1.add_layer(material='ro3035', thickness=5.0)
zitex1.add_layer(material='ldpe', thickness=0.5)
zitex1.add_layer(material='ro3006', thickness=5.0)
zitex1.add_layer(material='ldpe', thickness=0.5)

zitex1packed = zitex1.package_model()
zitex1sim_model = artools.Simulate(zitex1packed)
zitex1sim_results = zitex1sim_model.results['angle_set_0']
zitex1sim_f = zitex1sim_model.results['model_parameters']['frequencies']/1e9 # sim freq converted to GHz!
zitex1sim_t = zitex1sim_results['T']

##### Standard fts trilayer ptfe
zitex2 = artools.Model()
zitex2.set_frequency_sweep(0., 300., units='ghz')
zitex2.add_layer(material='vacuum', category='source')
zitex2.add_layer(material='alumina', category='terminator')
zitex2.add_layer(material='eptfe', thickness=12.10)
zitex2.add_layer(material='ldpe', thickness=0.5)
zitex2.add_layer(material='ro3035', thickness=5.0)
zitex2.add_layer(material='ldpe', thickness=0.5)
zitex2.add_layer(material='ro3006', thickness=5.0)
zitex2.add_layer(material='ldpe', thickness=0.5)

zitex2packed = zitex2.package_model()
zitex2sim_model = artools.Simulate(zitex2packed)
zitex2sim_results = zitex2sim_model.results['angle_set_0']
zitex2sim_f = zitex2sim_model.results['model_parameters']['frequencies']/1e9 # sim freq converted to GHz!
zitex2sim_t = zitex2sim_results['T']

fig, ax = plt.subplots()
ax.set_ylabel('Fractional Transmittance', fontsize=18)
ax.set_xlabel('Frequency [GHz]', fontsize=18)

plt.axvspan(79.4, 107.2, edgecolor='None', facecolor='k', alpha=.1)
plt.axvspan(127.7, 168.9, edgecolor='None', facecolor='k', alpha=.1)
plt.axvspan(196.2, 247.5, edgecolor='None', facecolor='k', alpha=.1)

plt.axvspan(85, 95, edgecolor='None', facecolor='k', alpha=.2)
plt.axvspan(145, 155, edgecolor='None', facecolor='k', alpha=.2)
plt.axvspan(215, 225, edgecolor='None', facecolor='k', alpha=.2)

ax.plot(porex1sim_f, np.poly1d(np.polyfit(porex1sim_f, porex1sim_t, 100))(porex1sim_f), label="14.75mil Stock Porex", linewidth=2.0, color='red')
ax.plot(porex1sim_f, porex1sim_t, color='red')

ax.plot(porex2sim_f, np.poly1d(np.polyfit(porex2sim_f, porex2sim_t, 100))(porex2sim_f), label="13.29mil Compressed Porex", linewidth=2.0, color='green')
ax.plot(porex2sim_f, porex2sim_t, color='green')

ax.plot(zitex1sim_f, np.poly1d(np.polyfit(zitex1sim_f, zitex1sim_t, 100))(zitex1sim_f), label="15.25mil Stock Zitex", linewidth=2.0, color='blue')
ax.plot(zitex1sim_f, zitex1sim_t,color='blue')

ax.plot(zitex2sim_f, np.poly1d(np.polyfit(zitex2sim_f, zitex2sim_t, 100))(zitex2sim_f), label="12.10mil Compressed Zitex", linewidth=2.0, color='magenta')
ax.plot(zitex2sim_f, zitex2sim_t, color='magenta')

plt.title('FTS Sim: Dimensions before and 48 Hours after Lamination', fontsize=20)
plt.suptitle('Porex and Zitex ePTFE', fontsize=24, fontweight='bold')
plt.grid(True)
plt.legend( loc=3, ncol=2, mode="expand", borderaxespad=0., fontsize=18)

major_ticks = np.arange(0, 301, 10)
minor_ticks = np.arange(0, 301, 5)
ymajor_ticks = np.arange(.65, 1, .025)
yminor_ticks = np.arange(.65, 1, .0125)

ax.set_yticks(ymajor_ticks)
ax.set_yticks(yminor_ticks, minor=True)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)




def averageBand(f,t, c='black', x=.8):
    low = np.ma.masked_inside(f, 79.4, 107.2)
    lowmask = np.ma.getmask(low)
    mid = np.ma.masked_inside(f, 127.7, 168.9)
    midmask = np.ma.getmask(mid)
    high = np.ma.masked_inside(f, 196.2, 247.5)
    highmask = np.ma.getmask(high)

    plt.text(90, x, str(np.round(np.mean(t[lowmask]),4)), fontsize=18, color=c)
    plt.text(145, x, str(np.round(np.mean(t[midmask]),4)), fontsize=18, color=c)
    plt.text(220, x, str(np.round(np.mean(t[highmask]),4)), fontsize=18, color=c)

averageBand(porex1sim_f, porex1sim_t, 'red', .8)
averageBand(porex2sim_f, porex2sim_t, 'green', .775)
averageBand(zitex1sim_f, zitex1sim_t, 'blue', .75)
averageBand(zitex2sim_f, zitex2sim_t, 'magenta', .725)

ax.add_patch(patches.Rectangle(
    (80, .715),
    167,
    .11,
    fill=False))      # remove background
plt.text(120, .8125, "Mean Across Light Grey Regions", fontsize=20)

plt.show()