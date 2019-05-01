def custom_convert(text, target):
	# Imports the Google Cloud client library
	from google.cloud import translate

	# Instantiates a client
	translate_client = translate.Client()

	translation = translate_client.translate(
	        text,
	        target_language=target)
	return translation