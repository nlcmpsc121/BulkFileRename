import os
import argparse
from PIL import Image

DEFAULT_SIZE = (320, 180) #change this value to change resizing dimensions x,y
x=1; #counter
print('Nathan Landivar npl5192\nBulk File Rename/ Image Resize Application\n')

def resize_image(input_dir, infile, output_dir="resized", size=DEFAULT_SIZE):
    outfile = os.path.splitext(infile)[0] + "_resized"
    extension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        img = img.resize((size[0], size[1]), Image.Resampling.LANCZOS)

        new_file = output_dir + "/" + outfile + extension
        img.save(new_file)
    except IOError:
        print("Unable to resize image {}".format(infile))


if __name__ == "__main__":
    dir = os.getcwd() #get path

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', help='Full Input Path')
    parser.add_argument('-o', '--output_dir', help='Full Output Path')

    parser.add_argument('-w', '--width', help='Resized Width')
    parser.add_argument('-t', '--height', help='Resized Height')

    args = parser.parse_args()

    if args.input_dir:
        input_dir = args.input_dir
    else:
        input_dir = dir + '/images'

    if args.output_dir:
        output_dir = args.output_dir
    else:
        output_dir = dir + '/resized'

    if args.width and args.height:
        size = (int(args.width), int(args.height))
    else:
        size = DEFAULT_SIZE

    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)

    # resizing
    try:
        for file in os.listdir(input_dir):
            resize_image(input_dir, file, output_dir, size=size)
            print('File ' + str(x) + ' successfuly resized. Output located in "resized" in the project folder.')
            x=x+1;
    except OSError:
        print('File(s) not found. Insert applicable file(s) into "images" in the project folder.')
