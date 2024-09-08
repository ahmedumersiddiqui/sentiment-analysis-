import spacy
import pickle

unlp = spacy.blank('ur')

def loadFromPickle(file):

    with open(file, 'rb') as handle:
        dictionary = pickle.load(handle)

    return dictionary

def roman_tokenizer(sentence):

    # Lowering
    sentence = sentence.lower()

    # Default Parameters
    tokens = []
    punctuation = '''!()%\n٪-;۔،:\n\/'"\,“./؟_ء'''

    dictionary =   loadFromPickle('model2.pkl')
    
    sentence = unlp(sentence)

    # Iterating Word By Word
    for word in sentence:

        word = str(word)
        # Iterating Index By Index
        for index in word:
            
              if index in punctuation:
                    word = word.replace(index,'')

        # Removing Any Remaining Special Characters
        if word != "\n" and word != "\r" and word != " " and word != '' and word != " \r" and word !='‘' and word !='’':
              tokens.append(word)

    bi_tokens = [] 
    for i in range(len(tokens)):
        
        if i + 1 < len(tokens):

            a = tokens[i]
            b = tokens[i + 1]

            if a + ' ' + b in dictionary:
                index = tokens.index(a)
                tokens.remove(a)
                tokens.remove(b)
                tokens.insert(index, a + ' ' + b)

    return tokens
