import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize_text(text):
    word_tokens = word_tokenize(text)
    sent_tokens = sent_tokenize(text)
    freq_table = dict()
    for word in word_tokens:
        word = word.lower()
        if word not in stopwords.words("english"):
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
    sent_scores = dict()
    for sentence in sent_tokens:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sent_scores:
                    sent_scores[sentence] += freq
                else:
                    sent_scores[sentence] = freq

    average = sum(sent_scores.values()) // len(sent_scores)
    summary = ''
    for sentence in sent_tokens:
        if sentence in sent_scores and sent_scores[sentence] > (1.2 * average):
            summary += " " + sentence
    return summary