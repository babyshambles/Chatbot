# EE628 final porject
# Chatbot based on Reccurent Neural Networks 
## Team member: Yufei Wang,  Jiangchuan Li


## Introduction
  We chose to design a Chatbot as our project of EE628 because of our interest in natural language processing. A Chatbot, or a Neural Conversation Model is an important part in natural language processing. It can reply to some questions automatically after trained on large amount of dialog data. 
  Although Deep Neural Networks (DNNs) can achieve great results in almost every difficult learning task whenever large labeled training sets are available, they cannot be used to map sequences to sequences which we will need in our model. Reccurent Neural Networks or simple RNNs, a Seq2Seq model is introduced to our project. Our model uses a multilayer Gated Recurrent Unit(GRU) to map the input sequence to a vector, and then another deep GRU to decode the target sequence from the vector. This RNN Encoder–Decoder system can be trained end-to-end and thus requires much fewer hand-crafted rules. After hours of training, we find that we can generate simple conversations given a large conversational training dataset despite the dataset is noisy or specific.
### Embedding Layer
Here for natural language processing, the first important is the emmbedding layer. We choose the Google News Word2word as the embedding layer. Also there are some other pre-trained word vector such as FastText, it time permits, will try these word vector to see which one has the most excellent performance.

### Corpus
The training datasets we choose for this project are the Cornell Movie Dialogs corpus, Ubuntu Dialogue Corpus and Supreme Court Conversation Data.

### Package
This project requires the following pakages:
python 3, tensorflow, numpy, nltk(Natural Language toolkit for tokenized sentences).

### Implementation
At the final step of this project, we take into consideration that make this chat robot come into being via web. This is mainly about to make a friendly interface, copy the model to the server, at the localhost make this application.

### Result
