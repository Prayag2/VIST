import requests
from subprocess import call
from sys import version_info


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
  pip_path = join(prefix, 'bin', 'pip3')
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
  print("All dependencies are installed!")
  quit()


def beep():
  beep = requests.get(
      'https://drive.google.com/uc?export=download&id=1f1UHs2yZ-LZP7yq5RdqvPGnHjjP0WG9O'
  )
  open('beep.mp3', 'wb').write(beep.content)


install_modules()
beep()
