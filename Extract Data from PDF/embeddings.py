import pandas as pd
import pdf_reader
import google.generativeai as genai


GOOGLE_API_KEY = 'Your API key here'

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'embedContent' in m.supported_generation_methods:
    print(m.name)


response = pdf_reader.extractText()
title = response[0]

try:
  with open('extracted_text.txt', 'r') as f:
    sample_text = f.read()
except FileNotFoundError:
  print('File not found')
  response = pdf_reader.extractText()

sample_text = sample_text.split('*'*30 + '\n')

df = pd.DataFrame(sample_text, columns=['text']).drop_duplicates().drop(index=0).reset_index(drop=True)

df['text'] = df['text'].replace('\n', ' ', regex=True)

def embed_fn(text):
  model = 'models/embedding-001'
  return genai.embed_content(model=model,
                             content=text,
                             task_type="retrieval_document",
                             title=title)["embedding"]

df['embeddings'] = df.apply(lambda row: embed_fn(row['text']), axis=1)
print(df.head(50))