"""

"""
import os
from tinytag import TinyTag


class Book:
    def __init__(self, title, author, series, length, isbn, narator, genres, release_date,
                 publisher, summary, rating, last_position, chapters, bitrate, filesize):
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
        self.Last_position = last_position
        self.Chapters = chapters
        self.Bitrate = bitrate
        self.Filesize = filesize

    def init_book_from_filepath(self, file_path):
        meta = TinyTag.get(file_path)
        self.Title = meta.title
        self.Author = meta.albumartist
        self.Series = meta.album
        self.Length = meta.duration
        self.Narator = meta.composer
        self.Genres = meta.genre
        self.Release_date = meta.year
        self.Bitrate = meta.bitrate
        self.Filesize = meta.filesize
        return self

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


class Library:
    def __init__(self):
        print("ska fixas")


def list_files_in_library(library_path):
    files = []

    # TODO add all different file types
    for r, d, f in os.walk(library_path):
        for file in f:
            if '.mp3' in file or '.m4b' in file or '.m4a' in file:
                file_path = os.path.join(r, file)
                files.append(file_path)
                book = Book.init_book_from_filepath(file_path)
                print(book)


# def metadata(file):
#     meta = TinyTag.get(file)
#
#     b = Book(title=meta.title,
#              author=meta.artist,
#              series=meta.album,
#              length=meta.duration,
#              isbn=None,
#              narator=meta.composer,
#              genres=meta.genre,
#              release_date=meta.year,
#              publisher=None,
#              summary=None,
#              rating=None,
#              last_position=None,
#              chapters=meta.track_total,
#              bitrate=meta.bitrate,
#              filesize=meta.filesize)
#
#     print(b.as_dict())


def main():
    # library_path = "Library/"
    library_path = "/home/oliver/Documents/Projekt/Audiobook-player/Library/"

    list_files_in_library(library_path)


if __name__ == "__main__":
    main()
