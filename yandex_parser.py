import os
from dotenv import load_dotenv
import asyncio
import random

from yandex_music import ClientAsync

load_dotenv()
access_token = os.getenv("YANDEX_ACCESS")

client = ClientAsync(token=access_token)

async def sort_by_newest(tracks_ids: list[int]):
    track_dates = dict()
    all_tracks = await client.tracks(track_ids=tracks_ids)
    for track in all_tracks:
        if track.albums:
            album = track.albums[0]
            track_date = album.release_date
            track_dates[track.id] = track_date
    sorted_tracks = sorted(tracks_ids, key=lambda e: track_dates.get(e), reverse=True)
    return sorted_tracks


async def get_tracks_by_artist(artist: str):
    await client.init()
    result = []

    artist_id = (await client.search(text=str(artist))).artists.results[0]["id"]
    tracks = await client.artists_tracks(artist_id)

    tracks_ids = []
    for track in tracks.tracks:
        tracks_ids.append(track.id)
    sorted_tracks_ids = await sort_by_newest(tracks_ids)
    tracks = await client.tracks(track_ids=sorted_tracks_ids)
    for track in tracks:
        result.append(f"{track.id} | {track.title}")
    return "\n".join(result)


