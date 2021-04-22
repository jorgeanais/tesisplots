import matplotlib.pyplot as plt
from apolo.data import dirconfig, objects
from apolo.catalog_proc.utils import read_fits_table
import mpl_scatter_density
from astropy.visualization import LogStretch
from astropy.visualization.mpl_normalize import ImageNormalize
import matplotlib.patches as mpatches


def make_photerror_plot(tile):
    """
    This function produces a photometry error plot for bands J, H and Ks using given tile.
    :param tile:
    :return:
    """
    file = tile.get_file(data_dir)
    table = read_fits_table(file)

    fig = plt.figure()
    ax1 = fig.add_subplot(311, projection='scatter_density')
    ax2 = fig.add_subplot(312, projection='scatter_density')
    ax3 = fig.add_subplot(313, projection='scatter_density')
    fig.subplots_adjust(hspace=0)
    fig.suptitle(f'Photometric error for tile {tile.name}')

    norm = ImageNormalize(vmin=0., vmax=1000, stretch=LogStretch())

    ax1.scatter_density(table['mag_J'], table['er_J'], color='blue', norm=norm, label='J')
    ax2.scatter_density(table['mag_H'], table['er_H'], color='green', norm=norm, label='H')
    ax3.scatter_density(table['mag_Ks'], table['er_Ks'], color='red', norm=norm, label='Ks')
    ax3.set_xlabel('Magnitudes')

    # Hide x labels and tick labels for all but bottom plot. Tweak default plot configuration
    for ax,lbl in zip([ax1, ax2, ax3], ['J', 'H', 'Ks']):
        ax.label_outer()
        ax.set_ylim(-0.05, 0.4)
        ax.set_xlim(9.9, 22.1)
        red_patch = mpatches.Patch(label=lbl, alpha=0.00)
        ax.legend(handles=[red_patch], loc='upper left', markerscale=0, markerfirst=False, framealpha=0.00)
        ax.set_ylabel(r'$\sigma$')

    fig.savefig(f'figphoterr_{tile.name}_v2.png', overwrite=True)
    fig.clf()


if __name__ == "__main__":
    data_dir = dirconfig.proc_vvv
    tiles = [objects.t067, objects.t068, objects.t069, objects.t070, objects.t105, objects.t106, objects.t107,
             objects.t108]

    for tile in tiles:
        make_photerror_plot(tile)

