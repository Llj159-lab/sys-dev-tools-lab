import argparse


def add(a: float, b: float) -> float:
    return a + b


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()

    result = add(args.a, args.b)
    print(f"{args.a} + {args.b} = {result}")


if __name__ == "__main__":
    main()
