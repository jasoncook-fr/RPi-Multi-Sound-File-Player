import glob
from pydub import AudioSegment

list_of_files = glob.glob('*.wav')           # create the list of file
fileoutCount = 1

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

for file_name in list_of_files:
	sound = AudioSegment.from_file(file_name, "wav")
	normalized_sound = match_target_amplitude(sound, -13.0)
	normalized_sound.export('/home/pi/jelly_project/sounds/modified/' + str(fileoutCount) + '.wav', format="wav")
	fileoutCount += 1
