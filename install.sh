echo "Warning: sudo will be used to create the command in /usr/bin/"
echo "Nothing harmful will happen, you may just be prompted for a password"


if command -v python >/dev/null 2>&1; then
	:
else
	echo "python not installed, this installation will fail"
	echo "please install python with 'sudo apt install python2.7' or preferred version"
fi


sudo cp bin/todo /usr/bin/

name=$(whoami)
cp -r ./ /home/$name/mini-todo/
