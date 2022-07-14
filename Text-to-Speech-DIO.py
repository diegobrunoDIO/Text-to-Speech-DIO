#instalar a biblioteca gTTS !pip install gTTS

from gtts import gTTS

text_to_say = "How are you doing?."

language = "en"

gtts_object = gTTS(text = text_to_say, 
                  lang = language,
                  slow = False)

gtts_object.save("/content/gtts.wav")

from IPython.display import Audio

Audio("/content/gtts.wav")

french_text = "Je vais au supermarché"

french_language = "fr"

french_gtts_object = gTTS(text = french_text,
                          lang = french_language,
                          slow = True)

french_gtts_object.save("/content/french.wav")

Audio("/content/french.wav")
