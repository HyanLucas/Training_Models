import os
import urllib.request
import matplotlib.pyplot as plt

def save_fig(fig_id, images_path, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(images_path, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

def download_image(download_url, save_path):
    print("Downloading", save_path)
    urllib.request.urlretrieve(download_url, save_path)
