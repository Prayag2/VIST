import requests
from subprocess import call
from sys import version_info
from struct import calcsize
from zipfile import ZipFile
from os import system, name, getcwd, path, remove
from time import sleep


def install_pip():
  from os import remove
  from urllib.request import urlretrieve
  print("Installing pip...")

  # Download get-pip.py
  urlretrieve("https://bootstrap.pypa.io/get-pip.py", 'get-pip.py')
  call(['python3', 'get-pip.py'])
  call(['python', 'get-pip.py'])

  # Remove file after downloading
  remove('get-pip.py')


def install_modules():
  # Import modules
  from os.path import isfile, join
  from sys import prefix
  from pkgutil import iter_modules

  # Check if pip is installed
  pip_path = join(prefix, 'Scripts', 'pip.exe')
  if not isfile(pip_path):
    install_pip()
    # Check again
    if not isfile(pip_path):
      # Raise error if couln't install pip
      print("Failed to find or install pip! Please install it manually!")
      quit()

  modules = ['SpeechRecognition', 'gTTS', 'pydub', 'requests']
  for module in modules:
    if module not in [installed[1] for installed in iter_modules()]:
      print(f"Installing {module}...")
      call(['pip3', 'install', module])
      call(['pip', 'install', module])
      print(f"Installed {module} successfully!")
    else:
      print(f"{module} is already installed! Skipping it...")
  print("All dependencies are installed!")


def download():
  pyaudio_zip_link = 'https://drive.google.com/uc?export=download&id=1q9HjIlCV26hfZMN1bZeZGpQib9OJGwe_'
  zip_file_name = 'pyaudio.zip'
  req = requests.get(pyaudio_zip_link)
  open(zip_file_name, 'wb').write(req.content)

  if version_info[0] < 3:
    raise Exception('You should be using Python 3.XX!')
  elif version_info[0] >= 3:
    if version_info[1] == 9:
      if calcsize("P"*8) == 32:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio-0.2.11-cp39-cp39-win32.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio-0.2.11-cp39-cp39-win32.whl')
          system('pip install PyAudio-0.2.11-cp39-cp39-win32.whl')
        remove('PyAudio-0.2.11-cp39-cp39-win32.whl')
        remove('pyaudio.zip')
      else:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio-0.2.11-cp39-cp39-win32.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio-0.2.11-cp39-cp39-win_amd64.whl')
          system('pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl')
        remove('PyAudio-0.2.11-cp39-cp39-win_amd64.whl')
        remove('pyaudio.zip')

    elif version_info[1] == 8:
      if calcsize("P"*8) == 32:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio-0.2.11-cp38-cp38-win32.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio-0.2.11-cp38-cp38-win32.whl')
          system('pip install PyAudio-0.2.11-cp38-cp38-win32.whl')
        remove('PyAudio-0.2.11-cp38-cp38-win32.whl')
        remove('pyaudio.zip')
      else:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio-0.2.11-cp38-cp38-win_amd64.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio-0.2.11-cp38-cp38-win_amd64.whl')
          system('pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl')
        remove('PyAudio-0.2.11-cp38-cp38-win_amd64.whl')
        remove('pyaudio.zip')

    elif version_info[1] == 7:
      if calcsize("P"*8) == 32:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio-0.2.11-cp37-cp37m-win32.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio-0.2.11-cp37-cp37m-win32.whl')
          system('pip install PyAudio-0.2.11-cp37-cp37m-win32.whl')
        remove('PyAudio-0.2.11-cp37-cp37m-win32.whl')
        remove('pyaudio.zip')
      else:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio-0.2.11-cp37-cp37m-win_amd64.whl')
          system('pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl')
        remove('PyAudio-0.2.11-cp37-cp37m-win_amd64.whl')
        remove('pyaudio.zip')

    elif version_info[1] == 6:
      if calcsize("P"*8) == 32:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio‑0.2.11‑cp36‑cp36m‑win32.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio‑0.2.11‑cp36‑cp36m‑win32.whl')
          system('pip install PyAudio‑0.2.11‑cp36‑cp36m‑win32.whl')
        remove('PyAudio‑0.2.11‑cp36‑cp36m‑win32.whl')
        remove('pyaudio.zip')
      else:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl')
          system('pip install PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl')
        remove('PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl')
        remove('pyaudio.zip')

    elif version_info[1] == 5:
      if calcsize("P"*8) == 32:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio‑0.2.11‑cp35‑cp35m‑win32.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio‑0.2.11‑cp35‑cp35m‑win32.whl')
          system('pip install PyAudio‑0.2.11‑cp35‑cp35m‑win32.whl')
        remove('PyAudio‑0.2.11‑cp35‑cp35m‑win32.whl')
        remove('pyaudio.zip')
      else:
        url = 'https://download.lfd.uci.edu/pythonlibs/w3jqiv8s/PyAudio‑0.2.11‑cp35‑cp35m‑win_amd64.whl'
        with ZipFile(zip_file_name) as z:
          z.extract('PyAudio‑0.2.11‑cp35‑cp35m‑win_amd64.whl')
          system('pip install PyAudio‑0.2.11‑cp35‑cp35m‑win_amd64.whl')
        remove('PyAudio‑0.2.11‑cp35‑cp35m‑win_amd64.whl')
        remove('pyaudio.zip')
    else:
      print("Please upgrade your python to 3.5 or higher")
      raise Exception('Upgrade your python installation')


def ff(name, link):
  if not path.isfile(name):
    print(f"Downloading", name)
    tmp = requests.get(link)
    open(name, 'wb').write(tmp.content)


def beep():
  beep = requests.get(
      'https://drive.google.com/uc?export=download&id=1f1UHs2yZ-LZP7yq5RdqvPGnHjjP0WG9O'
  )
  open('beep.mp3', 'wb').write(beep.content)


install_modules()

download()
beep()
s = input(
    "Around 200mb will be downloaded, are you sure you want to continue (y/n)\n? ").lower()
if s == 'y':
  ff(
      'ffmpeg.exe',
      'https://drive.google.com/uc?export=download&id=1Txk3dUAWc0yb1iebK5Nk2OGu1nPuZj1u'
  )
  ff(
      'ffprobe.exe',
      'https://drive.google.com/uc?export=download&id=17Ed5EbghEqBUdHpqGZ0rvn7lVxPlkZqm'
  )
  ff(
      'ffplay.exe',
      'https://drive.google.com/uc?export=download&id=1Txk3dUAWc0yb1iebK5Nk2OGu1nPuZj1u'
  )
else:
  raise Exception(
      "You won't be able to run the program if you don't download!"
  )
