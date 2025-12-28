numWrong = "Number is wrong, "
numAlphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def maxNumb():
  while True:
    print(f'print the "max number" (Base - 1) (a natural number greater than 0(max 61))')
    userInputBase = input()
    userInputBase = userInputBase.replace(' ', '')
    if not userInputBase.isdigit():
      print(numWrong, end=' ')  # end = " " replaces enter with a space
      continue
    userInputBase = int(userInputBase)
    if userInputBase < 1 or userInputBase > 61:
      print(numWrong, end=' ')
      continue
    else:
      maxNum = userInputBase
      return maxNum
  
def numberToBase10(maxNum):
  while True:
    result = 0
    base = maxNum + 1
    print(f"print the number you want to decode from the base-{base} system to the base-10 system.")
    userInputNum = input()
    userInputNum = userInputNum.strip().replace(' ', '').replace(',', '.')
    allowedNum = numAlphabet[:base]
    negative = userInputNum.startswith('-')  
    if negative:
      userNum = userInputNum[1:]
    else:
      userNum = userInputNum
  
    if '.' in userNum:
      beforComma, afterComma = userNum.split('.')
    else:
      beforComma, afterComma = userNum, ''
    tChar = True
    for char in beforComma + afterComma:
      if char not in allowedNum:
        print(f"{numWrong}char: '{char}' is not in base-{base}, pls", end=' ')
        tChar = False
        break
    if not tChar:
      continue
    longBeforComma = len(beforComma) - 1   
    for i, char in enumerate(beforComma):
      intNum = numAlphabet.index(char)
      position = longBeforComma - i
      result += intNum*(base**position)    
    for i, char in enumerate(afterComma):
      intNum = numAlphabet.index(char)
      position = -(i + 1)
      result += intNum*(base**position)
    if negative:
      result *= -1 
    return result
def main():
  print("numbers after 9 are replaced with English letters: 10-35 => a-z; 36-61 => A-Z")
  maxNum = maxNumb()
  result = numberToBase10(maxNum)
  print(result)
if __name__ == "__main__":
  main()
        
  
    
