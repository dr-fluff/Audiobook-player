"""

"""
import os
import time

from tinytag import TinyTag
from plex import get_data


class Book:
    def __init__(self, title, author, release_date, series, length, isbn, narrator, genres,
                 publisher, summary, rating, last_position, chapters, bitrate, filesize, plex_key):
        self.Title = title
        self.Author = author
        self.Series = series
        self.Length = length
        self.ISBN = isbn
        self.Narrator = narrator
        self.Genres = genres
        self.Release_date = release_date
        self.Publisher = publisher
        self.Summary = summary
        self.Rating = rating
        self.Last_position = last_position
        self.Chapters = chapters
        self.Bitrate = bitrate
        self.Filesize = filesize
        self.Plex_key = plex_key

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}


class Library:
    def __init__(self):
        self.Books = []

    def remove_book(self, book):
        self.Books.remove(book)

    def add_book(self, book):
        self.Books.append(book)

    def sort_by_title(self):
        pass

    def sort_by_author(self):
        pass

    def sort_by_release_date(self):
        pass


lib = Library()


def parse_plex_library(plex_lib):

    for dict in plex_lib:
        for key, val in dict.items():
            print(key)

        print("--------")
        time.sleep(1)




def init_book_from_filepath(file_path):
    meta = TinyTag.get(file_path)
    return Book(meta.title, meta.albumartist, meta.year, meta.album, meta.duration, None, meta.composer, meta.genre,
                None, meta.extra, None, None, None, meta.bitrate, meta.filesize)


def list_files_in_library(library_path):
    files = []
    library = Library(None)

    # TODO add all different file types
    for r, d, f in os.walk(library_path):
        for file in f:
            if '.mp3' in file or '.m4b' in file or '.m4a' in file:
                file_path = os.path.join(r, file)
                files.append(file_path)
                book = init_book_from_filepath(file_path)
                library.add_book(book)

    print(library.Books)


def main():
    plex_lib_dict = get_data.get_metadata()
    parse_plex_library(plex_lib_dict)


if __name__ == "__main__":
    main()
