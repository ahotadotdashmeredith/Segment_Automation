import re
import sys
from urllib.parse import urlparse, parse_qsl


sys.path.insert(1, 'C:\\Users\\ahota\\PycharmProjects\\GA\\Calls')


from Calls.specialRules import spInputData



#Defining variables
url = urlparse(spInputData['url'])
didPresent = True
did = 'NH'
returnObject = {
    'Problem 1' : {
        'did' : '',
        'emaillaunchid' : '',
        'error' : ''
    },
    'Problem 2' : {
        'memberLoggedIn' : '',
        'meredithHashId' : '',
        'error' : ''
    }
}


#Check if did parameter is in the url or not
try:
    did = dict(parse_qsl(url.query))["did"]
except:
    didPresent = False


#Condition 1
if didPresent:
    if did == spInputData['emaillaunchid']:
        returnObject['Problem 1']['did'] = did
        returnObject['Problem 1']['emaillaunchid'] = spInputData['emaillaunchid']
        returnObject['Problem 1']['error'] = 'No Error'
    else:
        returnObject['Problem 1']['did'] = did
        returnObject['Problem 1']['emaillaunchid'] = spInputData['emaillaunchid']
        returnObject['Problem 1']['error'] = 'Error'
else:
    returnObject['Problem 1']['did'] = 'NH'
    if spInputData['emaillaunchid']==None:
        returnObject['Problem 1']['emaillaunchid'] = 'null'
        returnObject['Problem 1']['error'] = 'No Error'
    else:
        returnObject['Problem 1']['emaillaunchid'] = spInputData['emaillaunchid']
        returnObject['Problem 1']['error'] = 'Error'


#Condition 2
returnObject['Problem 2']['memberLoggedIn'] = spInputData['memberLoggedIn']
if spInputData['memberLoggedIn']==True and spInputData['meredithHashId']=='NH':
    returnObject['Problem 2']['meredithHashId'] = "Not Present"
    returnObject['Problem 2']['error'] = "Error"
elif spInputData['memberLoggedIn']==True and re.fullmatch('[a-z0-9]{40}', spInputData['meredithHashId']):
    returnObject['Problem 2']['meredithHashId'] = spInputData['meredithHashId']
    returnObject['Problem 2']['error'] = "Error - Regex Mismatch"
else:
    returnObject['Problem 2']['meredithHashId'] = spInputData['meredithHashId']
    returnObject['Problem 2']['error'] = "No Error"


