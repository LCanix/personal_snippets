#!/bin/bash
timestamp=$(date +%y-%m-%d_%H-%M-%S)
randBoolean=$(($RANDOM%2))
if [ "$randBoolean" -eq "1" ]
then
    text="<html><head><title>foo bar</title></head><body><div id=\"bar\">OK</div><div id=\"foo\">Another word</div></body></html>"
else
    text="<html><head><title>foo bar</title></head><body><div id=\"bar\">FAILED</div><div id=\"foo\">Another word</div></body></html>"
fi

sleep 2
folder_name="result_$timestamp"
folder_path="result_folder/$folder_name"
mkdir $folder_path
file_path="$folder_path/result.html"
touch $file_path
echo $text >> $file_path
exit 1
