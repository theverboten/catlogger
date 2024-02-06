import openai

API_KEY = open("API_KEY.txt", "r").read()
openai.api_key = API_KEY

log = []
userMessage = 'You are professor of physics talking to freshman in physics. You also answering his questions in under 10 words. What is Heisenberg uncertainty principle?'
chatRole = 'professor of physics talking to freshman in physics. You also answering his questions in under 10 words'

log.append({"role": "user", "content": userMessage})


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=log
)

professorResponse = response['choices'][0]['message']['content']
print("ChatGPT:", professorResponse.strip("\n").strip())
memory = open("memory.txt", "r+").write(professorResponse.strip("\n").strip())
print(memory)
