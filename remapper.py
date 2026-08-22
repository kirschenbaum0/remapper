import os
print(r"""
 |  __ \                               (_) |
 | |  | | ___  ___ ___  _ __ ___  _ __  _| | ___ _ __
 | |  | |/ _ \/ __/ _ \| '_ ` _ \| '_ \| | |/ _ \ '__|
 | |__| |  __/ (_| (_) | | | | | | |_) | | |  __/ |
 |_____/ \___|\___\___/|_| |_| |_| .__/|_|_|\___|_|
                                 | |
                                 |_|
""")

modname = input("Jar Name: ")
modver = input("Mod Version: ")
print("Remapping...")
os.system(
    f'java -jar remapper.jar --input "{modname}" --output remapped.jar --minecraftVersion "{modver}"'
)
print("Done remapping.")
print("Decompiling...")
os.system("java -jar cfr.jar remapped.jar --outputdir src")
print("Done decompiling.")
delete = input("Would you like to delete the remapped jar? Y/N: ")
if delete == "Y" or "y":
    os.remove("remapped.jar")
print("Done! Your source is at src/. Warning: It still is not fully buildable. You need to add gradle for the source to be buildable.")
print("Thanks for using the decompiler.")
