try:
  # external modules
  import speech_recognition as sr  # for speech to text
  from gtts import gTTS  # google text to speech
  from pydub.playback import play  # audio manipulator
  from pydub import AudioSegment  # audio manipulator
  import requests  # for APIs

  # built-in modules
  from random import choice  # gives random choice in a list
  from ast import literal_eval  # ast module
  from sys import platform, version_info, exit  # system module
  from os import system, name, path, remove  # os module
  import webbrowser as wb  # web browser
  from time import sleep  # sleep
  from datetime import datetime

except ImportError:
  # if modules are not intalled, install them
  print("Please install the pre-requisites")
  quit()


# Variables
beep = 'beep.mp3'
data = {}
greetings = ['Namaste', 'Ram Ram', 'Jai Jinendra',
             'Jai Shri Krishna', 'Satsriaakaal', 'Hello', 'Hi']
what_am_i_doing_list = ['I am talking to you right now!',
                        'I know everything, so i am chilling!',
                        "I'm drinking tea.",
                        "I'm preparing for J.E.E. Advance for the past 10 years but cannot clear it!!",
                        "Damn, you woke me up! I was sleeping bruh."]
how_am_i_list = ['Talking to you makes me feel great!',
                 "I'm depressed. Anyways...",
                 "I'm great but you should be studying right now...",
                 "I don't have any feelings, bruh.",
                 "I think I will not be able to make it through the day!"]

# API URLs
covid_api_url = 'https://api.rootnet.in/covid19-in/stats/latest'
joke_api_url = 'https://official-joke-api.appspot.com/jokes/random'


# Utility functions
def cls():
  # Clear the console
  system('cls') if name == 'nt' else system('clear')


def save_to_file(data):
  # Save data to file
  with open('config.txt', 'w') as file:
    file.write(str(data))


def is_internet_active():
  # Check if the user has an active internet connection
  # By requesting Google's search engine
  try:
    _ = requests.get('https://www.google.com', timeout=1)
    return True
  except requests.ConnectionError:
    return False


def exitam():
  # Exit the program with goodbye message!
  speak("It was nice talking to you, hope to see you soon!")
  remove('speech.mp3')
  quit()


# Request and response function
def listen():
  # Configure the recognizer
  r = sr.Recognizer()
  # Listen the microphone for any voice
  with sr.Microphone() as source:
    # Adjust mic according to ambient noise
    r.adjust_for_ambient_noise(source, duration=0.5)
    print("Listening...")
    # Play the beep
    play(AudioSegment.from_mp3(beep))
    # Make a variable with the listened voice
    audio = r.listen(source)
  try:
    # Recognize the audio using Google
    print(r.recognize_google(audio))
    # Play the recognized audio
    play(AudioSegment.from_mp3(beep))
    return r.recognize_google(audio)
  except sr.UnknownValueError:
    # If voice isn't recognized
    speak("Could you say that again?")


def speak(text):
  # Print what the user has spoken
  print(text)
  # If user is running this on Windows, then set FFMPEG path
  if name == 'nt':
    ffmpeg = 'ffmpeg.exe'
    AudioSegment.converter = ffmpeg
  else:
    pass
  # Name of the mp3 to be played
  mp3 = 'speech.mp3'
  txt2speech = gTTS(text=text, lang='en-in')
  # Save the audio as speech.mp3
  txt2speech.save(mp3)
  # Play the saved audio
  play(AudioSegment.from_mp3(mp3))


# Common functions
def web_search(q):
  exceptions = ['search', 'search for', 'tell me about', 'what is']
  query = ''
  for exception in exceptions:
    if exception in q:
      q = q.replace(exception, '')
  query = q.split()
  parsed_query = '+'.join(query)  # Replace spaces with '+' sign
  google_url = f'https://www.google.com/search?q={parsed_query}'
  speak("Here's what I found!")
  wb.open_new_tab(google_url)


# API functions
def india_covid():
  try:
    # Get information about the covid in form of a JSON file
    res = requests.get(covid_api_url)
    res.raise_for_status()
  # Look for errors and report to the user
  except (requests.HTTPError, Exception, requests.exceptions.ConnectionError):
    print("Please check your network connection.")
  else:
    # Store data as JSON temporarily in a variable
    rJSON = res.json()
    # Extract data from JSON
    data = rJSON['data']
    # Speak out the extracted data
    speak(
        f"Total cases of COVID-19 in India are {data['summary']['total']}; whereas {data['summary']['discharged']} have been discharged and {data['summary']['deaths']} people died!"
    )


def jokeAPI():
  try:
    # Try to connect to the endpoint of the API
    res = requests.get(joke_api_url)
    res.raise_for_status()
  # Look for errors and report them
  except (requests.HTTPError, Exception, requests.exceptions.ConnectionError):
    print("Please check your network connection.")
  else:
    # Store data as JSON temporarily in a variable
    json = res.json()
    # Speak out the extracted joke setup
    speak(json['setup'])
    # Wait for 1 second
    sleep(1)
    # Speak out the extracted joke punchline
    speak(json['punchline'])


# Commands' functions
def date_time():
  # Get the current time
  now = datetime.now()
  # Create a date string
  dt_string = now.strftime("%d/%m/%Y. And the time is %H:%M:%S!")
  # Speak out today's date and time
  speak(f"Today is {dt_string}")


def hi():
  # Speak hi while blushing ;)
  speak(f'*blushing* {choice(greetings)} ji!')


def show_abilities():
  # Tell about VIST's abilities
  speak(
      "I can do math, crack some jokes and search the web for you! Try entering, 'tell me a joke'."
  )


