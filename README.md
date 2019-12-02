# EE628 final porject
## Chatbot based on Reccurent Neural Networks 
### Team member: Yufei Wang,  Jiangchuan Li
#### Table of Contents
* [Introduction](#Introduction)
* [TODO](#TODO)
    * [Corpus](#Corpus)
    * [Data pre-processing](#Data-pre-processing)
    * [Embedding layer](#Embedding-layer)
    * [Models](#Models)
         * [Reccurent Neural Networks](#Reccurent-Neural-Networks)
         * [Gated Recurrent Unit](#Gated-Recurrent-Unit)
    * [Training](#Training)
* [Results](#Results)
* [Installation](#Installation)
    * [How to run](#How-to-run)
    * [Dependency lists](#Dependency-lists)
* [Future works](#Future-works)
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
### Models 
#### Reccurent Neural Networks
* A simple RNN model can map the input sequence to a fixed size vector then map the vector to the target sequence in theory, but the results are not ideal when long term dependencies were introduced. The Long Short-Term Memory (LSTM) is explicitly designed to avoid the long-term dependency problem.

![Image text](https://github.com/babyshambles/Chatbot/blob/master/LSTM.png?raw=true)

* This is a standard deep LSTM model with four layers. In the image, each yellow square is a nerual net layer, in which sigmoid layer decides what information we are going to keep by iterating the following equation and tanh layer is a pointwise multiplication operation.
* In Neural Conversational Model problem, usually two LSTMs will be used: one for the input sequence as encoder and one for the outputsequence as decode. This is a simple demonstration of what's going on in the Encoder-Decoder models.

![Image text](https://github.com/babyshambles/Chatbot/blob/master/Encoder.png?raw=true)

#### Gated Recurrent Unit
Gated Recurrent Unit (GRU) is very similar to LSTM, with forget gate but has fewer parameters than LSTM. This is the sturcture of Gated Recurrent Unit.

![Image text](https://github.com/babyshambles/Chatbot/blob/master/GRU.png?raw=true)

We choose to use GRU instead of LSTM because we find that GRU has shorter training time than LSTM. GRU’s has fewer tensor operations, and the performance is similar to LSTM, sometimes even better in some small data sample cases.

### Training 
* As we get starting with the training process, we set the batch size 32, and the training epoch 50. We send the training set into the model. Since the data set corpus is such a large set and the structure of the DL model is a little complicated, it takes nearly one hour for one epoch to train. The total training time is about 50 hours.
* So we take AWS into consideration to make this training process accelerated. Here we import the tqdm, which could let us create a simple progress bars with just a few lines of codes. This make a grate help that allow us to know how much work this model has done and how many more time it will need.

## Results
### Self test
We include a self test step after everytime an epoch loop is finished. We test the model with two sentences: 1. Happy birthday have a nice day 2. donld trump won lost nights presidential debate according to snap online polls. We can see how the model's responce is improving.
![Image text](https://github.com/babyshambles/Chatbot/blob/master/Encoder.png?raw=true)
## Installation 
### How to run
### Dependency lists
This project requires the following pakages:
* python 3
* Tensorflow and Tensorlayer
* nltk(Natural Language toolkit for tokenized sentences)
* tqdm(for progression monitoring)
* numpy

## Future works 
* More dialog corpus. Because of the time limitation, we only use Twitter dialog to train this model. Our model didn't perform good enough when it answering questions because this corpus contains mostly comments, not conversations. And the model only generate meaningful responses in certain context. In the future, we can use dialogs like Cornell Movie Dialogs corpus and Supreme Court Conversation Data to improve our performance.
* Actions to save time. Due to the tight schedule and computing power limitation, we did a lot of works to reduce training time. We limited the length of dialogs, chose simpler model with less training time and reduced epoch times. We believe we can achieve better results with a longer training process.
* An user friendly interface. Now we chat with our Chatbot in command windows, this is more like a test of our model rather than chatting. If we want users to use our product, we need to design an user friendly interface. It's possible to design a beautiful website connected to our server by using Djungo and Redis.



