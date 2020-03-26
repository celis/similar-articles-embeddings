from gensim.models import Word2Vec, KeyedVectors
from typing import Dict


class GensimWord2Vec:
    """
    Wrapper around Gensim word2vec model
    """

    def __init__(self, model_config: Dict):
        self.model_config = model_config
        self._model = None

    def fit(self, data):
        """
        Fits model to data
        """
        self._model = Word2Vec(sentences=data, **self.model_config).wv

    def save(self, path: str):
        """
        Saves embeddings to path
        """
        if self._model is not None:
            self._model.save_word2vec_format(path, binary=True)