def solve():
  # Solves an expression
  while True:
    # Wait for user to enter an expression
    try:
      # Speak out
      speak("Enter an expression.")
      # User enters the expression
      exp = input("? ")
      # The expression is evaluated
      eval_exp = eval(exp)
    except:
      # If the expression is incorrect, report the user
      speak("Please enter a correct expression!")
      continue
    else:
      # Speak out the evaluated expression
      speak(str(eval_exp))
      break


def pronunciation():
  # Pronounces the given word
  while True:
    # VIST speaks out
    speak("Which word's pronunciation do you want to check?")
    # User enters the word
    word = input("? ").lower()
    # Check if the word is all alphabets
    if word.isalpha():
      # Speak out
      speak(f'This word is pronounced as {word}!')
    else:
      # Speak out
      speak(f"Please enter a correct word {data['name']}!")


def feedback():
  # Ask for feedback
  speak("Please send your feedback:")
  speak("axityatrips@gmail.com")
  speak("prayagjain2@gmail.com")


def countdown():
  # User enters the countdown time
  sec = int(input("Enter seconds for the countdown\n? "))
  while sec > 0:
    # Print the second
    print(sec)
    # Wait one second
    sleep(1)
    # Decrement second by one
    sec -= 1
  # Play the beep
  play(AudioSegment.from_mp3(beep))


def what_am_i_doing():
  # Speak out what VIST is doing
  speak(choice(what_am_i_doing_list))


def how_am_i():
  # Check how is VIST
  speak(choice(how_am_i_list))


def cmd_prompt():
  # Run functions corresponding to a command
  # list of commands corresponding to their functions
  commands = [
      {'trigger_on': ['what can you do', 'help',
                      'what you can do', 'what are your abilities'], 'func': show_abilities, 'args_required': False},
      {'trigger_on': ['covid status', 'covid', 'corona', 'corona virus', 'covid-19 status',
                      'corona status', 'corona virus status', 'covid-19', 'coronavirus'], 'func': india_covid, 'args_required': False},
      {'trigger_on': ['calculate', 'solve',
                      'calculator', 'evaluate'], 'func': solve, 'args_required': False},
      {'trigger_on': ['search', 'web search', 'web', 'search for', 'tell me about', 'what is'],
       'func': web_search, 'args_required': True},
      {'trigger_on': ['crack a joke', 'tell me a joke', 'joke', 'fun', 'laugh',
                      'make me laugh', 'tell me something funny'], 'func':jokeAPI, 'args_required': False},
      {'trigger_on': ['bye', 'exit', 'good bye'],
       'func': exitam, 'args_required': False},
      {'trigger_on': ['date', 'time'],
       'func': date_time, 'args_required': False},
      {'trigger_on': greetings, 'func': hi, 'args_required': False},
      {'trigger_on': ['what are you doing',
                      'doing'], 'func': what_am_i_doing, 'args_required': False},
      {'trigger_on': ['how are you', 'how have you been doing',
                      'how is it going'], 'func': how_am_i, 'args_required': False},
      {'trigger_on': ['pronunciation', 'how is this word pronounced',
                      'pronounced', 'how do you speak this'], 'func': pronunciation, 'args_required': False},
      {'trigger_on': ['support', 'feedback'],
       'func': feedback, 'args_required': False},
      {'trigger_on': ['countdown'], 'func': countdown, 'args_required': False},
  ]
  # Ask the user, 'How may I help you'.
  speak("How may I help you?")
  # Run the code block inside, unless the loop is broken.
  while True:
    try:
      # Listen for the command
      inp = listen().lower()
    except AttributeError:
      # If there's an error, continue to the top and ask again.
      continue
    else:
      # Internet search is set to True by default
      internet_search = True
      # For each dictionary in the commands list
      for dictionary_index in range(len(commands)):
        # For each sentence in the 'trigger_on' list.
        for keysentence in commands[dictionary_index]['trigger_on']:
          # If the user input contains the keysentence,
          # Then run its corresponding # function and set internet search to true
          if keysentence.lower() in inp:
            # pass arguments if arguments are requie
            if commands[dictionary_index]['args_required']:
              commands[dictionary_index]['func'](inp)
            else:
              commands[dictionary_index]['func']()
            internet_search = False
            break
        else:
          # If user input doesn't match any of the sentences in the 'trigger_on'
          # list, then look in the next dictionary
          continue
      else:
        if internet_search:
          # Search the internet for unrecognized commands
          web_search(inp)


def main():
  global data

  def save_to_file(data):
    with open('config.txt', 'w') as file:
      file.write(str(data))

  # Save details in a config file
  def save_config(key, value):
    data[str(key)] = value
    save_to_file(data)

  # Check if config.txt exists
  if path.isfile('config.txt'):
    # If yes then read config.txt
    with open('config.txt', 'r') as file:
      try:
        # Store the data in a variable
        data = literal_eval(file.read())
      except:
        # If data is corrupted
        speak('Your data is corrupted. Clearing cache...')
        # Remove config file and run main again
        remove('config.txt')
        main()
      else:
        # Speak one of the greetings in the greetings list and the name of the user
        speak(f"{choice(greetings)}, {data['name']}!")
  else:
    speak("Hey there! I am Vist, your virtual and personal assistant! Can you please enter your name?")
    name = input("? ")
    speak(f'That\'s a nice name, {name}!')
    save_config('name', name)


if __name__ == "__main__":
  if is_internet_active():
    cls()
    main()
    cmd_prompt()
  else:
    print("Connect to a working network and try again!")
