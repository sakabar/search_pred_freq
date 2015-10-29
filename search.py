#coding:utf-8
import sys
import re

def func(argvs, pred, keyword, cas):
    argc = len(argvs)

    dic = {}

    #キャッシュ読み込み
    # 'cache/cache.old'
    if argc < 4:
        raise Exception('Argument Error')
    if argc == 5:
        cache_file = argvs[4].strip('"')
        with open(cache_file, 'r') as f:
            for line in f:
                line = line.rstrip()
                lst = line.split(' ')
                dic[(lst[0], lst[1], lst[2])] = int(lst[3])

    arg_tpl = (pred, keyword, cas)
    if arg_tpl in dic:
        #もしキャッシュにあればそれを出力
        print "%s %s %s %d" % (pred, keyword, cas, dic[arg_tpl])
    else:
        cnt = 0 #頻度
        #なければサーチして辞書に追加、そして出力
        for line in sys.stdin:
            line = line.rstrip()

            # regex = re.compile("%s %s/[^;:/ ]*;[^:]+:%s[^ ]*$" % (pred, keyword, cas))
            regex_str = "^ *[0-9]+ %s %s(;[^:]*)?:%s" % (re.escape(pred), re.escape(keyword), re.escape(cas)) + "%?\*?$"
            regex = re.compile(regex_str)

            if regex.search(line):
                cnt += int(line.lstrip(' ').split(' ')[0])
                break #ヒットする行は一行のはず。

        #辞書を更新する
        dic[arg_tpl] = cnt
        print "%s %s %s %d" % (pred, keyword, cas, dic[arg_tpl])


        #終わったら辞書の情報をキャッシュに書き込み
        new_cache = 'cache/cache.new'
        with open(new_cache, 'w') as new_cache_f:
            for key in dic:
                new_cache_f.write("%s %s %s %d\n" % (key[0], key[1], key[2], dic[key]))
            new_cache_f.flush()



def main():
    argvs = sys.argv
    pred = argvs[1].strip('"')
    keyword = argvs[2].strip('"')
    cas = argvs[3].strip('"')

    func(argvs, pred, keyword, cas)

if __name__ == '__main__':
    main()
