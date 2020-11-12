import argh

import util

def main(in_filepath, per_part=100):
    xs = open(in_filepath).readlines()
    xs = [x.strip() for x in xs]
    for i, part in enumerate(go(xs, per_part)):
        print(part)
        with open(f"{in_filepath}-{i}", "w") as f:
            f.write("\n".join(part) + '\n')


if __name__ == "__main__":
    argh.dispatch_command(main)
