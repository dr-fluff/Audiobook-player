import time
import timeit

from plexapi.server import PlexServer
from plex import config
#import config

plex = PlexServer(config.PLEX_URL, config.PLEX_TOKEN)


# TODO add option for multiple different library names
# Get all books from plex server
def get_metadata():
    plex_audi_section = plex.library.section('Audiobooks')
    books = []

    for author in plex_audi_section.all():
        for book in author.albums():

            dict = book.__dict__
            tracks = {}
            duration = 0
            for i, t in enumerate(book.tracks()):
                tracks[i] = t.title
                duration += t.duration

            dict['track'] = tracks
            dict['duration'] = duration
            books.append(dict)

    stop = timeit.default_timer()

    return books


def play():
    pass

