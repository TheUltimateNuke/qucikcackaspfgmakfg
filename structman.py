import glob
from sys import argv

root_dir: str = argv[0]

def entry_point():
    allCSFiles: [str] = collectCSFiles()
    
    for filename in allCSFiles:
        print("checking for structs in " + filename + "...")
        structIndexes: [int] = checkForKeyword(filename, 'struct')
        
        if len(structIndexes) > 0:
            with open(filename, 'rwt') as struct:
                readLines: [str] = struct.readlines()
                for index in structIndexes: # repeat for all lines a struct keyword is on
                    struct_line: str = readLines[index] # get line the struct keyword is on
                    lineAfterStruct = 0
                    
                    while lineAfterStruct < len(readLines) - index:
                        lineAfterStruct += 1
                        if (readLines[index + lineAfterStruct]):
                            
                    
                

def collectCSFiles() -> [str]:
    allCSFiles: [str] = []
    
    for filename in glob.iglob(root_dir + '**/*.cs', recursive=True):
        allCSFiles.append(filename)
        print("found C# file: " + filename + "!")
    return allCSFiles

def checkForKeyword(path: str, keyword: str) -> [int]:
    keywordLine = []
    with open(path, 'tr') as f:
        lines = f.readlines()
        for row in lines:
            if row.find(keyword) != -1:
                print("found keyword \"" + keyword + "\" at line " + lines.index(row) + " in " + path + '!')
                keywordLine.append(lines.index(row))
    return keywordLine
                

