#!/bin/zsh

if [ `hostname` != "tsumire" ]; then
  echo "Plese run in tsumire server" >&2
  exit 1
fi

if [ $# -ne 3 ]; then
  echo "Plese run with two arguments" >&2
  exit 1
fi
pred=$1 #用言代表表記
keyword=$2
cas=$3
file_name=`lv /local2/sasano/pred.list | LC_ALL=C grep " "$pred | awk '{print $1}'`".data.basic"
{
  echo /local2/sasano/pa.data.basic.split/$file_name
  echo "\"$pred\" \"$keyword\" \"$cas\""
  echo ""
} >&2

#「する/する:動」に関しては時間がかかりすぎるためカウントしない
if [ $pred = "する/する:動" ]; then
  echo "0 する/する:動 "$keyword":"$cas
else
  lv /local2/sasano/pa.data.basic.split/$file_name \
    | LC_ALL=C grep -- $pred" "$keyword"/[^;:/ ]*;[^:]\+:"$cas"[^ ]*$"
fi
 
