import requests
from subprocess import call
from sys import version_info


def install_modules():
    # Import modules
    from pkgutil import iter_modules

    modules = ['SpeechRecognition', 'gTTS', 'pydub', 'requests', 'geocoder']
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
