import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
from openpyxl import Workbook

# It takes two argument text and filename 
# text - Normal string which we want to convert into the speech
# filename- where .mp3 file will be store i.e audio file

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    


# This function returns pydubs audio segment
# 
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)  # combines all the mp3 files 
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3("railway.mp3")  # reading mp3 file

    # 1 - Generate kripya dheyan dijiye
    start = 88000     # timing in the milisecond
    finish = 90200    #  end time in the mili seconds
    audioProcessed = audio[start:finish]    # slicing of the audion in the file railway.mp3
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)

    print(df)
    for index, item in df.iterrows():   # iterrow it is the pandas function in which index defines index of the row i.e 0 1 2  etc.
                                        #  item defines the col no like 'from','via' likewise in the xls file
        # 2 - Generate from-city
        textToSpeech(item['from'], '2_hindi.mp3')

        # 4 - Generate via-city
        textToSpeech(item['via'], '4_hindi.mp3')

        # 6 - Generate to-city
        textToSpeech(item['to'], '6_hindi.mp3')

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'], '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    

