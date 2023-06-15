file = 'No.3 Start.bat'
def create_bat_file(file_path):
    with open(file, 'w') as bat:
        pypash1 = input("Pythonのファイルのpathを入力してください：")
        icopath = input("アイコンのファイルのpathを入力してください：")
        bat.write("pyinstaller " + pypash1 + " --onefile -i "+ icopath)
        print(file_path)


create_bat_file(file)