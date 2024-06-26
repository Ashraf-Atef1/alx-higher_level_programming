#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the value ofthe X-Request-Idvariable found in the header of the response"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as res:
        print(res.headers["X-Request-Id"])
