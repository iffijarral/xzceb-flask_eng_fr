'''Import liberaries'''
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version = VERSION,
    authenticator = authenticator
)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    '''Translates given English text to French'''
    if english_text != '':
        try:
            # Call translate method
            french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()["translations"][0]["translation"]
            # Return the translated text
            return french_text
        except ApiException as ex:
            print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
    else:
        return "Please give any text to translate"
def french_to_english(french_text):
    '''Translates given French text to English'''
    if french_text != '':
        try:
            # Call translate method
            english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()["translations"][0]["translation"]
            # Return the translated text
            return english_text
        except ApiException as ex:
            print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
    else:
        return "Please give any text to translate"
