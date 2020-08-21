from subprocess import call
from sys import version_info
from struct import calcsize
from zipfile import ZipFile
from os import system, name, getcwd, path, remove
from time import sleep
from urllib.request import urlretrieve


def install_modules():
    # Import modules
    from pkgutil import iter_modules

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
            print(f"Installed {module} successfully!")
        else:
            print(f"{module} is already installed! Skipping it...")
    print("All dependencies are installed!")


def download():
    print("Installing PyAudio")
    pyaudio_zip_link = 'https://drive.google.com/uc?export=download&id=1q9HjIlCV26hfZMN1bZeZGpQib9OJGwe_'
    zip_file_name = 'pyaudio.zip'
    urlretrieve(pyaudio_zip_link, zip_file_name)
    if version_info[0] < 3:
        raise Exception('You should be using Python 3.XX!')
    elif version_info[0] >= 3:
        if version_info[1] == 9:
            if calcsize("P"*8) == 32:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio-0.2.11-cp39-cp39-win32.whl')
                    call(['pip', 'install', 'PyAudio-0.2.11-cp39-cp39-win32.whl'])
                remove('PyAudio-0.2.11-cp39-cp39-win32.whl')
                remove('pyaudio.zip')
            else:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio-0.2.11-cp39-cp39-win_amd64.whl')
                    call(['pip', 'install', 'PyAudio-0.2.11-cp39-cp39-win_amd64.whl'])
                remove('PyAudio-0.2.11-cp39-cp39-win_amd64.whl')
                remove('pyaudio.zip')

        elif version_info[1] == 8:
            if calcsize("P"*8) == 32:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio-0.2.11-cp38-cp38-win32.whl')
                    call(['pip', 'install', 'PyAudio-0.2.11-cp38-cp38-win32.whl'])
                remove('PyAudio-0.2.11-cp38-cp38-win32.whl')
                remove('pyaudio.zip')
            else:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio-0.2.11-cp38-cp38-win_amd64.whl')
                    call(['pip', 'install', 'PyAudio-0.2.11-cp38-cp38-win_amd64.whl'])
                remove('PyAudio-0.2.11-cp38-cp38-win_amd64.whl')
                remove('pyaudio.zip')

        elif version_info[1] == 7:
            if calcsize("P"*8) == 32:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio-0.2.11-cp37-cp37m-win32.whl')
                    call(['pip', 'install', 'PyAudio-0.2.11-cp37-cp37m-win32.whl'])
                remove('PyAudio-0.2.11-cp37-cp37m-win32.whl')
                remove('pyaudio.zip')
            else:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio-0.2.11-cp37-cp37m-win_amd64.whl')
                    call(['pip', 'install', 'PyAudio-0.2.11-cp37-cp37m-win_amd64.whl'])
                remove('PyAudio-0.2.11-cp37-cp37m-win_amd64.whl')
                remove('pyaudio.zip')

        elif version_info[1] == 6:
            if calcsize("P"*8) == 32:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio‑0.2.11‑cp36‑cp36m‑win32.whl')
                    call(['pip', 'install', 'PyAudio‑0.2.11‑cp36‑cp36m‑win32.whl'])
                remove('PyAudio‑0.2.11‑cp36‑cp36m‑win32.whl')
                remove('pyaudio.zip')
            else:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl')
                    call(['pip', 'install', 'PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl'])
                remove('PyAudio‑0.2.11‑cp36‑cp36m‑win_amd64.whl')
                remove('pyaudio.zip')

        elif version_info[1] == 5:
            if calcsize("P"*8) == 32:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio‑0.2.11‑cp35‑cp35m‑win32.whl')
                    call(['pip', 'install', 'PyAudio‑0.2.11‑cp35‑cp35m‑win32.whl'])
                remove('PyAudio‑0.2.11‑cp35‑cp35m‑win32.whl')
                remove('pyaudio.zip')
            else:
                with ZipFile(zip_file_name) as z:
                    z.extract('PyAudio‑0.2.11‑cp35‑cp35m‑win_amd64.whl')
                    call(['pip', 'install', 'PyAudio‑0.2.11‑cp35‑cp35m‑win_amd64.whl'])
                remove('PyAudio‑0.2.11‑cp35‑cp35m‑win_amd64.whl')
                remove('pyaudio.zip')
        else:
            print("Please upgrade your python to 3.5 or higher")
            raise Exception('Upgrade your python installation')


def ff(name, link):
    if not path.isfile(name):
        print(f"Downloading", name)
        urlretrieve(link, name)


def beep_and_could():
    urlretrieve(
        'https://drive.google.com/uc?export=download&id=1f1UHs2yZ-LZP7yq5RdqvPGnHjjP0WG9O',
        'beep.mp3'
    )
    urlretrieve(
        'https://drive.google.com/uc?export=download&id=1g6wM9N05Zem1rwSbJnG9N0PC1MNR487A',
        'couldYouSayThatAgain.mp3'
    )


install_modules()

download()
beep_and_could()
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
