import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from heapq import nlargest

stop_words = stopwords.words('turkish')

def generate_summary(text, n):
    sentences = sent_tokenize(text)
    vectorizer = TfidfVectorizer(stop_words=stop_words)

    tfidf_martrix = vectorizer.fit_transform(sentences)
    sentences_score = cosine_similarity(tfidf_martrix[-1], tfidf_martrix[:-1])[0]
    summary_sentences = nlargest(n, range(len(sentences_score)), key=sentences_score.__getitem__)
    summary_tfidf = ' '.join([sentences[i] for i in sorted(summary_sentences)])

    return summary_tfidf

text = """
İlk katman olan mukoza en içteki
katmandır ve üç alt katmandan oluşur:
mukozal membran,
lamina propria ve
muscularis mukozası.

Mukoza bir zar görevi görür.

Gastrointestinal sistemin lümenini
kaplayan epitel hücrelerinden oluşur ve
yediğimiz besinler ile temas halinde
olan iç yüzey tabakasıdır.
"""

print(generate_summary(text, 3))
