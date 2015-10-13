# search_pred_freq

## 内容物
exe.sh これを実行すればOK
search_pred_freq.sh 述語の頻度を調べる
count_diff.sh シェルか? pythonか? 2つの出力の格フレームの頻度を比べる。

## USAGE
```
$lv hoge.knp | ./exe.sh | tee result.txt | python sum.py > count.txt
$cat result
# S-ID:1 KNP:4.13-CF1.1 DATE:2015/10/07 SCORE:-25.79032
# S-ID:2 KNP:4.13-CF1.1 DATE:2015/10/07 SCORE:-34.01050
   8748 負ける/まける:動 自分/じぶん;c人:ニ格*
    581 負ける/まける:動 自分/じぶん;c人:ニ格%*
# S-ID:3 KNP:4.13-CF1.1 DATE:2015/10/07 SCORE:-32.84601
   2449 勝つ/かつ:動 自分/じぶん;c人:ニ格*
    226 勝つ/かつ:動 自分/じぶん;c人:ニ格%*
$cat count.txt #文ID<tab>文中に現れる述語の格フレームにおける頻度の和
1       0
2       9329
3       2675
4       0
5       9
6       10
$join orig_count.txt changed_count.txt | awk '{print $1" "($3+1)/($2+1)}' | awk '$2 > 1 {print $0}' > gt_one.txt
$lv gt_one | python show.py
```
