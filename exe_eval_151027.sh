#!/bin/zsh

outputdir=output151026_2300 
for f in $outputdir/*.pred.freq; do
  awk -f sum_pred_freq_of_each_sentence.awk $f > $f:r:r".sentence.freq"
done


paste -d '\t' $outputdir/orig.sentence.freq $outputdir/changed.sentence.freq | cat -n \
  | awk '{r=($3+1.0)/($2+1.0); printf("%s %s %s %.6f\n", $1, $2, $3, r)}' #| awk '$4 >= 1.5 {print $0}'

