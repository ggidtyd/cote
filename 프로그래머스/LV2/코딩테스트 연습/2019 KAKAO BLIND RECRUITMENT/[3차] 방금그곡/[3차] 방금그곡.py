class MusicInfo:
    start_time = 0
    play_time = 0
    melody_len = -1
    melody = ""
    title = ""


    def __init__(self, title, start_time=0, play_time=0, melody_len=-1, melody=""):
        self.title = title
        self.start_time = start_time
        self.play_time = play_time
        self.melody_len = melody_len
        self.melody = melody
        

def solution(m, musicinfos):
    answer = MusicInfo("(None)")
    music_infos = []

    m = m.replace('C#', 'H').replace('D#', 'I').replace('F#', 'J').replace('G#', 'K').replace('A#', 'L')
    for info in musicinfos:
        start_time, end_time, title, melody = info.split(',')
        start_h, start_m = start_time.split(':')
        end_h, end_m = end_time.split(':')

        start_time = (int(start_h)*60 + int(start_m))
        play_time = (int(end_h)*60 + int(end_m)) - start_time
        
        melody = melody.replace('C#', 'H').replace('D#', 'I').replace('F#', 'J').replace('G#', 'K').replace('A#', 'L')
        melody = melody * (play_time // len(melody)) + melody[:play_time % len(melody)]

        music_infos.append(MusicInfo(title, start_time, play_time, len(melody), melody))


    for info in music_infos:
        if m in info.melody:
            if info.melody_len > answer.melody_len:
                answer = info
            elif info.melody_len == answer.melody_len and info.start_time < answer.start_time:
                answer = info
                
    return answer.title