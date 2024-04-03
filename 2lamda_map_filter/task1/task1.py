def transform_words(words:list) -> list:
    def transformation(word:str) -> str:
        return word.upper() + str(len(word))

    transformation = lambda w: w.upper() + str(len(w))

    words = list(map(transformation, words))
    return words
   