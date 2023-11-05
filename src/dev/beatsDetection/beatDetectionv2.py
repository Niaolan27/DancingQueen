import librosa
audio_file = "C:\\Users\\wands\\Documents\\CS_15112\\505.mp3"
y, sr = librosa.load(audio_file)

duration = librosa.get_duration(y=y, sr=sr)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr) 
print(f"Duration: {duration} seconds")
print(f"Sample Rate: {sr} Hz")
print(f'Tempo:{tempo, _, len(_)}')


