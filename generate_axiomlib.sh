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

python generate.py $OUT/reference
python generate.py $OUT/testing


cp extra/class_names $OUT/class_names
cp extra/param_names $OUT/param_names
cp extra/dataset.conf $OUT/$OUT.conf