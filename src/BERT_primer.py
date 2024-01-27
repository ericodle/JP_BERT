"""
Welcome to this short BERT primer using a few Japanese example sentences.

The aim of this primer is to familiarize you with the mathematical basis by which artifical neural networks manipulate text to perform complex NLP tasks.
"""

# We used the transformers library for this project.
# MeCab should already be installed in your environment.
pip install transformers==3.0.2

import torch
from transformers.modeling_bert import BertModel
from transformers.tokenization_bert_japanese import BertJapaneseTokenizer

# comment here
tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
model = BertModel.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
print(model)

from transformers import BertConfig
config_japanese = BertConfig.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')

# We can print the entire BERT layout. It's big, as you can see.
print("Confirm BERT architecture below:"
print(config_japanese)

"""
write about the text approach here
"""
      
text1 = "会社をクビになった。"
text2 = "テレワークばかりでクビが痛い。"
text3 = "会社を解雇された。"
      
input_ids1 = tokenizer.encode(text1, return_tensors='pt')  #pt stands for "pytorch"

print("Check the text and token IDs for Text 1:")
print(tokenizer.convert_ids_to_tokens(input_ids1[0].tolist()))  # print the Japanese text
print(input_ids1)  # print the corresponding ids for the characters

input_ids2 = tokenizer.encode(text2, return_tensors='pt')  

print("Check the text and token IDs for Text 2:")
print(tokenizer.convert_ids_to_tokens(input_ids2[0].tolist()))  
print(input_ids2)
      
input_ids3 = tokenizer.encode(text3, return_tensors='pt') 

print("Check the text and token IDs for Text 3:")
print(tokenizer.convert_ids_to_tokens(input_ids3[0].tolist()))  
print(input_ids3)
      
      
result1 = model(input_ids1)
 
print("The first tensor of result1 is of shape:" result1[0].shape)
print("The second tensor of result1 is of shape:" result1[1].shape)

"""
Result1[0] contains 1 row, 9 columns... and 768 elements in the third dimension.

"1" represents the number of batches, "9" represents the 9 ids that we fed into BERT from text1, and "768" represents the dimensions of each input id.

Result1[1] contains 1 row and 768 colums (or rather, a list of 768 numbers).

Now, let's feed text2 and text3 into BERT and get result2 and result3.
"""
      
result2 = model(input_ids2)
result3 = model(input_ids3)
      
"""
Each word in BERT is represented by a 768-dimensional vector.

Before we fed the text into BERT, those vector values were determined by the dictionary/tokenizer.

After we fed the text through BERT, the 768 dimensions of each vector (word) was changed!

Now, we can compare the outputs for each sentence and do some mathematical comparisons.

Let's consider two words in our example sentences: "クビ" and "解雇".

First, we will identify the target words in our three results.
"""

word_vec1 = result1[0][0][3][:]  # ”クビ” in text1 (id #3)
word_vec2 = result2[0][0][5][:]  # ”クビ” in text2（id #5）
word_vec3 = result3[0][0][3][:]  # ”解雇” in text3（id #3）

"""
We can confirm that the vectors for ”クビ” have changed based on the surrounding words in its sentences.

In other words, the vectors have changed due to both the BERT model training and the input sentence context.

We can print the vectors for 'クビ' from Text 1 and Text 2 and see the change for ourselves.
"""
 
print("Output 'クビ' from Text 1"+'\n')
print(word_vec1)
print("Output 'クビ' from Text 2"+'\n')
print(word_vec2)
      
"""
We can now start asking mathematical questions!

"Is the meaning of ”クビ” in Text 1 more similar to the meaning of ”クビ” in Text 2? Or, is the meaning of ”クビ” in Text 1 more similar to the meaning of ”解雇” in Text 3?"

One way to answer this question is to use Cosine Similarity, which follows the formula:

similarity=max(∥x1​∥2​⋅∥x2​∥2​,ϵ)x1​⋅x2​​

Fortunately, PyTorch has a built-in Cosine Similarity function.
"""
      
cos = torch.nn.CosineSimilarity(dim=0)

# similarity between 'クビ' in Text 1 and Text 2 
cos_sim_12 = cos(word_vec1, word_vec2)
# similarity between 'クビ' in Text 1 and Text 3 
cos_sim_13 = cos(word_vec1, word_vec3)

print("Similarity between 'クビ' in Text 1 and Text 2: " cos_sim_12)
print("Similarity between 'クビ' in Text 1 and Text 2: " cos_sim_13)
      
"""
The cosine similarity between ”クビ” in Text 1 and Text 2 is 0.66, whereas the similarity between ”クビ” in Text 1 and ”解雇” in Text 3 is 0.78.

Therefore, the meaning of ”クビ” in Text 1 and the meaning of ”解雇” in Text 3 is more similar than the meanings of ”クビ” in Text 1 and Text 2.

This is correct, as the ”クビ” in Text 1 refers to getting fired from a job (”解雇”) not the anatomical "neck" meaning in Text 2.
"""
