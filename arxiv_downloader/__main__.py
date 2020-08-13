# -*- coding: utf-8 -*-
# Copyright 2019-2020, University of Freiburg.
# Chair of Algorithms and Data Structures.
# Markus Näther <naetherm@informatik.uni-freiburg.de>

import sys
import argparse

from arxiv_downloader import ArXiv, ArXivPaper


def main(argv=None):

  if argv == None:
    argv = sys.argv[1:]

  parser = argparse.ArgumentParser(
    prog="arxiv_downloader", 
    description="Downloads a single paper source code by its id (--paper-id) to the download directory (--download-dir).", 
    add_help=True)

  parser.add_argument(
    "--paper-id",
    dest="paper_id",
    type=str,
    required=True,
    help="The ID of the paper to download"
  )
  parser.add_argument(
    "--download-dir",
    dest="download_dir",
    type=str,
    required=True,
    help="The directory where to download the file."
  )

  args = parser.parse_args()

  ArXiv.download_by_pid(args.paper_id, args.download_dir)

def fetch_main():
  
  parser = argparse.ArgumentParser(
    prog="arxiv_fetcher", 
    description="Script for retrieving and generating the paper-ids.txt file.", 
    add_help=True)

  parser.add_argument(
    "--data-dir",
    dest="data_dir",
    type=str,
    required=True,
    help="The path to the directory where the paper-ids.txt should be saved."
  )
  args = parser.parse_args()
  ArXiv.fetch_papers(args.data_dir)

def autoload_main(argv=None):

  if argv == None:
    argv = sys.argv[1:]

  parser = argparse.ArgumentParser(
    prog="arxiv_autoload", 
    description="Downloads all paper ids given by a file (--paper-ids) to a specific directory (--download-dir)",
    add_help=True)
  parser.add_argument(
    "--paper-ids",
    dest="paper_ids",
    type=str,
    required=True,
    help="Path to the file holding all paper ids to download."
  )
  parser.add_argument(
    "--download-dir",
    dest="download_dir",
    type=str,
    required=True,
    help="The directory where to download the file."
  )

  args = parser.parse_args()

  with open(args.paper_ids, 'r') as fin:
    for lin in fin:
      lin = lin.replace('\n', '')
      print("Downloading ArXiv paper: {}".format(lin))
      ArXiv.download_by_pid(lin, args.download_dir)

if __name__ == '__main__':
  main()
