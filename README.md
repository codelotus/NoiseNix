# NoiseNix
---

A utility project for cleaning echo's and background noise from an mp3 recording.

At its core, NoiseNix simply a wrapper for passing [GregorR/rnnoise-models](https://github.com/GregorR/rnnoise-models) to [ffmpeg](https://ffmpeg.org/)

### Dependencies
1. [pipenv](https://pipenv.pypa.io/en/latest/)
1. [ffmpeg](https://ffmpeg.org/) - must be installed on your path

### Project Setup
1. This project uses git submodules to manage some dependencies.  To update submodules, after initial project clone, run:
    ```bash
    $ git submodule update --init --recursive
    ```
1. Use pipenv to setup local python environment
    ```bash
    $ pipenv --python 3.10
    $ pipenv install
    ```
1. Start pipenv shell
    ```bash
    $ pipenv shell
    ```
1. Run the script, passing `-h` to view usage
    ```bash
    $ python noise_nix.py -h
    ```
    Example:
    ```bash
    $ python noise_nix.py audio_file.mp3
    ```