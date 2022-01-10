"""

"""
import os
import time

from tinytag import TinyTag
from plex import get_data


class Book:
    def __init__(self, title, author, release_date, series, length, isbn, narrator, genres,
                 publisher, summary, rating, last_position, chapters, bitrate, filesize, plex_key, art=None):
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
        self.Art = art

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


def _find(dict, keyword):
    for key, val in dict.items():
        if keyword == key:
            return val


def parse_plex_library(plex_lib):
    print("parse plex lib")
    for plex_book_dict in plex_lib:
        book = Book(title=_find(plex_book_dict['_data'], 'title'),
                    author=_find(plex_book_dict['_data'], 'parentTitle'),
                    release_date=_find(plex_book_dict['_data'], 'originallyAvailableAt'),
                    series=_find(plex_book_dict['_data'], 'titleSort'),
                    length=plex_book_dict['duration'],
                    isbn=None,
                    narrator=plex_book_dict['styles'],
                    genres=plex_book_dict['genres'],
                    publisher=plex_book_dict['studio'],
                    summary=plex_book_dict['summary'],
                    rating=_find(plex_book_dict['_data'], 'rating'),
                    last_position=None,
                    chapters=plex_book_dict['track'],
                    bitrate=None,
                    filesize=None,
                    plex_key=plex_book_dict['key'],
                    art=None)

        lib.add_book(book)


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
