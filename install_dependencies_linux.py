import requests
from os import system
from subprocess import call
from sys import version_info
from urllib.request import urlretrieve


def install_pip():
    while True:
        distro_id = int(input(
            "Please select your linux distro (1. Ubuntu/Debian, 2. Arch, 3. Fedora, 4. OpenSUSE): ")) - 1
        commands = [['sudo apt install python3-pip'], ['sudo pacman -S python-pip'],
                    ['sudo yum install epel-release', 'sudo yum install python3-pip'], ['sudo zypper install python3-pip']]
        try:
            for command in commands[distro_id]:
                c = command.split()
                call(c)
        except:
            print("There was an error. Please try again.")
            continue
        else:
            print("Pip Installed Successfully!")
            break


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

    modules = ['SpeechRecognition', 'gTTS', 'pydub',
               'requests', 'geocoder', 'func-timeout']
    for module in modules:
        if module not in [installed[1] for installed in iter_modules()]:
            print(f"Installing {module}...")
            try:
                call(['pip3', 'install', module])
                call(['pip', 'install', module])
            except:
                pass
            system('clear')
            print(f"Installed {module} successfully!")
    print("All dependencies are installed!")
    quit()


def beep_and_could():
    urlretrieve(
        'https://drive.google.com/uc?export=download&id=1f1UHs2yZ-LZP7yq5RdqvPGnHjjP0WG9O',
        'beep.mp3')
    urlretrieve(
        'https://drive.google.com/uc?export=download&id=1g6wM9N05Zem1rwSbJnG9N0PC1MNR487A',
        'couldYouSayThatAgain.mp3'
    )


install_modules()
beep_and_could()
