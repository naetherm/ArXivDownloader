# -*- coding: utf-8 -*-
# Copyright 2019-2020, University of Freiburg.
# Chair of Algorithms and Data Structures.
# Markus Näther <naetherm@informatik.uni-freiburg.de>

import os

import requests
import urllib.request
import logging
import multiprocessing
from multiprocessing.pool import ThreadPool
from time import time as timer

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

class ArXivPaperIDFetcher(object):

  def __init__(self):
    super(ArXivPaperIDFetcher, self).__init__()

class ArXivPaper(object):

  def __init__(
    self,
    pid,
    download_dir
  ):
    super(ArXivPaper, self).__init__()

    self.pid = pid
    self.download_dir = download_dir

  def download(self):
    url = "https://export.arxiv.org/e-print/" + self.pid

    try:
      if not os.path.exists(os.path.join(self.download_dir, "{}.tar.gz".format(self.pid))):
        urllib.request.urlretrieve(url, os.path.join(self.download_dir, "{}.tar.gz".format(self.pid)))
      else:
        logger.warning("File already exists, will skip.")
    except:
      logger.warning(
        "Unable to download the file '{}' - skipping.".format(
          os.path.join(self.download_dir, "{}.tar.gz".format(self.pid))))

class ArXiv(object):

  def __init__(self):
    super(ArXiv, self).__init__()

  @staticmethod
  def download(paper):
    paper.download()

  @staticmethod
  def download_by_pid(pid, download_dir):
    paper = ArXivPaper(pid, download_dir)
    ArXiv.download(paper)
    
  @staticmethod
  def fetch_url(url):
    try:
      response = urllib.request.urlopen(url)
      return True, url
    except Exception as e:
      return False, url

  @staticmethod
  def fetch_papers(data_dir):
    # TODO(naetherm): Implement this
    # This is super simple ...
    small_y_range = ["08", "09", "10", "11", "12", "13", "14"]
    large_y_range = ["15", "16", "17", "18", "19", "20"]
    month_range = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    list_of_urls = []
    with open (data_dir+"/paper_ids.txt", 'w') as fout:
      for y in small_y_range:
        for m in month_range:
          for p in ["%04d" % i for i in range(1, 9999)]:
            list_of_urls.append("https://export.arxiv.org/abs/{}{}.{}".format(y, m, p))
      for y in large_y_range:
        for m in month_range:
          for p in ["%05d" % i for i in range(1, 99999)]:
            list_of_urls.append("https://export.arxiv.org/abs/{}{}.{}".format(y, m, p))
      print(f"Generated {len(list_of_urls)} urls")
      result_urls = []
      results = ThreadPool(multiprocessing.cpu_count()).imap_unordered(ArXiv.fetch_url, list_of_urls)
      for f, url in results:
        if f is True:
          fout.write(url)
