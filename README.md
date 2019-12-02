# EE628 final porject
# Chatbot based on Reccurent Neural Networks 
## Team member: Yufei Wang,  Jiangchuan Li


## Introduction
 * We chose to design a Chatbot as our project of EE628 because of our interest in natural language processing. A Chatbot, or a Neural Conversation Model is an important part in natural language processing. It can generate answers for some sentences automatically after trained on large amount of dialog data. 
 * Although Deep Neural Networks (DNNs) can achieve great results in almost every difficult learning task whenever large labeled training sets are available, they cannot be used to map sequences to sequences which we will need in our model. Reccurent Neural Networks or simple RNNs, a Seq2Seq model is introduced to our project. 
 * Our model uses a multilayer Gated Recurrent Unit(GRU) to map the input sequence to a vector, and then another deep GRU to decode the target sequence from the vector. This RNN Encoder–Decoder system can be trained end-to-end and thus requires much fewer hand-crafted rules. After hours of training, we find that we can generate simple conversations given a large conversational training dataset despite the dataset is noisy or specific.
 * During our development, we mainly use Python3.7 and Tensorflow. Tensorflow already has a lot of Reccurent Neural Networks embedded and built-in, is very easy to use them. And we run our training models on Amazon Web Services to reduce the training time.
## TODO
### Corpus
First we need to choose our training datasets. We need a large and noisy dialogs corpus so we can test the ability of Seq2Seq models. Thanks to github, we found a Corpus which contained Twitter comments and conversations.
### Data pre-processing 
We need to do some data cleaning and transformations before using it to train the model. Here are some works we do:
* We delete all the tags and symbols, only keep the words information. At the same time we delete the sentences that are too long or too short to keep the datasets in order.
* we get the real lists of words and we call it the whole vocabulary, this vocabulary includes thefrequency of every word. We also create the index of word, words to index dictionary.
* Tokenization. As we know Deep Learning models can not read text directly, so our job is to convert this word-basedtext to integer index. First we split the data into question set and answer set, then add zero padding tothese both sets. Here we should note that if the word is not in the vocabulary, we should replace theword with ’unk’ and get the final results indices of words. 
### Embedding layer
Words embedding is an important part in Natural Language Processing. The main idea behinds this is, we can keep the relation between related words and sentances by turned the words into vectors. In the Embedding space, two embedding vectors(which represent two words) should be close to one another if two words are related. 
![Image text](https://github.com/babyshambles/Chatbot/blob/master/embedding.png?raw=true)

Usually a embedding layer is used before the training model. We choose Google News Word2Word as our embedding layer.

### Corpus
The training datasets we choose for this project are the Cornell Movie Dialogs corpus, Ubuntu Dialogue Corpus and Supreme Court Conversation Data.

### Package
This project requires the following pakages:
python 3, tensorflow, numpy, nltk(Natural Language toolkit for tokenized sentences).

### Implementation
At the final step of this project, we take into consideration that make this chat robot come into being via web. This is mainly about to make a friendly interface, copy the model to the server, at the localhost make this application.

### Result
