import matplotlib.pyplot as plt
from apolo.data import dirconfig, objects
from apolo.catalog_proc.utils import read_fits_table
import numpy as np

def make_completeness_plot(tile, data_dir):
    """
    This function produces a completeness histograms for all J, H and Ks bands for a given tile.
    :param data_dir:
    :param tile:
    :return:
    """
    file = tile.get_file(data_dir)
    table = read_fits_table(file)

    fig, axs = plt.subplots(3, sharex=True, sharey=True, gridspec_kw={'hspace': 0})
    fig.suptitle(f'Histogram of magnitudes per band for tile {tile.name}')

    kwargs = dict(histtype='stepfilled', alpha=0.5, ec="k")
    start = 4
    stop = 21
    bin_width = 0.25
    hbins = np.arange(start, stop, bin_width)
    axs[0].hist(table['mag_J'], bins=hbins, label='J (VVV/2MASS)', color='b', **kwargs)
    axs[0].hist(table['mag_J'][table['catalog']=='2MASS'], bins=hbins, label='J (2MASS)', color='darkblue', **kwargs)
    axs[1].hist(table['mag_H'], bins=hbins, label='H (VVV/2MASS)', color='g', **kwargs)
    axs[1].hist(table['mag_H'][table['catalog'] == '2MASS'], bins=hbins, label='H (2MASS)', color='darkgreen', **kwargs)
    axs[2].hist(table['mag_Ks'], bins=hbins, label='Ks (VVV/2MASS)', color='r', **kwargs)
    axs[2].hist(table['mag_Ks'][table['catalog'] == '2MASS'], bins=hbins, label='Ks (2MASS)', color='darkred', **kwargs)
    axs[2].set_xlabel('Magnitudes')

    # Hide x labels and tick labels for all but bottom plot. Tweak some default plot configuration
    for ax in axs:
        ax.label_outer()
        ax.set_yscale('log')
        ax.set_ylim(0.5,  590400)
        #ax.set_xlim(9.9, 22.1)
        ax.legend(loc='upper left', markerscale=0, markerfirst=True, framealpha=0.00)
        #ax.set_ylabel(r'$\sigma$')

    fig.savefig(f'fighist_{tile.name}.png', overwrite=True)
    fig.clf()


if __name__ == "__main__":
    data_dir = dirconfig.cross_vvv_2mass
    tiles = [objects.t067, objects.t068, objects.t069, objects.t070, objects.t105, objects.t106, objects.t107,
             objects.t108]

    for tile in tiles:
        make_completeness_plot(tile, data_dir)

