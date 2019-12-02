import tensorlayer as tl
from tensorlayer.models.seq2seq import Seq2seq
import tensorflow as tf
import tensorlayer_dataprocess
def initial_setup(data_coupus):
    metadata, idx_q, idx_a = tensorlayer_dataprocess.load_data(PATH='{}'.format(data_coupus))
    (trainX, trainY), (testX, testY), (validX, validY) = tensorlayer_dataprocess.split_dataset(idx_q, idx_a)
    trainX = tl.prepro.remove_pad_sequences(trainX.tolist())
    trainY = tl.prepro.remove_pad_sequences(trainY.tolist())
    testX = tl.prepro.remove_pad_sequences(testX.tolist())
    testY = tl.prepro.remove_pad_sequences(testY.tolist())
    validX = tl.prepro.remove_pad_sequences(validX.tolist())
    validY = tl.prepro.remove_pad_sequences(validY.tolist())
    return metadata, trainX, trainY, testX, testY, validX, validY

if __name__ == '__main__':
    data_corpus = ''
    metadata, trainX, trainY, testX, testY, validX, validY = initial_setup(data_corpus)
    src_len = len(trainX)
    tgt_len = len(trainY)

    assert src_len == tgt_len
    batch_size = 32
    n_step = src_len // batch_size
    src_vocab_size = len(metadata['idx2w'])
    emb_dim = 1024

    word2idx = metadata['w2idx']
    idx2word = metadata['idx2w']

    unk_id = word2idx['unk']
    pad_id = word2idx['_']

    start_id = src_vocab_size
    end_id = src_vocab_size + 1

    word2idx.update({'start_id': start_id})
    word2idx.update({'end_id': end_id})
    idx2word = idx2word + ['start_id', 'end_id']
    src_vocab_size = tgt_vocab_size = src_vocab_size + 2

    num_epochs = 50
    vocabulary_size = src_vocab_size

    decoder_seq_length = 20
    modell = Seq2seq(decoder_seq_length = decoder_seq_length,
                     cell_enc=tf.keras.layers.GRUCell,
                     cell_dec=tf.keras.layers.GRUCell,
                     n_layer=3,
                     n_units=256,
                     embedding_layer=tl.layers.Embedding(vocabulary_size=vocabulary_size, embedding_size=emb_dim))

    optimizer = tf.optimizers.Adam(learning_rate = 0.001)

    def inference(seed, top_n):
        modell.eval()
        seed_id = [word2idx.get(w, unk_id) for w in seed.split(' ')]
        sentence_id = modell(inputs=[[seed_id]], seq_length=20, start_token=start_id, top_n=top_n)
        sentence = []
        for w_id in sentence_id[0]:
            w = idx2word[w_id]
            if w == 'end_id':
                break
            sentence = sentence + [w]
        return sentence


    tl.files.load_and_assign_npz(name='model_thefinal.npz', network=modell)


while(True):
    seeds = [input('You: ')]

    for seed in seeds:
        print("Query >", seed)
        top_n = 2
        for i in range(top_n):
            sentence = inference(seed, top_n)
            print(" >", ' '.join(sentence))

