import os
import argparse

# posFilePath = "/media/slam/c7dbaae8-95ba-4e4e-af96-241a5f5eabef/DATA-TEST-202012/20201215151326_WM_SHANGHAI_AFA1119_20Hz/11_POINTCLOUD/LiDAR_1_POINTCLOUD"


def merge_pos_files(posFilePath):
    allDir = os.listdir(posFilePath)

    posFileslist = []
    for names in allDir:
        if names.endswith(".pos"):
            posFileslist.append(os.path.join(posFilePath, names))

    newfile = open(os.path.join(posFilePath, "merged_pos.txt"), 'w')
    for item in posFileslist:
        for txt in open(item, 'r'):
            newfile.write(txt)

    newfile.close()


def arg_parser():
    parser = argparse.ArgumentParser(description='merge pos files')
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='pos file path',
                        required=True)
    arg = parser.parse_args()
    return arg


if __name__ == "__main__":
    args = arg_parser()
    merge_pos_files(args.input)
