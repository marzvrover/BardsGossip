# Bard's Gossip

Bard's Gossip's goal is to make music sharing as seamless as possible.

## Usage

I recommend copying `src/bardgossip.py` into a folder in your `$PATH`.
```
cp ./src/bardgossip.py $HOME/.scripts/bin/bardgossip
```

Then, you can use `bardgossip` to translate music links.

```shell
$ bardgossip --apple-music "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# https://music.apple.com/US/album/never-gonna-give-you-up/1478168215?i=1478168518&app=music
```

You can also copy and/or open the link.

```shell
$ bardgossip --copy --silent --apple-music "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
$ pbpaste # xsel --clipboard --output
# https://music.apple.com/US/album/never-gonna-give-you-up/1478168215?i=1478168518&app=music
$
$ bardgossip --open --silent --apple-music "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# open "https://music.apple.com/US/album/never-gonna-give-you-up/1478168215?i=1478168518&app=music"
```
## `bardgossip --help`
    usage: bardgossip [-h] [--open] [--copy] [--silent]
                      (--amazon-music | --apple-music | --deezer | --napster | --pandora | --qobuz | --songwhip | --spotify | --tidal | --youtube | --youtube-music)
                      url [x-callback-url]

    Convert your music links to other music services

    positional arguments:
      url              The URL of the song you want to convert
      x-callback-url   Optional: URI for x-callback-url

    optional arguments:
      -h, --help       show this help message and exit
      --open           Open the link in a browser
      --copy           Copy the link to your clipboard
      --silent         Don't print the link
      --amazon-music   Get the Amazon Music link
      --apple-music    Get the Apple Music link
      --deezer         Get the Deezer link
      --napster        Get the Napster link
      --pandora        Get the Pandora link
      --qobuz          Get the Qobuz link
      --songwhip       Get the SongWhip link
      --spotify        Get the Spotify link
      --tidal          Get the Tidal link
      --youtube        Get the YouTube link
      --youtube-music  Get the YouTube Music link
