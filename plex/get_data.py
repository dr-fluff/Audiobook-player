from plexapi.server import PlexServer
from plex import config

plex = PlexServer(config.PLEX_URL, config.PLEX_TOKEN)


# TODO add option for multiple different library names
# Get all books from plex server
def get_metadata():
    plex_audi_section = plex.library.section('Audiobooks')
    books = []

    for author in plex_audi_section.all():
        for b in author.albums():
            books.append(b.__dict__)

    return books


if __name__ == '__main__':
    lib = get_metadata()
    print(lib)
