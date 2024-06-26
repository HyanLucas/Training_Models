import os
import tarfile
import urllib

def download_extract_data(url, path, name):
    os.makedirs(path, exist_ok=True)
    tgz_path = os.path.join(path, name)
    urllib.request.urlretrieve(url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=path)
    housing_tgz.close()