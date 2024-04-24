# spotify-cli
Simple CLI program that utilizes the Spotify API.

## Overview
This starter repo is meant to be used as an introduction to APIs.

## Getting Started
Ensure that you have Python installed on your machine.

You can do so by running:
```
which python
```
or
```
which python3
```

If both commands fail, visit https://www.python.org/downloads/ to download whichever version of Python you prefer.

This simple implementation is meant to be compatible with most versions of Python. It doesn't require any external dependencies being installed.

## Creating Spotify App
Follow this [brief section in this guide](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app) to create a Spotify app which will grant you a `CLIENT_ID` and `CLIENT_SECRET` that whose values you will need to fill in `credentials.py`.

# Running `spotify-genie`

To see what the program is capable of, from the root of the repo, run:

```
./spotify-genie --help
```

You will see:
```
Spotify Genie: Get information about your favorite artists, albums, and tracks from Spotify plus more.

options:
  -h, --help    show this help message and exit

subcommands:
  [subcommand]
    songs       Get song information about <artist>.
    albums      Get album information about <artist>.
    similar-to  [NOT YET IMPLEMENTED] Get artists that are similar to <artist>.

Run `./spotify-genie <subcommand> -h` to learn more about a subcommand. Available artists in this program are: Drake, Beyonce, Bad Bunny, Peso Pluma, Coldplay, Taylor Swift, Two Door
Cinema Club, Queen, Michael Jackson, 2Pac, J Cole. You can add more artists by updating artist_directory.py.
```
