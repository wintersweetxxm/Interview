import os

def main():
    i = 0

    for filename in os.listdir(dirName):
        dst =dstFilename + str(i) + ".jpg"
        src = dirName+filename
        dst = dirName+dst

        os.rename(src, dst)
        i += 1

if __name__ == '__main__':
    main()
