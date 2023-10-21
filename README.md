<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://github.com/ericodle/JP_BERT/blob/main/JPBERT_workflow.jpg" alt="Logo" width="200" height="350">
  </a>

<h3 align="center">JP_BERT</h3>

  <p align="center">
  BERT is a transformer-based language model published in 2019 that has recently gained attention for its high Natural Language Processing (NLP) benchmark scores. This repository serves as a source of supplementary material for an NLP conference paper on Japanese-trained BERT (JP_BERT) currently under review. We herein archive our training data, Python scripts, raw BERT output, and statistical calculations for the reference of anyone interested.
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>

## Overview

Computer language models now perform comparably to humans on multiple NLP tasks, suggesting artificial intelligence (AI) is ready for the classroom. To further the adoption of AI as a learning tool, we herein evaluate a Japanese BERT language model (JPBERT) on an adverb test using a custom perplexity (PPX) output layer. Comparing raw PPX score, inter-question perplexity range (IQPR), and difference between the first and second lowest perplexity scores (2-1DIFF), we found that 2-1DIFF and IQPR significantly predicted correct JPBERT responses on an N3-level Japanese adverb test. Moreover, JPBERT was able to outperform human university students studying Japanese as a second language (72\% vs. 42.7\% accuracy). Our proposed perplexity model is a useful tool for language educators, particularly as an automated test screening method that objectively evaluates the difficulty of an exam.


<!-- ABOUT THE PROJECT -->
## Computer Assisted Language Learning (CALL)

Modern work on the application of computers in the L2 education classroom often fall under the banner of Computer Assisted Language Learning, or CALL. Within this field exists the subtopic of ICALL (Intelligent CALL) that aims to use artificial intelligence as a means of providing linguistic feedback to students. Such tools include E-Tutor for students of German, ICICLE for American Sign Language learners, and CASTLE for grammar correction through text-based role playing. For learning Japanese, the popularization of digital voice recorders, touch-screen displays, electronic dictionaries, and smartphone apps such as Duolingo and Kahoot! demonstrate the persistence of CALL in the language classroom．Following the trend of exploring intelligent computer systems to aid language learning, we herein focus on recent developments in deep neural network language models.

## Perplexity

Computer language models now perform comparably to humans on multiple NLP tasks, suggesting artificial intelligence is ready for the classroom. To further the adoption of AI as a learning tool, we herein evaluate a Japanese BERT language model (JP_BERT) on adverb understanding via a custom perplexity (PPX) output layer. Comparing raw PPX score, inter-question perplexity range (IQPR), and difference between the first and second lowest perplexity scores (2-1DIFF), we found that 2-1DIFF and IQPR significantly predicted correct JPBERT responses on an N3-level Japanese adverb test. Our proposed PPX model is a useful tool for language educators, particularly as an automated test screening method that objectively evaluates the difficulty of an exam.

**Perplexity**
$$Perplexity = \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

 wherein the softmax function $\sigma$ is defined as

**Softmax**
$$\sigma X_k = \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

The equations above defines our proposed perplexity measure. $\sigma{(x)}_i$ represents loss due to masking token i on output vector \textbf{x}, while n represents the total number of tokens in the input text. Equation 5 describes the softmax function, $\sigma$. For each element j in an output vector \textbf{z}, softmax calculates the mean of exponential values for $\textbf{z}_j$ for every element in \textbf{z} from k=1 to n.

<p align="right">(<a href="#top">back to top</a>)</p>

## Testing Results

JP_BERT correctly answered 72 of 100 multiple-choice adverb questions (72%) correctly. Assuming the null hypothesis that JP_BERT would correctly answer 25% of the questions correctly by chance, Mann-Whitney U testing found the model to score significantly higher (U=2650; P<0.00001) than chance. To evaluate the utility of our PPX layer in predicting adverb test accuracy, we performed significance testing using the Mann-Whitney U test again. JP_BERT accuracy (correct vs. incorrect answer groups) on the 100-response N3 adverb question set was significantly different with respect to 2-1DIFF (U=493; P=0.00004) and IQPR (U=625; P=0.00164), but not raw PPX output (PPX; U=888; P=0.17879). 

*Figure

Histograms showing the roughly normal distributions of input question lengths, generated perplexity (PPX) scores, and the derived measures 2-1DIFF and IQPR. All distributions were roughly normal, and non-representative outliers were omitted from the X-axis range.

## Getting Started

Since we are not training neural networks in this project, users should be able to reproduce our results with a laptop.

Download this repository by going up to the green "Code" button at the top right and clicking "Download ZIP".

Alternatively, you can also clone the repo directly using the following commands.

  ```sh
  # Replace "your_folderpath_here" with the actual folder where you want the project to go.
  cd /your_folderpath_here
  git clone git@github.com:ericodle/JP_BERT.git
  ```

> __For this example, the working directory is the repository root directory.__ 

### Install dependencies using pip

  ```sh
  # Install dependencies if necessary. 
  # You may want to work in a virtual environemnt. Conda environments are nice for that.
  pip install transformers==3.0.2
  pip install torch torchvision
  pip install git
  ```
  
