import re


mountainMatchingPattren = r'(\bmountains?\b | \bwaterfall\b | \bcliff\b)'
mountainFilteringOutPattren = r'(\b(?!as.*waterfall)\b)'

sandyMatchingPattren = r'(\bbeachs?\b | \bsand\b)'
sandyFilteringOutPattren = r'(\blike(?!.*beach)\b| \b(?!beach.*bum)\b | \b(?!beach.*blanket)\b | Mr.*\<Sandy\> | \b(?!beach.*towel)\b | \b(?!boulder-broken.*beach)\b)'

flatMatchingPattren = r'(\bgrass | streets? | city| cites | towns?\b)'
flatFilteringOutPattren = r'(talk(?!.*town) | \btown(?!hall)\b | \bdark(?!town))'

hillMatchingPattren = r'\b(hill | river)\b'
hillFilteringOutPattren = r'(\bant(?!.*hill)\b)'


mountainList=[]
sandyList=[]
flatList=[]
hillList=[]


numberOfMatchingLines = 0

with open('output.txt') as myFile:
    for i, line in enumerate(myFile):
        if (i < 1000000):


            if(re.findall(mountainMatchingPattren, line)):
                if(re.findall(mountainFilteringOutPattren, line)):
                    mountainList.append(line)
                    numberOfMatchingLines += 1

            if(re.findall(sandyMatchingPattren, line)):
                if(re.findall(sandyFilteringOutPattren, line)):
                    sandyList.append(line)

            if(re.findall(flatMatchingPattren, line)):
                if(re.findall(flatFilteringOutPattren, line)):
                    flatList.append(line)

            if(re.findall(hillMatchingPattren, line)):
                if(re.findall(hillFilteringOutPattren, line)):
                    hillList.append(line)




with open('result.txt', 'w+') as wFile:

    wFile.write('Mountain\n')
    wFile.write('There are ' + str(numberOfMatchingLines) + ' lines' + '\n' )
    wFile.write('\n')
    wFile.writelines('\n'.join(mountainList))
    wFile.write('Sandy\n')
    wFile.writelines('\n'.join(sandyList))
    wFile.write('flat\n')
    wFile.writelines('\n'.join(flatList))
    wFile.write('hill\n')
    wFile.writelines('\n'.join(hillList))
