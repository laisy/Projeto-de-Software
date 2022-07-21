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

        self.verbos = sorted([token.lemma_ for token in doc if token.pos_ == "VERB"])
        self.verbos_aux = sorted([token.lemma_ for token in doc if token.pos_ == "AUX"])
        self.pronomes = sorted([token.lemma_ for token in doc if token.pos_ == "PRON"])
        self.subst_comuns = sorted([token.lemma_ for token in doc if token.pos_ == "NOUN"])
        self.subst_proprios = sorted([token.lemma_ for token in doc if token.pos_ == "PROPN"])
        self.conjuncoes = sorted([token.lemma_ for token in doc if token.pos_ == "CCONJ"])

    def maxLenArray(self):
        max = 0

        if len(self.verbos) > max:
            max = len(self.verbos)

        if len(self.verbos_aux) > max:
            max = len(self.verbos_aux)

        if len(self.pronomes) > max:
            max = len(self.pronomes)

        if len(self.subst_comuns) > max:
            max = len(self.subst_comuns)

        if len(self.subst_proprios) > max:
            max = len(self.subst_proprios)

        if len(self.conjuncoes) > max:
            max = len(self.conjuncoes)

        return max

