import re


#One Female in a line
#names
#names = r'(([a-z]+|.)[A-Z]([a-z]+|\.))'
onePerson = r'(\b(child|girl|sir|Sir|Mr|Ms|Mrs|Major|boy|captain|Captain|Dr.|nurse|haridresser|dad|mom|sister|brother|mother|friend|mum|doctor|professor|niece|nephew|uncles|aunt|kid|son)\b)'


oneFemalePronouns = r'\b(she\b)'
oneFemalePossessiveAdjective = r'(\bher\b)'

matchOnePersonWithThings = r'(\b(child|girl|boy|captain|Captain|nurse|haridresser|dad|mom|sister|brother|mother|friend|mum|doctor|professor|niece|nephew|uncles|aunt|kid|son).*(\bher.(name|keys?|cars?))\b)'
matchWithVerbers = r'(\b(see|talk|look|listen|help)(.*\bher)\b)' #if I put walk here I will not get the right result in she walk to her car
matchHerWithThings = r'(\bshe(.*(\b(her.(name|keys?|cars?|back|neck|time|arms|animal|parents|dances|birthday|own))))\b)'

#male
oneMalePronouns = r'(\bhe\b)'
oneMalePossessiveAdjective = r'(\b(his|him)\b)'

matchOneMaleWithThings = r'(\b(child|girl|boy|captain|Captain|nurse|haridresser|dad|mom|sister|brother|mother|friend|mum|doctor|professor|niece|nephew|uncles|aunt|kid|son).*(\bhis\b.(name|keys?|cars?))\b)'
matchMaleWithVerbers = r'(\b(see|talk|look|listen|help).*him\b)'
matchHisWithThings = r'(\bhe(.*(\b(his.(name|keys?|cars?))))\b)'

#more than one
two_persons=r'(\b(she.*her|he.*his|I.*my)\W+(friend|mother|brother|sister|father|mom|dad|mum|cusin|nephew|niece|uncle|aunt|child|kid|son|daughter|girl|boy|boyfriend|bf|girlfriend|gf|best.friend)\b)'

three_persons01=r'(\b(she.*her|he.*his|I.*my)\W+(two)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
three_persons02=r'(\b(she.*|he.*|I)\W+(two.*of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'


four_persons=r'(\b(she.*her|he.*his|I.*my)\W+(three)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
four_persons02=r'(\b(she.*|he.*|I)\W+(three\W+of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'

five_persons=r'(\b(she.*her|he.*his|I.*my)\W+(four)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
five_persons02=r'(\b(she.*|he.*|I)\W+(four\W+of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'

six_persons=r'(\b(she.*her|he.*his|I.*my)\W+(five)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
six_persons02=r'(\b(she.*|he.*|I)\W+(five\W+of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'

seven_persons=r'(\b(she.*her|he.*his|I.*my)\W+(six)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
seven_persons02=r'(\b(she.*|he.*|I)\W+(six\W+of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'

eight_persons=r'(\b(she.*her|he.*his|I.*my)\W+(seven)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
eight_persons02=r'(\b(she.*|he.*|I)\W+(seven\W+of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'

nine_persons=r'(\b(she.*her|he.*his|I.*my)\W+(eight)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
nine_persons02=r'(\b(she.*|he.*|I)\W+(eight\W+of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'

ten_persons=r'(\b(she.*her|he.*his|I.*my)\W+(nine)(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'
ten_persons02=r'(\b(she.*|he.*|I)\W+(nine\W+of)\W+(her|his|my)\W+(friends|brothers|sisters|cusins|nephews|nieces|uncles|aunts|childs|kids|sons|daughters|girls|boys|boyfriend|bf|girlfriends|gfs|best.friends)\b)'




characterList=[]

