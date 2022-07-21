import spacy

class SyntaxAnalisys:
        def __init__(self, text):
                self.text = text
                self.verbos = []
                self.verbos_aux = []
                self.pronomes = []
                self.subst_comuns = []
                self.subst_proprios = []
                self.conjuncoes = []
        
        def analyze(self):
                nlp = spacy.load("pt_core_news_sm")
                doc = nlp(self.text)
                
                self.verbos = [token.lemma_ for token in doc if token.pos_ == "VERB"]
                self.verbos_aux = [token.lemma_ for token in doc if token.pos_ == "AUX"]
                self.pronomes = [token.lemma_ for token in doc if token.pos_ == "PRON"]
                self.subst_comuns = [token.lemma_ for token in doc if token.pos_ == "NOUN"]
                self.subst_proprios = [token.lemma_ for token in doc if token.pos_ == "PROPN"]
                self.conjuncoes = [token.lemma_ for token in doc if token.pos_ == "CCONJ"]


