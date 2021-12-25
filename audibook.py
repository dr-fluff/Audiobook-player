"""
hej

"""
import pyaudio
import sys
import numpy as np
import wave
import struct


class Book:
    def __init__(self, title, author, series, length, isbn, narator, genres, release_date, publisher, summary, rating):
        self.Title = title
        self.Author = author
        self.Series = series
        self.Length = length
        self.ISBN = isbn
        self.Narator = narator
        self.Genres = genres
        self.Release_date = release_date
        self.Publisher = publisher
        self.Summary = summary
        self.Rating = rating


def main():
    File = "Test_data/Robert_Jordan/Wheel_of_Time/[01]_The_Eye_of_the_World/The_Eye_of_the_World-Robert_Jordan.mp3"
    start = 12
    length = 7
    chunk = 1024

    spf = wave.open(File, 'rb')
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    p = pyaudio.PyAudio()

    stream = p.open(format=
                    p.get_format_from_width(spf.getsampwidth()),
                    channels=spf.getnchannels(),
                    rate=spf.getframerate(),
                    output=True)

    pos = spf.getframerate() * length

    signal = signal[start * spf.getframerate():(start * spf.getframerate()) + pos]

    sig = signal[1:chunk]

    inc = 0
    data = 0

    # play
    while data != '':
        data = struct.pack("%dh" % (len(sig)), *list(sig))
        stream.write(data)
        inc = inc + chunk
        sig = signal[inc:inc + chunk]

    stream.close()
    p.terminate()


if __name__ == "__main__":
    main()