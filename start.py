from loc import *
import argparse


def start():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "directory", help="Name of folder or directory u wish to scan")
    parser.add_argument(
        "-e", nargs='+', help="Extensions u wish to scan for", required=False)

    args = parser.parse_args()
    print(main(Path(args.directory)))
    print(sys.argv)


start()
