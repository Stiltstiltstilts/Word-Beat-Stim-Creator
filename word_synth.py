from gtts import gTTS
import librosa
import soundfile as sf
from pydub import AudioSegment
from constants import sub_cong

def synthWord(word, filename, language="en"):
    "outputs mp3 of word"
    tts = gTTS(text=word, lang=language,)
    tts.save("{}.mp3".format(filename))
    #print("file successfully created!")

synthWord("boy","boy")
####### create mp3 for each word in sentence ####
for trial_dict in sub_cong:
    sentence = trial_dict['sent_stim']
    for word in sentence:
        synthWord()

# Load speech file
word = AudioSegment.from_file('/Users/Stilts/Documents/GitHub/Cong_music_lang2/boy.mp3', format="mp3")

# load tone file
tone = AudioSegment.from_file("/path/to/sound.wav", format="wav")

# len of audio in ms
original_word_len = len(word)

# compute stretch factor
stretch_factor = (desired_dur + rise_len) / actual_dur

word = librosa.effects.time_stretch(word, stretch_factor)

onset = librosa.onset.onset_detect(word)
onset = onset(0) # just return the first onset

word = word(onset:)


tone.overlay(word, position=1000) # need to specify position
# go through each sentence, 
# 1. generate individual words
# generate subdir for each sentence
# 2. onset detect the start of the speech sound, and set the start of the soundfile to be 17.5ms before that (i.e. to align with tone)
# 3. time-stretch to tone length and save as .wav
# 4. Overlay speech sounds to correct bits in the tone sequence?
