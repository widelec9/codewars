def song_decoder(song):
    return ' '.join([w for w in song.split('WUB') if w and w != 'WUB'])
