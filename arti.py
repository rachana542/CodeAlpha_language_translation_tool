from googletrans import Translator
sen = input("Enter the text which is to be translated: ")
desti = input("Type destination language for \nEnglish as en, Spanish as es, French as fr, German as de, Hindi as hi,Chinese Simplified as zh-cn, Japanese as ja, Korean as ko, Arabic as ar, Russian as ru, Portuguese as pt, Italian as it, Dutch as nl, Turkish as tr, Bengali as bn, Urdu as ur, Vietnamese as vi, Tamil as ta, Telugu as te, Gujarati as gu\n:")
translator_api = Translator()
result = translator_api.translate(sen, dest=desti)
print("Translated sentence:", result.text)
