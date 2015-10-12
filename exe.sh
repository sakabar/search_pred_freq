#!/bin/zsh

set -u
# set -e #途中で失敗したらエラー

#KNPの出力を標準入力から読み込む
while read knp_line; do
    if [ `echo $knp_line | grep -c "^#"` -eq 1 ]; then
	echo $knp_line
    else
	grepped=`echo $knp_line | LC_ALL=C grep -c "<格解析結果:"`
	if [ $grepped -eq 1 ]; then
	    verb_type=`echo $knp_line | LC_ALL=C grep -o "<用言:[^>]*>" | sed -e 's/<用言:\([^>]*\)>/\1/g'`
	    verb_cand_form=`echo $knp_line | LC_ALL=C grep -o "<用言代表表記:[^>]*>" | sed -e 's/<用言代表表記:\([^>]*\)>/\1/g'`
	    case_num=`echo $knp_line | LC_ALL=C grep -o "<格解析結果:[^>]*>" | sed -e 's|<格解析結果:[^/]*/[^:]*:[^:]*:\([^>]*\)>|\1|g' | tr ';' '\n' | grep -c -v "/U/"`
	    case_res=`echo $knp_line | LC_ALL=C grep -o "<格解析結果:[^>]*>" | sed -e 's|<格解析結果:[^/]*/[^:]*:[^:]*:\([^>]*\)>|\1|g' | tr ';' '\n' | grep -v "/U/" | head -n1`

	    if [ $case_num -ne 0 ]; then
		keyword=`echo $case_res | awk -F'/' '{print $3}'`
		cas=`echo $case_res | awk -F'/' '{print $1}'`"格"
		verb=$verb_cand_form":"$verb_type
		# echo $verb
		# echo $keyword
		# echo $cas
		./search_pred_freq.sh $verb $keyword $cas
		# exit
	    fi
	fi
    fi
done
