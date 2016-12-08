#!/bin/bash
cd /home/pi/Scripting/
touch email.txt
python weatherUp.py >> email.txt
mail 6263994354@messaging.sprintpcs.com < email.txt
rm email.txt
