# Python Assistant (VIST)

## Packages used:

- speech_recognition (`pip3 install SpeechRecognition`)
- gtts (`pip3 install gTTS`)
- pydub (`pip3 install pydub`)
- requests (`pip3 install requests`)

## Problems faced while installing packages

### Windows

There might be a problem while you try to install all the packages. First off, you require Microsoft Visual C++ build tools. And you need to pay attention while installing pyAudio too. Basically PyAudio has stopped supporting python 3.7 and above but we have a solution to this too. You just need to open IDLE and see the python version and the bit (either 64 or 32). When you have got hold of that then you have to download an appropriate `.whl` file from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio 'Click me'). To install the `.whl` file you need to open command prompt there and run `pip3 install <name of the file>.whl` or `pip install <name of the file>.whl`! After all this you must have a running copy of VIST.

- Install Python 3.XX, make sure to check the checkbox at the bottom! [See Image](https://doc-00-5s-docs.googleusercontent.com/docs/securesc/sh0ssa4qv9mf4q46unndk1pd2or408ao/obndsrpk9iscs93t5h5ru8mr79b01m8a/1597593300000/13338967790131960641/13338967790131960641/16KY_8RvC8r6H1B5VundREybiC-ZGVHZU?e=view&authuser=0&nonce=fhn1e2runlspa&user=13338967790131960641&hash=lssn74mpij54466sjcjfq08usl51fph9)
- Install Microsoft visual C++ build tools! [See Image](https://doc-0g-5s-docs.googleusercontent.com/docs/securesc/sh0ssa4qv9mf4q46unndk1pd2or408ao/5lufanmll3p3n9uprldftf80cm8m3ehu/1597593450000/13338967790131960641/13338967790131960641/1EIA5HzDIA2_aad8s1LJ_CMbSKAwfrtPO?e=view&authuser=0)
- Select an appropriate python version and architecture which is either amd64 (64bit) or 32bit! [See Image](https://doc-0s-5s-docs.googleusercontent.com/docs/securesc/sh0ssa4qv9mf4q46unndk1pd2or408ao/86r6eqti17flpt3a9fk5kfba0v053her/1597593525000/13338967790131960641/13338967790131960641/1ZWKnY-_QColkQRlQ5QYyqfWxiUlWUTx1?e=view&authuser=0)
- Enter `cmd` in start menu and navigate to the C:/ with `cd /` then type `cd /Users/<YourUserName>/<NameOfTheFolderInWhichYouDownloadedPyAudioWHL>` after that copy the name of the whl file with the extension `.whl`. Then execute `pip install <NameOfTheFile>.whl`! [See Image](https://doc-0o-5s-docs.googleusercontent.com/docs/securesc/sh0ssa4qv9mf4q46unndk1pd2or408ao/hkkffuam2h725d0cm8icqudhva0mep48/1597593675000/13338967790131960641/13338967790131960641/1pzxvJt-89Pmrc43Wz1BQYGrWbXs9fb1p?e=view&authuser=0&nonce=q3abpathqc698&user=13338967790131960641&hash=njramp6e95500amurj6tveii9hi3mb34)

#### OR

Install visual c++ build tools using the tutorial just above this
Run installer script first! Using `python install_dependencies_win.py`

### Linux

There might be a problem while you try to install all the packages. You need to pay attention while installing pyAudio too. Basically PyAudio has stopped supporting python 3.7 and above but we have a solution to this too. First, you might need to run this `sudo apt-get install python3-pyaudio python-pyaudio`! If the version in the repositories are old, then you'll have to run `sudo apt-get install python3-pyaudio python-pyaudio portaudio19-dev` After all this you must have a running copy of VIST.

#### OR

Run installer script first! Using `python3 install_dependencies_linux.py`

## Commands that can be used for

### Getting help

- What can you do?
- Help
- What are your abilities

### Getting updates of the coronavirus in India

- Covid status
- Covid
- Corona
- Corona Virus
- Covid-19 status
- Corona Status
- Coronavirus
- Covid-19

### Getting a joke

- Crack a joke
- Tell me a joke
- Tell me something funny
- Or may contain: Joke, Fun, Laugh

### Getting date and time

- It should include: date or time

### Getting what VIST is doing

- Sup
- What are you doing
- Or should contain doin

### Getting what VIST is doing

- How are you
- How have you been
- How is it going

### Starting a countdown from a given second

- You must say countdown

## Getting the pronunciation of a word

- Should contain the word pronunciation
- How is this word pronounced
- How do you speak this

## Getting to know the config.txt

The `config.txt` is a file that stores your name for further use. If you edit your name in the file, nothing happens, but if it finds something else, it will generate the file again by again asking your name!
