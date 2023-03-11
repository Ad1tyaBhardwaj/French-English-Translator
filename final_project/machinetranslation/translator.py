'''imported modules
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
#Test comment
apikey = os.environ['apikey']
url = os.environ['url']
print(apikey)

authenticator = IAMAuthenticator('xB4The5OOj0cC7EkHiLZmxlsrEBndIxWwflAVEe7QWLk')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com')

'''
Function to translate english text to french
'''
def english_to_french(english_text):
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = (french_text["translations"][0]['translation'])
    print(french_text)
    return french_text

'''
Function to translate french text to english
'''

def french_to_english(french_text):
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = (english_text["translations"][0]['translation'])
    print(english_text)
    return english_text
