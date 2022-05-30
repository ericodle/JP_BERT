import numpy as np
import pandas as pd
import csv
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForMaskedLM


def run_bert(sentence):
    with torch.no_grad():
        model = AutoModelForMaskedLM.from_pretrained("cl-tohoku/bert-large-japanese")
        
        # Load pre-trained model tokenizer
        tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-large-japanese")
        tokenize_input = tokenizer.tokenize(sentence)
        tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
        sen_len = len(tokenize_input)
        sentence_loss = 0.
"""
This FOR loop is the key component of our entire study.
Here we define the masking algorithm that calculates perplexity.
"""

    for i, word in enumerate(tokenize_input):
        # The input [MASK] is recognized by BERT as a masking token.
        tokenize_input[i] = '[MASK]'
        mask_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
        output = model(mask_input)
        prediction_scores = output[0]
        softmax = nn.Softmax(dim=0)
        ps = softmax(prediction_scores[0, i]).log()
        word_loss = ps[tensor_input[0, i]]
        sentence_loss += word_loss.item()
        tokenize_input[i] = word
    # Perplexity (ppl) is defined as the exponential of the negative ratio of sentence loss to sentence length.
    ppl = np.exp(-sentence_loss/sen_len)
    return ppl

sentences_file = pd.read_csv ('./N3_adverbs.csv')
sentences = pd.DataFrame(sentences_file, columns=['text', 'perplexity'])

output=[]
for i in range(0, len(sentences.text)):
    result=run_bert(sentences.text[i])
    output.append(result)

print(output)

