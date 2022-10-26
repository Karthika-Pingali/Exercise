import sys
from typing import final
import yaml
from find import find
if len(sys.argv) > 1:
        try:
            file1 = open(sys.argv[1],"r+")
        except:
            print("File not found")
        else:
            lines = file1.readlines()
            #print(lines)
            v = find(lines)
            lines = v.findTags('image:')
            with open('final.yaml', 'w') as f:
                f.writelines(lines)
                #print(yaml.dump_all(final.yaml))
            # findTags('image:', lines)
            file1.close()
else:
        print("Args Missing")
