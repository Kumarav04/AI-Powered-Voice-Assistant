import openai
api_key = "*Enter you API key here*"
openai.api_key = api_key
def generate_response():
    myprompt = "Just want to check if you are working"
    response = openai.Completion.create(engine="text-davinci-002", prompt=myprompt, max_tokens=1000)

    # Convert response to text
    answer = response.choices[0].text

    # Convert text to speech
    return answer

print(generate_response())
