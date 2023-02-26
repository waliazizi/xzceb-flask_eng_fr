#This module uses the IBM Watson Language Translator API to translate text from English to French and vice versa.
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

#This loads the .env file that contains API_KEY and url to the ibm watson translator.
load_dotenv()

#The api key and url is loaded from os current working directory.
API_KEY = os.environ['API_KEY']
URL = os.environ['URL']     

#Strings to choose language From and Into.
EN_FR = 'en-fr'
FR_EN = 'fr-en'

#The authenticator authenticate using API_KEY that is pulled via load_dotenv().
AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version='2018-05-01',authenticator=AUTHENTICATOR)
LANGUAGE_TRANSLATOR.set_service_url(URL)

#The funtion translates English and return French.
def englishToFrench(english_text):
    french_text = LANGUAGE_TRANSLATOR.translate(
        text = english_text,model_id = EN_FR).get_result()
    return french_text['translations'][0]['translation']

#The funtion translates French and return English.
def frenchToEnglish(english_text):
    english_text = LANGUAGE_TRANSLATOR.translate(
        text=english_text,model_id = FR_EN).get_result()
    return english_text['translations'][0]['translation']

# #Takes the strings of English and stores translated string in results veriable.
# result = englishToFrench('Hello')
# print(result)

# #Takes the strings of Franch and stores translated string in results veriable.
# result = frenchToEnglish('Bonjour')
# print(result)
