import argparse
from demo_pkg.core import hello


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    print(hello(args.name))


if __name__ == "__main__":
    main()
