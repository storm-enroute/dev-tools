#!/usr/bin/env python

import argparse
import sys


def log(s):
  print(s)
  sys.stdout.flush()


def abort(s):
  log(s)
  sys.exit(1)


def main(args):
  parser = argparse.ArgumentParser(description="Run basic lint checks.")
  parser.add_argument("--path", required=True,
    help="Path to specific file to check, or directory to check recursively.")
  args = parser.parse_args(args[1:])
  print(args.path)


if __name__ == "__main__":
  main(sys.argv)
