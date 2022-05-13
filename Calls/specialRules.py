from Calls.gettingCalls import pageCall

#Parameters with special conditions
spInputData = {}
spConditionsList = ['memberLoggedIn', 'emaillaunchid', 'url', 'meredithHashId']
for i in spConditionsList:
    try:
        spInputData[i] = pageCall[0]['properties'][i]
    except:
        spInputData[i] = 'NH'


