from rainwaveclient import RainwaveClient
import typer

def read_file(filename):
	return open(filename).read().strip()

def make_info_string(song):
	return f'Title: {song.title}\nStation/Album: {song.album.name}\nArtist(s): {song.artist_string}'

def print_info(song):
	print(make_info_string(song))

app = typer.Typer()

rw = RainwaveClient(user_id=read_file('.id'),key=read_file('.key'))

@app.command()
def display(station_int):
	station_int = int(station_int) - 1
	current_song = rw.channels[station_int].schedule_current.song
	print_info(current_song)
	while True:
		try:
			song = rw.channels[station_int].schedule_current.song
			if make_info_string(song) != make_info_string(current_song):
				current_song = song
				print('\n---New Song---')
				print_info(current_song)
		except KeyboardInterrupt:
			exit()

if __name__ == '__main__':
	app()
