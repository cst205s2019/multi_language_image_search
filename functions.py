def custom_convert(text, lang):
	# Imports the Google Cloud client library
	from google.cloud import translate

	# Instantiates a client
	translate_client = translate.Client()
	translation = translate_client.translate(
	        text,
	        target_language=lang)
	return translation['translatedText']
