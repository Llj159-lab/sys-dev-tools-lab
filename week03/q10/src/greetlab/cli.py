import argparse
import sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    try:
        a = p.parse_args()
        print(f"Hello, {a.name}!")
    except SystemExit as e:
        sys.exit(2)
