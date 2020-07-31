sentence = input() 
i = 0
while True:
  print(i)
  if (sentence[i+1].isupper() == True) and (sentence[i] == ' '):
    sentence = sentence[:i] +  ". " +  sentence[i+1:]
    i += 1
  
  i += 1
  if i >= (len(sentence)):
    break
print(sentence + ".") 
    
