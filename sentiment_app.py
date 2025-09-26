
import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="kdrucshi/DistilBERT_IMDB")

import torch
def predictions(sentence):
  input_encode = tokenizer(sentence, truncation = True, padding = True,return_tensors="pt")
  device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
  input = {k:v.to(device) for k,v in input_encode.items()}
  output = model(**input)
  a = torch.argmax(output.logits)
  if a == 0:
    return "Negative"
  elif a == 1:
    return "Positive"

demo = gr.Interface(fn=predictions, inputs="textbox", outputs="textbox")

if __name__ == "__main__":
    demo.launch()
