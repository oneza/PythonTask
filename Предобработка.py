#Предобработка музыкальных мультитреков формата .midi
#для объединения звуковых дорожек, удаления лишних и дальнейшего запуска модели

!pip install pypianoroll
from google.colab import drive
drive.mount('/content/drive')
from pypianoroll import Multitrack, Track
import glob

def main():
  c=0
  for filename in (glob.glob('drive/My Drive/Synth pop MIDI/*.mid')):
      mtrack = Multitrack(filename)
      mtrack.to_pretty_midi()
      #mtrack = remove_short_tracks(mtrack)
      orchestra = group_by_program(mtrack)
      l=len(mtrack.tracks)
      trackid=[x for x in range(l)]
      newmtrack, inst = merge_instrument(mtrack,orchestra,trackid)
      filename=filename[30:]
      if len(newmtrack.tracks)==4:
        c+=1
        print(filename, len(newmtrack.tracks), inst, orchestra)
        newmtrack.write('drive/My Drive/Synth pop MIDI/four tracks with drum sum/'+filename)
  print(c)

def remove_short_tracks(mtrack):
  l=len(mtrack.tracks)
  i=j=l-1
  al=[]
  while j>=0:
      al.append((mtrack.tracks[j]).get_active_length())
      j-=1
  al.sort()
  a=[]
  while i>=0:
      actl=(mtrack.tracks[i]).get_active_length()
      apr=mtrack.tracks[i].get_active_pitch_range()
      if actl<al[l-1]*0.1 or apr[1]<50:
          a.append(i)
      i-=1
  mtrack.remove_tracks(a)
  return mtrack
    

def group_by_program(mtrack):
  orchestra=[[]for _ in range(5)]
  trackcount=0
  for track in mtrack.tracks:
    if track.program<90:
      if not track.is_drum:
        i=track.program // 25
        orchestra[i].append(trackcount)
      else:
        orchestra[4].append(trackcount)
    trackcount+=1
  orchestra[2]=orchestra[2]+orchestra[3]
  orchestra.remove(orchestra[3])
  return orchestra

def merge_instrument(mtrack,orchestra,trackid):
  #instname=['piano','chromatic percussion','organ','guitar','bass','strings','ensemble','brass','reed','pipe','synth lead','synth pad','synth effects','ethnic','percussive','sound effects']
  instname=['piano','guitar','synth lead','drum']
  drums=[False,False,False,True]
  programs=[5,28,81,0]
  inst=[]
  for p in range(0,4):
    if orchestra[p]!=[]:
      inst.append(instname[p])
      mtrack.merge_tracks(track_indices=orchestra[p], mode='max', program=programs[p], is_drum=drums[p], name=instname[p], remove_merged=False)
  mtrack.remove_tracks(trackid)
  return mtrack, inst

if __name__ == "__main__":
    main()