import shutil

source = "../files/Rays.png";
target = "../files/Sunrays.png";

shutil.copyfile(source, target)

print(source + " is copied to " + target)