with open('output.txt') as myFile:

    for i, line in enumerate(myFile):
        charCounter = 0
        if(i < 10000):
            #findNames = re.findall(names,line)
            findOnePerson = re.findall(onePerson,line)
            findOneFemalePronouns = re.findall(oneFemalePronouns,line)
            findOneFemalePossessiveAdjective = re.findall(oneFemalePossessiveAdjective,line)
            findMatchOnePersonWithThings = re.findall(matchOnePersonWithThings,line)
            findMatchHerWithThings = re.findall(matchHerWithThings,line)
            findMatchWithVerbers = re.findall(matchWithVerbers,line)

            #Count 1 to each name
            #if findNames and not findOnePerson and not findOneFemalePronouns and not findOneFemalePossessiveAdjective:
                #characterList.append(line)
                #charCounter += len(findNames)
            #One famele
            if findOnePerson and not findOneFemalePronouns and not findOneFemalePossessiveAdjective:
                characterList.append(line)
                charCounter += len(findOnePerson)
            elif findOneFemalePossessiveAdjective  and not findOnePerson and not findOneFemalePronouns:
                if(len(findMatchHerWithThings) >= 1):
                    characterList.append(line)
                    charCounter += 1
                else:
                    characterList.append(line)
                    charCounter += len(findOneFemalePossessiveAdjective)
            elif findOneFemalePossessiveAdjective  and findOnePerson and not findOneFemalePronouns:
                if(len(matchOnePersonWithThings) == 0):
                    characterList.append(line)
                    charCounter += len(findOnePerson) + 1
                else:
                    characterList.append(line)
                    charCounter += 1

            elif findOneFemalePronouns and not findOnePerson and not findOneFemalePossessiveAdjective:
                characterList.append(line)
                charCounter += 1
            elif findOneFemalePossessiveAdjective and findOneFemalePronouns and not findOnePerson:
                if (len(findMatchWithVerbers) >= 1):
                    characterList.append(line)
                    charCounter += 2
                elif (len(findMatchHerWithThings) == 0):
                    characterList.append(line)
                    charCounter += len(findOneFemalePossessiveAdjective) + 1
                else:
                    characterList.append(line)
                    charCounter += 1

#One Male
            findOneMalePronouns = re.findall(oneMalePronouns,line)
            findOneMalePossessiveAdjective = re.findall(oneMalePossessiveAdjective,line)
            findMatchOneMaleWithThings = re.findall(matchOneMaleWithThings,line)
            findMatchHisWithThings = re.findall(matchHisWithThings,line)
            findMatchMaleWithVerbers = re.findall(matchMaleWithVerbers,line)



            if findOneMalePossessiveAdjective  and not findOnePerson and not findOneMalePronouns:
                if(len(findMatchHisWithThings) >= 1):
                    characterList.append(line)
                    charCounter += 1
                else:
                    characterList.append(line)
                    charCounter += len(findOneMalePossessiveAdjective)
            elif findOneMalePossessiveAdjective  and findOnePerson and not findOneMalePronouns:
                if(len(findMatchOneMaleWithThings) == 0):
                    characterList.append(line)
                    charCounter += len(findOnePerson) + 1
                else:
                    characterList.append(line)
                    charCounter += 1

            elif findOneMalePronouns and not findOnePerson and not findOneMalePossessiveAdjective:
                characterList.append(line)
                charCounter += 1
            elif findOneMalePossessiveAdjective and findOneMalePronouns and not findOnePerson:
                if (len(findMatchMaleWithVerbers) >= 1):
                    characterList.append(line)
                    charCounter += 2
                elif (len(findMatchHisWithThings) == 0):
                    characterList.append(line)
                    charCounter += len(findOneMalePossessiveAdjective) + 1
                else:
                    characterList.append(line)
                    charCounter += 1

#more than onePerson
            findTwoPersons = re.findall(two_persons,line)
            findThreePersons01 = re.findall(three_persons01,line)
            findThreePersons02 = re.findall(three_persons02,line)
            findFourPersons = re.findall(four_persons,line)
            findFourPersons02 = re.findall(four_persons02,line)
            findFivePersons = re.findall(five_persons,line)
            findFivePersons02 = re.findall(five_persons02,line)
            findSixPersons = re.findall(six_persons,line)
            findSixPersons02 = re.findall(six_persons02,line)
            findSevenPersons = re.findall(seven_persons,line)
            findSevenPersons02 = re.findall(seven_persons02,line)
            findEightPersons = re.findall(eight_persons,line)
            findEightPersons02 = re.findall(eight_persons02,line)
            findNinePersons = re.findall(nine_persons,line)
            findNinePersons02 = re.findall(nine_persons02,line)
            findTenPersons = re.findall(ten_persons,line)
            findTenPersons02 = re.findall(ten_persons02,line)

            if findTwoPersons:
                characterList.append(line)
                charCounter += 2
            if(findThreePersons01 or findThreePersons02):
                characterList.append(line)
                charCounter += 3
            if(findFourPersons or findFourPersons02):
                characterList.append(line)
                charCounter += 4
            if(findFivePersons or findFivePersons02):
                characterList.append(line)
                charCounter += 5
            if(findSixPersons or findSixPersons02):
                characterList.append(line)
                charCounter += 6
            if(findSevenPersons or findSevenPersons02):
                characterList.append(line)
                charCounter += 7
            if(findEightPersons or findEightPersons02):
                characterList.append(line)
                charCounter += 8
            if(findNinePersons or findNinePersons02):
                characterList.append(line)
                charCounter += 9
            if(findTenPersons or findTenPersons02):
                characterList.append(line)
                charCounter += 10


            if(charCounter != 0):
                print(charCounter)

with open('result2.txt', 'w+') as wFile:
    wFile.writelines('\n'.join(characterList))
