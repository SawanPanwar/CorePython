#Copy a Binary File
import shutil
source = "C:\\Users\\Sawan\\Desktop\\Rays.jpg";
target = "C:\\Users\\Sawan\\Desktop\\R\\Sunrays.jpg";
shutil.copyfile(source,target)
print(source + " is copied to " + target)
