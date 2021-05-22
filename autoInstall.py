import os;
libs={'numpy','matplotlib','pillow','sklearn','requests',\
    'jieba','beautifulsoup4','wheel','networks','sympy',\
    'pyinstaller','django','flask','werobot','pyqt5',\
        "pandas",'pyopengl','pypdf2','docopt','pygame'}

try:
    for lib in libs:
        os.system('pip install '+lib)
        print("{} has install successful".format(lib))
except:
    print("Failed")
