from src.queries import Query


def translate_sentiment(text: str) -> bool:
    """
    Convert a text message to a boolean.
    True is a good sentiment
    False is a bad sentiment.

    This function sends the string param to to LISA API
    to extract sentiment with NLP.

    Note: Since LISA is "a little debiased" the
    word "bem" (portuguese meaning to "well", "good" or "fine")
    is being classified as neutral (scoring 0), and here
    in this we are considering only a binary sentiment where
    0 stands for bad since its boolean value is False
    """
    if text == 'bem':
        return True
    return Query.query_sentiment_value(text)
