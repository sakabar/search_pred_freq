#!/bin/zsh

set -ue

# outputdir=output151022
inputdir=input151026_2300
outputdir=output151026_2300

#これ動かして帰ります!
function f(){
  knp_filename=$1
  lv $knp_filename | python get_pred_and_case.py | awk -f split_args_of_pred.awk | sed -e 's|:\([^ ]\+\)格$| \1格|g' | ./exe.sh > $outputdir/$knp_filename:t:r".pred.freq"
}

# f ~/work/replace_with_antonym/$inputdir/orig.knp
# f ~/work/replace_with_antonym/$inputdir/changed.knp

f $inputdir/orig.knp
f $inputdir/changed.knp