### Get MeCab and IPADIC working

The pre-trained BERT model used for this project employs the MeCab text segmenter for Japanese. Along with MeCab comes the IPADic tokenization dictionary, which must also be installed. The following code got everything working in our environment, but be prepared to do the incompatible dependency/missing package dance a bit before everything works.

  ```sh
  # First, install MeCab.
  apt install aptitude swig 
  aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y
  pip install mecab-python3==0.996.6rc2
  
  # Next, install the Neologd ipadic dictionary---it contains more modern internet words.
  git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
  echo yes | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a
  ```

If everything went well, we should be able to perform the following test.

  ```python
  import MeCab
  m=MeCab.Tagger("-Ochasen")
  text = "私は機械学習が好きです。"
  text_segmented = m.parse(text)
  print(text_segmented)
  ```
MeCab will then do its job and segment the text we provided. Additionally, MeCab identifies each segment into its katakana pronounciation and grammatical class. Handy!
         
<pre>
私        ワタシ      私        名詞-代名詞-一般  
は        ハ         は        助詞-係助詞                         
機械      キカイ      機械      名詞-一般                       
学習      ガクシュウ   学習      名詞-サ変接続                 
が        ガ         が        助詞-格助詞-一般                    
好き      スキ        好き      名詞-形容動詞語幹                
です      デス        です      助動詞  
。         。         。       記号-句点                           
</pre>

You can also replace the "-Ochasen" Tagger with "-Owakati" and "-Oyomi" for different text breakdown formats.

### generate_ppx.py

> This is the main project script. Open the .py file for helpful tips and enlightening comments. More importantly, our proposed perplexity model is coded as a FOR loop in this script.

```sh
# This will generate a ppx value for each N3 adverb question response. 
# The questions are taken from N3_adverbs.csv under the "text" column.

./generate_ppx.py
```

<p align="right">(<a href="#top">back to top</a>)</p>


## Content

- [ ] generate_ppx.py

This is the main script of the entire JP_BERT project. Here, we have coded our proposed perplexity algorithm as a simple FOR loop with accompanying comments in the .py file. For further reference, please check out our soon-to-be-published paper on the topic.

- [ ] ppx_descriptive_stats.csv

This CSV file contains the same first two columns as "ppx_output.csv" plus additional post-run calculations. Column C is labeled "correct" and contains a binary coding scheme (1=correct, nothing=incorrect) for JP_BERT's accuracy on the N3 test set. The correct answer for each question was placed at the top of every 4-response list. Therefore, if the minimum perplexity value for a given quartet occurs on the first response, a "1" is asigned. Otherwise, JPBERT answered the question incorrectly and a value of zero (space left blank) is assigned. Column D is labeled text_length and contains character counts for each corresponding input string in Column A. Column E is labeled "IQPR", which stands for "inter-question perplexity range." These values represent the difference between the maximum and minimum perplexity values for each quartet. Column F is labeled "2-1DIFF", which stands for "the difference between JPBERT's second and first answers to the question". Columns G-H, I-J, K-L, and M-N contain descriptive statistics for perplexity scores, text lengths, IQPR values, and 2-1DIFF values, respectively.

- [ ] N3_adverbs.csv

This CSV file contains two data columns. The first column is titled "text" and consists of 100 transcribed N3 Japanese adverb questions from a comercially available JLPT test prep book. Each of the 4 possible answers for each question are written out such that JP_BERT can evaluate sentence perplexities in their entirety. Each 4-sentence question set is separated by a blank row, producing a list 500 rows in length. The second column is titled "perplexity" and contains perplexity values corresponding to adjacent text inputs.

- [ ] BERT_primer.py

We have provided a beginner's guide for using BERT in Japanese (or any language). Feel free to open up this .py file in your favorite IDE or text editor and read all the helpful comments. You can copy-paste the code one block at a time in a command line interface, or even run it in a Colab/Jupyter Notebook. No GPU required! We hope this primer serves as an easy-to-understand overview of how BERT does math of words.

<p align="right">(<a href="#top">back to top</a>)</p>


## Concluding Thoughts

One barrier to wide-spread adoption is the technical knowledge required to set up and implement a neural network language model. Not only do we ask language teacher to be functionally proficient in computer programming, but also to possess sufficient knowledge as to implement and interpret (as well as troubleshoot) our perplexity approach. This barrier to entry was recently addressed by the free-to-use and beginner-friendly tool ChatGPT, which has garnered recent attention as a general-purpose AI language model and which is already the subject of research for its academic applications.

Another concern of AI in the classroom is student data privacy, the threats to which remain unclear. To facilitate free and easy access to JPBERT, perplexity, and all future tools we develop, we provide our code, source data, and example workbooks on GitHub in the hopes that language teachers otherwise intimidated by this or other CALL tools feel encouraged to explore AI in the classroom.

<!-- CONTRIBUTING -->
## Contributing

Contributions make the open source community great. Everyone has a unique combination of skills and experience. Your input is **highly valued**.
If you have ideas for improvement, please fork the repo and create a pull request. 
If this is your first pull request, just follow the steps below:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU Lesser General Public License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
