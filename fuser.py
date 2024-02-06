import openai
from playsound import playsound
from google.cloud import texttospeech

API_KEY = open("API_KEY.txt", "r").read()
openai.api_key = API_KEY
QUESTION = open("question.txt", "r").read()

log = []
userMessage = 'You are professor of physics talking to freshman in physics. You also answering his questions in under 10 words.' + QUESTION
chatRole = 'professor of physics talking to freshman in physics. You also answering his questions in under 10 words'

log.append({"role": "user", "content": userMessage})


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=log
)

professorResponse = response['choices'][0]['message']['content']
print("ChatGPT:", professorResponse.strip("\n").strip())
memory = open("memory.txt", "r+").write(professorResponse.strip("\n").strip())

MPTEXT = professorResponse.strip("\n").strip()
print(MPTEXT)

# Instantiates a client
client = texttospeech.TextToSpeechClient()
TEXT = open("memory.txt", "r").read()
# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=MPTEXT)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output1.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output1.mp3"')

playsound(r'C:\Users\hp\Desktop\Psychologger\output1.mp3')
