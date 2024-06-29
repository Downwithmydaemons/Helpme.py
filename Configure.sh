!#/bin/bash

sudo mv Enumhelp.py /opt/. && chmod +x Enumhelp.py

echo 'alias Helpme="./opt/Enumhelp.py"' >> .zshrc

print('Help me has been set up\n Use "Helpme" to call this tool')
