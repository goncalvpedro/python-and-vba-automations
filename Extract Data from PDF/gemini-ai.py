import textwrap

import google.generativeai as genai

from IPython.display import Markdown, display


GOOGLE_API_KEY = 'Your API key here.'

genai.configure(api_key=GOOGLE_API_KEY)


# To display the text in a more friendly way
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Check the avaiable models
for model in genai.list_models():
      if 'generateContent' in model.supported_generation_methods:
            print(model.name)

# Choosing a model
model = genai.GenerativeModel('gemini-1.0-pro')

# Giving the prompt
response = model.generate_content("Tell 5 recipes using rice", stream=True)

# Formatting the response text
for chunk in response:
  print(chunk.text)
  print("_"*80)


