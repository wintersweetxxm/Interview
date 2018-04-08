from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def main(filename="test.png",width=40,height=40,outfilename="out_file"):
    text = ""
    im = Image.open(filename)
    im = im.resize((width,height),Image.NEAREST)
    for i in range(height):
        for j in range(width):
            text += get_char(*im.getpixel((j,i)))
    text += "\n"
    print(text)
    with open("outfilename", 'w') as f:
        f.write(text)

def write_file(outfilename, content):
    with open(outfilename, "w") as f:
        f.write(content)
def parse_param():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file")
    parser.add_argument('-o',"--out_file")
    parser.add_argument("--width", type=int, default=80)
    parser.add_argument("--height",type=int, default=80)
    arsg = parser.parse_args()

    width, height, in_file, out_file = arsg.width, arsg.height, arsg.input_file, arsg.out_file
    return(width,height, in_file, out_file)


def get_char(r,g,b, alpha = 256):
    if alpha ==0:
        return (' ')
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

'''
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
'''
if __name__ == '__main__':
    width, height, in_f, out_f = parse_param()
    main(filename="ascii_dora.png",width=width,height=height,outfilename=out_f)

