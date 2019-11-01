# Chat Robot
### Introduction
This project is mainly about trying to produce a chat robot. Based on the result of a neural conversational model(like the google chat bot). This project's model uses a RNN based on the seq2seq model for sentence prediction. This model is operated on python via Tensorflow.

### Embedding Layer
Here for natural language processing, the first important is the emmbedding layer. We choose the Google News Word2word as the embedding layer. Also there are some other pre-trained word vector such as FastText, it time permits, will try these word vector to see which one has the most excellent performance.

### Corpus
The training datasets we choose for this project are the Cornell Movie Dialogs corpus, Ubuntu Dialogue Corpus and Supreme Court Conversation Data.

### Package
This project requires the following pakages:
python 3, tensorflow, numpy, nltk(Natural Language toolkit for tokenized sentences).

### Implementation
At the final step of this project, we take into consideration that make this chat robot come into being via web. This is mainly about to make a friendly interface, copy the model to the server, at the localhost make this application.
