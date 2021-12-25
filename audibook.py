"""
hej

"""

from audioplayer import AudioPlayer
import eyed3


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

    tag = eyeD3.Tag()
    tag.link(File)
    print
    tag.getArtist()
    print
    tag.getAlbum()
    print
    tag.getTitle()

    if eyeD3.isMp3File(File):
         audioFile = eyeD3.Mp3AudioFile(File)
         tag = audioFile.getTag()



if __name__ == "__main__":
    main()