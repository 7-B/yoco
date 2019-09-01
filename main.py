import argparse
from sketchKeras import sketch
from simplification import simplify
   
def main():
    parser = argparse.ArgumentParser(description='Sketch Keras + simplification demo')
    parser.add_argument('--img', type=str, help='Input image file.')
    opt = parser.parse_args()

    sketch(opt.img)
    simplify()


if __name__ == "__main__":
    main()