#coding:utf-8
import sys

def get_sentence_id(line):
    return int(line.split(' ')[1][5:])

def main():
    #1行目の'#'から始まる行を読み込んだ時に文字を出力するのを抑制
    print_flag = False
    count = 0
    s_id = -1
    line = ""
        
    for line in sys.stdin:
        line = line.rstrip()
        if (not print_flag) and line[0] == '#':
            s_id = get_sentence_id(line)
            print_flag = True

        elif print_flag and line[0] == '#':
            print "%d\t%d" % (s_id, count)
            s_id = get_sentence_id(line)
            count = 0
        else:
            num = int(line.lstrip().split(' ')[0])
            count += num

    #ループから抜けた後、最後のdocのぶんを出力する
    print "%d\t%d" % (s_id, count)

if __name__ == '__main__':
    main()
