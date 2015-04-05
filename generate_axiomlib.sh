#!/bin/bash
OUT=$1

if [ $# -eq 0 ]
then 
	OUT="dataset"
fi

if !([ -d "$OUT" ])
then 
	mkdir "$OUT" 
fi

length=$(shuf -i 3-6 -n 1)
abnormal=$(cat /dev/urandom | tr -dc 'ABCDEFG' | fold -w $length | head -n 1)

python generate.py $OUT/reference $abnormal
python generate.py $OUT/testing $abnormal

cp extra/class_names $OUT/class_names
cp extra/param_names $OUT/param_names
cp extra/dataset.conf $OUT/$OUT.conf
