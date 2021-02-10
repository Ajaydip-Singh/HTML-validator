#!/usr/bin/env zsh

echo "The script is running"

python ~/Documents/automations/webdev_automations/htmlvalidator.py $1

cat  ~/Documents/automations/webdev_automations/validatorResult.txt

rm  ~/Documents/automations/webdev_automations/validatorResult.txt

echo "Script has finished running"
