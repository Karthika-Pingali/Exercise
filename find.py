
class find:
    def __init__(self, lines):
         self.index = 0
         self.lines = lines
    
    def findTags(self, tag):
        while self.index < len(self.lines):
            
            if "image:" in self.lines[self.index]:
                #print(self.lines[self.index],end="")
                fSpace = self.frontspace(self.lines[self.index])
                #print(line.find("image:"))
                if self.isImageTagLink():
                    self.nexttag(fSpace)
            self.index+=1
        return self.lines
    def isImageTagLink(self):
        return True
    def frontspace(self, n):
        return len(n) - len(n.strip())
    def nexttag(self, fSpace):
        self.index += 1
        line = self.lines[self.index]
        while self.frontspace(line) > fSpace:
            self.index+=1
            line = self.lines[self.index]
            #print(line)
        self.match()
    # Matching the next tag and if it has imagePullPolicy then get the value of it
    def match(self):
        line = self.lines[self.index]
        tag="imagePullPolicy:"
        if tag in line:
            if line.strip() == tag:
                self.Case1()
            else:
                print("No Changes")
                self.Case3()
                print(line, end="",)
        else:
            print(False)
            self.Case2()
    # case 1
    #   if imagePullPolicy has someother child tag del it and put  ifNotPresent
    def Case1(self):
        fSp = self.frontspace(self.lines[self.index])
        #  IfNotPresent
        self.lines[self.index] = self.lines[self.index][0:len(self.lines[self.index])-1] + " IfNotPresent\n"
        self.index+=1
        line = self.lines[self.index]
        # print(line)
        while fSp < self.frontspace(line):
            print(line, end="")
            # i+=1
            # line = self.lines[i]
            self.lines.pop(self.index)
            line = self.lines[self.index]
            # self.totalLen -= 1
    # case 2
    #   if imagePullPolicy not present
    def Case2(self):
        offset = self.frontspace(self.lines[self.index-1])
        val = ' '*offset + "imagePullPolicy: IfNotPresent\n"
        self.lines.insert(self.index, val)
    # case 3
    # if imagePullPolicy does not have IfNotPresent
    def Case3(self):
        line = self.lines[self.index]
        if "IfNotPresent" not in line:
            self.lines.pop(self.index)
            self.insertTagCase2()
    