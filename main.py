import argparse
from sketch import sketch
from simplification import simplify

def main():
    parser = argparse.ArgumentParser(description='Sketch + simplification demo')
    parser.add_argument('--img', type=str, help='Input image file.')
    opt = parser.parse_args()

    sketch(opt.img)
    simplify('sketch.jpg')


if __name__ == "__main__":
    main()