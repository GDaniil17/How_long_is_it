from tkinter import Tk
from tkinter import filedialog
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
import os

def insertText():
    root = Tk()
    root.withdraw()
    current_directory = filedialog.askdirectory()
    return current_directory

st = insertText()
alles = 0
a = []
day, h, m, s = 0, 0, 0, 0
mp3 = False
mp4 = False

if "y" in input("Do you want scan all mp3 files?  "):
    mp3 = True
else:
    mp4 = True

for top, dirs, files in os.walk(st):
    for nm in files:
        if mp3:
            if nm.endswith("mp3"):
              print(os.path.join(top, nm))
              audio = MP3(os.path.join(top, nm))
              length = audio.info.length
              h += length//60//60
              m += length//60%60
              s += length%60*10//10
              if s >= 60:
                m += s//60
                s %= 60
              if m >= 60:
                h += m//60
                m %= 60
              if h >= 24:
                day += h//24
                h %= 24
              a.extend([(length//60//60*60*60)+(length//60%60*60)+(length%60*10//10)])
              alles += (length//60//60*60*60)+(length//60%60*60)+(length%60*10//10)
              print("{} hour(-s) {} minute(-s) and {} second(-s)".format(length//60//60, length//60%60, length%60*10//10))
        elif mp4:
            if nm.endswith("mp4"):
              print(os.path.join(top, nm))
              audio = MP4(os.path.join(top, nm))
              length = audio.info.length
              h += length//60//60
              m += length//60%60
              s += length%60*10//10
              if s >= 60:
                m += s//60
                s %= 60
              if m >= 60:
                h += m//60
                m %= 60
              if h >= 24:
                day += h//24
                h %= 24
              a.extend([(length//60//60*60*60)+(length//60%60*60)+(length%60*10//10)])
              alles += (length//60//60*60*60)+(length//60%60*60)+(length%60*10//10)
              print("{} hour(-s) {} minute(-s) and {} second(-s)".format(length//60//60, length//60%60, length%60*10//10))
              
print("-----------------------------------------------------------------------------")
print("{} day(-s) {} hour(-s) {} minute(-s) and {} second(-s)".format(day, h, m, s))
print("-----------------------------------------------------------------------------")
if alles != 0:
    tr = input("Do you want to know how many percents left?")
    if "y" in tr.lower():
        n = int(input("Which epsisode in the folder do you watch?"))
        time = list(map(int, input().replace(":", " ").replace(" : ", " ").replace("  ", " ").split()))
        if len(time) == 3:
          print("{} %".format((sum(a[:n-1])+((time[0]*60*60)+(time[1]*60)+time[2]))/alles*100))
        elif len(time) == 2:
          print("{} %".format((sum(a[:n-1])+((time[0]*60*60)+(time[1]*60)))/alles*100))
        elif len(time) == 1:
          print("{} %".format((sum(a[:n-1])+((time[0]*60*60)))/alles*100))
