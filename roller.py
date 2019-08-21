import re
from random import randint

def parse(text):
  trimSummon = text.replace('\n','').split('!!roll')[1].strip()
  matchResult = re.match(r"(?P<dice>\d{0,2}d\d{0,3}\s?([+-]\s?\d{0,2})?).*", trimSummon)
  parsedSection = matchResult.group('dice')
  [numDie, rest] = [elem.strip() for elem in parsedSection.split('d')]
  if numDie == '':
    numDie = 1 # !!roll d20 should be valid
  if '+' in rest:
    [dieSize,modifier] = [int(elem.strip()) for elem in rest.split('+')]
  elif '-' in rest:
    [dieSize,modifier] = [int(elem.strip()) for elem in rest.split('-')]
    modifier *= -1
  else:
    dieSize = int(rest.strip())
    modifier = 0
  return {
    "numDie": int(numDie),
    "dieSize": dieSize,
    "modifier": modifier
  }

def roll(rollOpts):
  [numDie,dieSize,modifier] = rollOpts['numDie'],rollOpts['dieSize'],rollOpts['modifier']
  rolledDie = [randint(1,dieSize) for elem in range(numDie)]
  total = sum(rolledDie) + modifier
  return({
    "total": total,
    "rolledDie": f"[{','.join(str(v) for v in rolledDie)}]"
  })

def buildResponse(text):
  parsedRoll = parse(text)
  responseContent = f"Rolling {parsedRoll['numDie']} d{parsedRoll['dieSize']}s then adding {parsedRoll['modifier']}...\n\n"
  result = roll(parsedRoll)
  responseContent += f"Rolled: {result['rolledDie']}\nTotal (including modifier):{result['total']}"
  return responseContent

x = buildResponse("blah blah\n !!roll 4d20")
print(x)