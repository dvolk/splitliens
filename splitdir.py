import pathlib, os

import argh

import util

def main(in_dir, per_part=100):
    p = pathlib.Path(in_dir)
    xs = list(p.glob("*"))
    xs = sorted(xs, key=os.path.getmtime)
    for i, part in enumerate(util.go(xs, per_part)):
        print(f"mkdir {in_dir}-{i}")
        for x in part:
            print(f"mv {x} {in_dir}-{i}/{x.name}")

if __name__ == "__main__":
    argh.dispatch_command(main)
