#coding:utf-8
import sys

def main():
    file_name = 'output.txt' #FIXME
    file_name='/home/lr/tsakaki/work/replace_with_antonym/output_with_knp.txt'
    lines = map(lambda l: l.rstrip(), open(file_name, "r").readlines())

    for line in sys.stdin:
        line = line.rstrip()
        ind = int(line.split(' ')[0]) - 1 #インデックスは0-base
        print lines[ind]

if __name__ == '__main__':
    main()
