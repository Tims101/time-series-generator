@echo off

set OUT=%1
if [%1]==[] set OUT="dataset"
if not exist %OUT% mkdir %OUT%

generate.py %OUT%/reference
generate.py %OUT%/testing

copy extra\class_names %OUT%\class_names
copy extra\param_names %OUT%\param_names
copy extra\dataset.conf %OUT%\%OUT%.conf


