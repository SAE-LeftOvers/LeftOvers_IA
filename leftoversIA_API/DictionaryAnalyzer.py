from typing import Dict

class DictionaryAnalyzer:
    def __init__(self):
        self.nothing = None

    def analyze(self, wordspoints_attribution: Dict[str, int], dictionary_to_evaluate: Dict[str, int]) -> int:
        output_value = 0
        for word in wordspoints_attribution:
            word_number = dictionary_to_evaluate.get(word)
            if word_number :
                output_value += word_number * wordspoints_attribution[word]
        return output_value