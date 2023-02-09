
import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
from openpyxl import Workbook


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en-AU'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)



def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3("announce_english.mp3")

    # 1 - Generate namskar kripya dheyan dijiye
    start =0000
    finish = 1900
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is flight_name

    # 3 generate- ki udan sankhya
    start = 2000
    finish = 2900
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 generate -flight_no

    # 5 ab
    start = 4700
    finish = 5099
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6  generate -city

    # 7  generate - jane ke liye taiyar hai sabhi yatri se nivedan he ki viman ke dwar kramank
    start = 5300
    finish = 9300
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")


    # 8 gate no

    # 9 prastan kare
    start = 10100
    finish = 10990
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")

    # 10 generate flight name

    # 11 generate apki sukhad yatra ki kamana karati hai danyavad
    start = 12000
    finish = 14800
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)

    for index, item in df.iterrows():

        # 2 - Generate flight_name
        textToSpeech(item['flight_name'], '2_hindi.mp3')

        # 4 generate -flight_no
        textToSpeech(item['flight_no'],'4_hindi.mp3')

        # 6 generate city
        textToSpeech(item['City_name'],'6_hindi.mp3')

        #8 generate Gate_no
        textToSpeech(item['Gate_no'],'8_hindi.mp3')

        # 10 generate flight name
        textToSpeech(item['flight_name'],'10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['flight_no']}_{index + 1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_english.xlsx")