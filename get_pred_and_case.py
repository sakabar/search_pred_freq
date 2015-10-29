#coding:utf-8

import sys
import re

def get_normalized_cand_form(basic_phrase):
    pat = re.compile("<正規化代表表記:([^>]+)>")
    match_obj = pat.search(basic_phrase)
    if match_obj:
        return match_obj.group(1)
    else:
        return "" #見つからなかったら空文字を返す
        # raise Exception('error in ' + basic_phrase)

def get_verb_normalized_cand_form(basic_phrase):
    pat = re.compile("<用言代表表記:([^>]+)>")
    match_obj = pat.search(basic_phrase)
    if match_obj:
        return match_obj.group(1)
    else:
        return "" #見つからなかったら空文字を返す
        # raise Exception('error in ' + basic_phrase)


#KNPの出力結果と、"ヲ/C/花/2/0/1"のような文字列を受け取り、
#("花/か?花/はな", "ヲ格")のような、正規化代表表記と格のペアを返す
def my_map(knp_lines, case_arg):
    #ヲ/C/花/2/0/1
    lst = case_arg.split('/')
    basic_phrases = [line for line in knp_lines if line[0] == '+']
    ind = int(lst[3])
    basic_phrase = basic_phrases[ind]
    normalized_cand_form = get_normalized_cand_form(basic_phrase)
    if normalized_cand_form == "":
        return ("", "")
    else:
        return (normalized_cand_form, lst[0] + "格")

#格解析結果の行を読み込んでいろいろ返す
def get_pred_and_case_from_result_line(knp_lines, case_line):
    #normalized_cand_form_pat = re.compile("<正規化代表表記:([^>]+)>")
    #こっちのほうがいい?

    # normalized_cand_form_pat = re.compile("<用言代表表記:([^>]+)>")
    pat = re.compile("<格解析結果:[^/]+/[^:]+:([^0-9]+)[0-9]+:([^>]+)>")
    match_obj = pat.search(case_line)

    if match_obj:
        pred_type = match_obj.group(1)
        pred = get_verb_normalized_cand_form(case_line)
        if pred == "": #用言代表表記が存在しなかったら正規化代表表記を使う
            pred = get_normalized_cand_form(case_line)
        if pred == "":
            raise Exception(case_line)
        cases = [arg for arg in match_obj.group(2).split(';') if arg.split('/')[1] != 'U']
        ans_lst = [ans for ans in [my_map(knp_lines, case) for case in cases] if ans != ("", "") and (ans[1] == "ガ格" or ans[1] == "ヲ格" or ans[1] == "ニ格" or ans[1] == "カラ格")] #ガ/ヲ/ニ格のみ使う
        return (pred+":"+pred_type, ans_lst)

    else:
        raise Exception('Error in ' + case_line)

    # return ("見る/みる:動", [("花/か?花/はな", "ヲ格")])


def get_pred_and_case(knp_lines):
    case_result_lst = [line for line in knp_lines if "格解析結果" in line]
    if len(case_result_lst) == 0:
        return []
    else:
        return [get_pred_and_case_from_result_line(knp_lines, case_line) for case_line in case_result_lst]

def main():
    knp_lines = []

    for line in sys.stdin:
        line = line.rstrip()

        knp_lines.append(line)
        if line == "EOS":
            ans = get_pred_and_case(knp_lines)
            if len(ans) == 0:
                pass
            else:
                for ans_pred, ans_cases in ans:
                    print to_str(ans_pred, ans_cases)
                    
            print "EOS"
            knp_lines = []

def to_str(pred, cases):
    return ("%s " % pred) + " ".join([case_tpl[0]+":"+case_tpl[1] for case_tpl in cases])
        

if __name__ == '__main__':
    main()
