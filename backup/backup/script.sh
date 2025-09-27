#!/bin/bash
backed_up=0
for file in ~/linux/*; do 
cp -r -u  "$file"  ~/linux/backup;
((backed_up++))
done
echo "Files backed up: $backed_up"
