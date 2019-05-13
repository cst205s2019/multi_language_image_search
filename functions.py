def custom_convert(text, lang):
    """
    A function which uses the Google Cloud Vision API, creating a class 
    and then calling the translate method. 

    Keyword arguments:  
    text -- the user input string to be translated
    lang -- the 2 letter abbreviation of a language

    """

	from google.cloud import translate

	# Instantiates a client
	translate_client = translate.Client()
	translation = translate_client.translate(
	        text,
	        target_language=lang)
	return translation['translatedText']
