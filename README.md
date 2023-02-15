# resurrection-man
grave robbing and other fun things

# dependencies
- [pyenv](https://github.com/pyenv/pyenv#automatic-installer)

- [pipenv](https://pipenv.pypa.io/en/latest/)

- `python -m pip install pipenv`
(This installs pip which will later be used to set up pipenv. Try not to confuse the commands via terminal history like amp did)

- [make](https://www.technewstoday.com/install-and-use-make-in-windows/)

- `winget install gnuwin32.make`

- don't forget to add make to the path in windows. example: `C:\Program Files (x86)\GnuWin32\bin`

*on a real OS this isn't a problem, but on windows you gotta use gnumake*

# getting started

WSL causes more problems than its worth, use native dev tools if you're using Windows. [See this issue](https://github.com/Murder-Hobo-Interactive/resurrection-man/issues/15)

- *install the dependencies listed above*

- make sure that `python` is a valid command
    - In linux
        - if not set alias in `.bashrc` and run `source ~/.bashrc` ->  *set alias in `.bashrc` on linux*

        - `alias python='python3'`

*install and run*

- `python -m pipenv install`

- `make run`

# Scene Builder
- `make scene-builder`
    - left click: place actors
    - mouse scroll: change selected actor
    - q: quit and save to `new_level.pickle`
# editing assets
`make edit`

# type checking
`make types`

# uml
`make uml`

- [uml reference](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/)

might require graphviz

`brew install graphviz`

or

`apt-get install graphviz`


## Packages
![packages uml](./packages.png)

## Classes
![classes uml](./classes.png)
