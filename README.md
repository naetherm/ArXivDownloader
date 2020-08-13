# ArXiv Downloader

Just install via ```python setup.py install --user```.

There are then three programs available:

```
arxiv_fetcher: Recieve a list of all available papers on arxiv
arxiv_autoload: Downloads all papers within a given txt file (usually works on the resulting txt of the above step)
arxiv_downloader: Downloads a single, given, paper by its id
```

## Usage

### Retrieving all valid paper ids:

```
arxiv-fetcher --data-dir=.
```

### Downloading all papers of the generated paper-ids.txt

```
arxiv_autoload --paper-ids=./paper-ids.txt --download-dir=./tmp/
```
