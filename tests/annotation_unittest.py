#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
    Date: 25/03/2018
"""

import unittest
from deepnlpf.pipeline import Annotation

class TestAnnotation(unittest.TestCase):

    # ok, está funcionando.
    # ['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse', 'depparse', 'truecase', 'dcoref']
    custom_pipeline_stanfordcorenlp = {
        'tools': [
            {
                'stanfordcorenlp': {
                    'pipeline': ['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse', 'depparse', 'truecase', 'dcoref']
                }
            }
        ]
    }

    # ok, está funcionando.
    custom_pipeline_semafor = {
        'tools': [
            {
                'semafor': {
                    'pipeline': ['parsing']
                }
            }
        ]
    }

    # ok, está funcionando. falta colocar offline
    # ['SHALLOW_PARSE', 'NER_ONTONOTES', 'SRL_NOM', 'SRL_VERB', 'SRL_PREP']
    custom_pipeline_cogcomp = {
        'tools': [
            {
                'cogcomp': {
                    'pipeline': ['SRL_NOM', 'SRL_VERB', 'SRL_PREP']
                }
            }
        ]
    }

    # no found
    custom_pipeline_pywsd = {
        'tools': [
            {
                'pywsd': {
                    'pipeline': ['disambiguate']
                }
            }
        ]
    }

    custom_pipeline_supwsd = {
        'tools': [
            {
                'supwsd': {
                    'pipeline': ['wsd']
                }
            },
        ]
    }

    custom_pipeline_spacy = {
        'tools': [
            {
                'spacy': {
                    'pipeline': ['pos', 'tag', 'shape', 'is_alpha', 'is_title', 'like_num', 'label']
                }
            },
        ]
    }

    # TODO add essa análise : wordnet_sumo
    custom_pipeline_freeling = {
        'tools': [
            {
                'freeling': {
                    'pipeline': ['wsd', 'svo_triples_srl']
                }
            }
        ]
    }

    custom_pipeline_quanteda = {
        'tools': [
            {
                'quanteda': {
                    'pipeline': ['frequency']
                }
            }
        ]
    }

    custom_pipeline_all = {
        'tools': [
            {
                'stanfordcorenlp': {
                    'pipeline': ['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse', 'depparse', 'truecase', 'dcoref']
                }
            },
            {
                'semafor': {
                    'pipeline': ['parsing']
                }
            },
            {
                'cogcomp': {
                    'pipeline': ['SHALLOW_PARSE', 'NER_ONTONOTES', 'SRL_NOM', 'SRL_VERB', 'SRL_PREP']
                }
            },
            {
                'spacy': {
                    'pipeline': ['pos', 'tag', 'shape', 'is_alpha', 'is_title', 'like_num', 'label']
                }
            },
            {
                'pywsd': {
                    'pipeline': ['disambiguate']
                }
            },
        ]
    }



    # --------------------------------------------------------------------------------------------------

    experience_1_analise_lexica_cogcomp = {
        'tools': [
            {
                'cogcomp': {
                    'pipeline': ['NER_ONTONOTES']
                }
            }
        ]
    }



    experience_1_analise_lexica_all = {
        'tools': [
            {
                'stanfordcorenlp': {
                    'pipeline': ['tokenize', 'pos', 'lemma', 'ner']
                }
            },
            {
                'spacy': {
                    'pipeline': ['pos', 'tag', 'shape', 'is_alpha', 'is_title', 'like_num', 'label']
                }
            },
            {
                'cogcomp': {
                    'pipeline': ['NER_ONTONOTES']
                }
            }
        ]
    }
    # -------------------------------------------------------------------------------------------------

    id_dataset = '5dc1708df24f6cc5e8de731a'

    """
        Pipeline
    """

    annotation = Annotation(id_dataset, custom_pipeline_supwsd, True)
    result = annotation.annotate()

if __name__ == '__main__':
    unittest.main()