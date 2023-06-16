from pydub import AudioSegment

song = AudioSegment.from_mp3("audio4p.mp3")

# pydub does things in milliseconds
ten_seconds = 10 * 1000

first_10_seconds = song[:ten_seconds]

last_5_seconds = song[-5000:]

# pydub does things in milliseconds
ten_seconds = 10 * 1000

first_10_seconds = song[:ten_seconds]

last_5_seconds = song[-5000:]

# boost volume by 6dB
beginning = first_10_seconds + 6

# reduce volume by 3dB
end = last_5_seconds - 3

without_the_middle = beginning + end

without_the_middle.duration_seconds == 15.0

# song is not modified
backwards = song.reverse()

# 1.5 second crossfade
with_style = beginning.append(end, crossfade=1500)

# repeat the clip twice
do_it_over = with_style * 2

awesome = do_it_over.fade_in(2000).fade_out(3000)

awesome.export("mashup.mp3", format="mp3")