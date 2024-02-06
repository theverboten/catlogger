import openai


def get_advice(task):
    API_KEY = open("API_KEY.txt", "r").read()
    openai.api_key = API_KEY
    # QUESTION = open("question.txt", "r").read()
    QUESTION = task

    log = []
    userMessage = 'Imagine you are a therapeutic cat, which gives people advice with possible solution to their problems.  You also answering under 12 words.' + QUESTION
    chatRole = 'therapeutic cat talking to youre pacient. You also answering his questions in under 12 words'

    log.append({"role": "user", "content": userMessage})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=log
    )

    professorResponse = response['choices'][0]['message']['content']
    print("ChatGPT:", professorResponse.strip("\n").strip())
    memory = open(
        "memory.txt", "r+").write(professorResponse.strip("\n").strip())

    MPTEXT = professorResponse.strip("\n").strip()
    return MPTEXT
