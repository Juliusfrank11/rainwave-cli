# rainwave-cli
A (very primative) command line program for rainwave

Essentially this only displays the current song info for a rainwave station in terminal and plays that station via `mpv`. Not planning on adding more features right now as I never really used the voting feature that much on rainwave

You can use the standard `mpv` controls of `9` and `0` to adjust the volume.

## Dependences
MacOS:
```
brew install mpv python3
pip3 install python-rainwave-client typer
```
Ubuntu:
```
sudo apt install mpv python3
pip3 install python-rainwave-client typer
```

## Usage
```
bash main.sh {station}
```

`station` is one of `all|games|ocremix|covers|chiptune`.

You can use the standard `mpv` controls of `9` and `0` to adjust the volume.

You need to `^Z` to exist the program
