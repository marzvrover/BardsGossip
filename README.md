# Bard's Gossip

Bard's Gossip's goal is to make music sharing as seamless as possible.

## Usage

I recommend copying `src/bardsgossip.py` into a folder in your `$PATH`.
```
cp ./src/bardsgossip.py $HOME/.scripts/bin/bardsgossip
```

Then, you can use `bardsgossip` to translate music links.

```shell
$ bardsgossip --apple-music "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# https://music.apple.com/US/album/never-gonna-give-you-up/1478168215?i=1478168518&app=music
```

You can also copy and/or open the link.

```shell
$ bardsgossip --copy --silent --apple-music "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
$ pbpaste # xsel --clipboard --output
# https://music.apple.com/US/album/never-gonna-give-you-up/1478168215?i=1478168518&app=music
$
$ bardsgossip --open --silent --apple-music "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# open "https://music.apple.com/US/album/never-gonna-give-you-up/1478168215?i=1478168518&app=music"
```
## `bardsgossip --help`
    usage: bardsgossip [-h] [--paste] [--open] [--copy] [--silent]
                      (--amazon-music | --apple-music | --deezer | --napster | --pandora | --qobuz | --songwhip | --spotify | --tidal | --youtube | --youtube-music)
                      url [x-callback-url]

    Convert your music links to other music services

    positional arguments:
      url              The URL of the song you want to convert
      x-callback-url   Optional: URI for x-callback-url

    optional arguments:
      -h, --help       show this help message and exit
      --paste          Paste the link to the clipboard. Still requires url, this is used to get around Shortcut limitations.
      --open           Open the link in a browser
      --copy           Copy the link to your clipboard
      --silent         Don't print the link
      --amazon-music   Get the Amazon Music link
      --apple-music    Get the Apple Music link
      --deezer         Get the Deezer link
      --napster        Get the Napster link
      --pandora        Get the Pandora link
      --qobuz          Get the Qobuz link
      --songwhip       Get the Songwhip link
      --spotify        Get the Spotify link
      --tidal          Get the Tidal link
      --youtube        Get the YouTube link
      --youtube-music  Get the YouTube Music link

## Siri Shortcuts

Example shortcut to: [Copy Spotify Link](https://www.icloud.com/shortcuts/5ed64dbb98da4189acbdf095f28b79a9). Shortcut file also attached to [the latest release](https://github.com/marzvrover/BardsGossip/releases/latest).

This uses the [Pythonista3](https://omz-software.com/pythonista/) app to execute the python code. You must add [bardsgossip.py](./src/bardsgossip.py) to the Pythonista3 app.

Example deeplink Pythonisa3 URL to open in the shortcut:
```
pythonista3://iCloud/Shortcuts/bardsgossip.py?action=run&argv=--paste&argv=--copy&argv=--silent&argv=--spotify&argv=place_holder
```

I highly recommend using the `--paste` option to get around Shortcut limitations that prevents sending Apple Music links. Otherwise it is the same as running it directly. However, to add additional arguments use `&argv=ARGUMENT` until you reach the last argument, with a placeholder for the expected url input if using `--paste`.
