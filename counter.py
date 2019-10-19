import re

onePerson = r'(\b(child|girl|sir|Sir|Mr|Ms|Mrs|Major|boy|captain|Captain|Dr.|nurse|haridresser|dad|mom|sister|brother|mother|friend|mum|doctor|professor|niece|nephew|uncles|aunt|kid|son)\b)'
subjectPronouns = r'(\b(she|he|I|you|they|we)\b)'
objectPronouns = r'(\bher|him|me|you|them|us\b)'
possessiveAdjective = r'(\bher|his|my|your|their|our\b)'

matchOnePersonWithPossessiveAdjective = r'(\b(child|girl|boy|captain|Captain|nurse|haridresser|dad|mom|sister|brother|mother|friend|mum|doctor|professor|niece|nephew|uncles|aunt|kid|son).*(\b(her|his|my|your|their|our).(name|keys?|cars?))\b)'
matchVerbersWithObjectPronouns = r'(\b(see|talk|look|listen|help)(.*\bher|his|my|your|their|our)\b)' #if I put walk here I will not get the right result in she walk to her car
matchSubjectProunounsWithPossessiveAdjective = r'(\b(she|he|I|you|they|we).*((her|his|my|your|their|our).(name|keys?|cars?))\b)'
matchPossessiveAdjectiveWithThings = r'(\b(her|his|my|your|their|our).(name|keys?|cars?)\b)'



characterList=[]

with open('testfile.txt') as myFile:

    for i, line in enumerate(myFile):
        charCounter = 0
        if(i < 10):

            findOnePerson = re.findall(onePerson,line)
            findSubjectpronouns = re.findall(subjectPronouns,line)
            findObjectPronouns = re.findall(objectPronouns,line)
            findPossessiveAdjective = re.findall(possessiveAdjective,line)
            findMatchOnePersonWithPossessiveAdjective = re.findall(matchOnePersonWithPossessiveAdjective,line)
            findMatchVerbersWithObjectPronouns = re.findall(matchVerbersWithObjectPronouns,line)
            findMatchSubjectProunounsWithPossessiveAdjective= re.findall(matchSubjectProunounsWithPossessiveAdjective,line)
            findMatchPossessiveAdjectiveWithThings = re.findall(matchPossessiveAdjectiveWithThings,line)

            if findOnePerson and not findSubjectpronouns and not findObjectPronouns and not findPossessiveAdjective:
                characterList.append(line)
                charCounter += len(findOnePerson)
            elif findPossessiveAdjective  and not findOnePerson and not findSubjectpronouns and not findObjectPronouns:
                if findPossessiveAdjective == 'her':
                    if(len(findMatchPossessiveAdjectiveWithThings) >= 1 and len(findMatchVerbersWithObjectPronouns) == 0):
                        characterList.append(line)
                        charCounter += 1
                    elif(len(findMatchPossessiveAdjectiveWithThings) == 0 and len(findMatchVerbersWithObjectPronouns) >=1):
                        haracterList.append(line)
                        charCounter += 2
                    elif(len(findMatchPossessiveAdjectiveWithThings) >= 1 and len(findMatchVerbersWithObjectPronouns) >=1):
                        haracterList.append(line)
                        charCounter += 2
                if findPossessiveAdjective == '(his|my|your)':
                    if(len(findMatchPossessiveAdjectiveWithThings) >= 1):
                        characterList.append(line)
                        charCounter += 1
                    else:
                        haracterList.append(line)
                        charCounter += len(findMatchPossessiveAdjectiveWithThings)

                #I'm not sure about the perfect number to put.
                #if findPossessiveAdjective == '(their|our)'
                #    if(len(findMatchPossessiveAdjectiveWithThings) >= 1):
                #        characterList.append(line)
                #        charCounter += 1
                #    else:
                #        haracterList.append(line)
                #        charCounter += len(findMatchPossessiveAdjectiveWithThings)

            elif findOnePerson and findPossessiveAdjective and not findSubjectpronouns and not findObjectPronouns:
                if( findPossessiveAdjective == (her|his|my|your) and len(findMatchOnePersonWithPossessiveAdjective) == 0):
                    characterList.append(line)
                    charCounter += len(findOnePerson) + 1
                else:
                    characterList.append(line)
                    charCounter += 1

                #I'm not sure about the perfect number to put.
                #if( findPossessiveAdjective == (their|our) and len(findMatchOnePersonWithPossessiveAdjective) == 0):
                #    characterList.append(line)
                #    charCounter += len(findOnePerson) + 1
                #else:
                #    characterList.append(line)
                #    charCounter += 1

            elif findSubjectpronouns and not findOnePerson and not findPossessiveAdjective and not findObjectPronouns:
                if(findPossessiveAdjective == (she|he|I|you)):
                    characterList.append(line)
                    charCounter += 1
                #I'm not sure about the perfect number to put.
                #else:
                #    characterList.append(line)
                #    charCounter += 1
            elif findSubjectpronouns  and findPossessiveAdjective and not findObjectPronouns and not findOnePerson:
                if(findPossessiveAdjective =='her'):
                    if (len(matchVerbersWithObjectPronouns) >= 1):
                        characterList.append(line)
                        charCounter += 2
                    elif (len(findMatchSubjectProunounsWithPossessiveAdjective) == 0):
                        characterList.append(line)
                        charCounter += len(findPossessiveAdjective) + 1
                    elif (len(findMatchSubjectProunounsWithPossessiveAdjective) == 1):
                        characterList.append(line)
                        charCounter += 1
                elif(findPossessiveAdjective =='(his|my|your)'):
                    if (len(findMatchSubjectProunounsWithPossessiveAdjective) == 0):
                        characterList.append(line)
                        charCounter += len(findPossessiveAdjective) + 1
                    elif (len(findMatchSubjectProunounsWithPossessiveAdjective) == 1):
                        characterList.append(line)
                        charCounter += 1
                #I'm not sure about the perfect number to put.
                #elif(findPossessiveAdjective =='(our|their)'):
                #    if (len(findMatchSubjectProunounsWithPossessiveAdjective) == 0):
                #        characterList.append(line)
                #        charCounter += len(findPossessiveAdjective) + 1
                #    elif (len(findMatchSubjectProunounsWithPossessiveAdjective) == 1):
                #        characterList.append(line)
                #        charCounter += 1



            if(charCounter != 0):
                print(charCounter)

with open('result2.txt', 'w+') as wFile:
    wFile.writelines('\n'.join(characterList))
