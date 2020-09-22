import matplotlib.pyplot as plt
from apolo.data import dirconfig, objects
from apolo.catalog_proc.utils import read_fits_table
import numpy as np

# -----------------------------

def make_photerror_plot(tile):
    """
    This function produces a photometry error plot for bands J, H and Ks using given tile.
    :param tile:
    :return:
    """
    file = tile.get_file(data_dir)
    table = read_fits_table(file)

    fig, axs = plt.subplots(3, sharex=True, sharey=True, gridspec_kw={'hspace': 0})
    fig.suptitle(f'Photometric error for tile {tile.name}')

    kargs_plot = dict(markersize=1.0, alpha=0.1)

    axs[0].plot(table['mag_J'], table['er_J'], '.', **kargs_plot, label='J', color='b')
    axs[1].plot(table['mag_H'], table['er_H'], '.', **kargs_plot, label='H', color='g')
    axs[2].plot(table['mag_Ks'], table['er_Ks'], '.', **kargs_plot, label='Ks', color='r')
    axs[2].set_xlabel('Magnitudes')

    # Hide x labels and tick labels for all but bottom plot. Tweak some default plot configuration
    for ax in axs:
        ax.label_outer()
        ax.set_ylim(-0.05, 0.4)
        ax.set_xlim(9.9, 22.1)
        ax.legend(loc='upper left', markerscale=0, markerfirst=False, framealpha=0.00)
        ax.set_ylabel(r'$\sigma$')

    fig.savefig(f'figphoterr_{tile.name}.png', overwrite=True)
    fig.clf()



data_dir = dirconfig.proc_vvv
tiles = [objects.t067, objects.t068, objects.t069, objects.t070, objects.t105, objects.t106, objects.t107, objects.t108]

for tile in tiles:
    make_photerror_plot(tile)
