import urllib

def download_image(download_url, save_path):
    print("Downloading", save_path)
    urllib.request.urlretrieve(download_url, save_path)