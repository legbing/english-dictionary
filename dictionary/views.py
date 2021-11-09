from django.shortcuts import render
from PyDictionary import PyDictionary
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet


# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = set()
    antonyms = set()
    for synset in wordnet.synsets(search):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
            if(lemma.antonyms()):
                antonyms.add(lemma.antonyms()[0].name())

    
    context = {
        'meaning': meaning,
        'synonyms': ', '.join([x for x in synonyms]),
        'antonyms': ', '.join([x for x in antonyms])
    }
    return render(request, 'word.html', context)