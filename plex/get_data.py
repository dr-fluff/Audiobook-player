
from plexapi import myplex
from plexapi.server import PlexServer

from plexapi.myplex import MyPlexAccount
from plexapi.sync import AUDIO_BITRATE_320_KBPS

import plex_config


# Get server instance from login info
def _plex_server_login():
    client = myplex.MyPlexAccount(plex_config.USERNAME, plex_config.PASSWORD)
    server = client.resource(plex_config.SERVER).connect()
    return server


def token_login():
    plex = PlexServer(plex_config.baseurl, plex_config.token)

    return plex


# Get all books from plex server
def get():
    server = token_login()
    plex_lib = server.library.section('Audiobooks')
    print("logged in to plex")

    lib_dict = {"key": "Title"}
    amount_of_albums = 0
    for author in plex_lib.all():
        amount_of_albums += len(author.albums())
        for b in author.albums():
            lib_dict[b.key] = b.title


    print("amount of books in library: ", amount_of_albums)
