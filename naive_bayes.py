
#creating a spam model
#runs once on a training data
def train:
  total = 0
  numSpam = 0
  for email in trainData:
     if email.label == SPAM :
       numSpam +=1
     total += 1
     processEmail(email.body , email.label):
    pA = numSpam/float(total)
    pNotA = (total - numSpam)/float(total)

#reading words from a specific email
  def processEmail(body , label):
    for word in body:
        if label == SPAM
           trainPositive[word] = trainPositive.get(word, 0) + 1
            positiveTotal += 1
        else
          trainNegative[word] = trainNegative.get(word, 0) + 1
            negativeTotal += 1
#gives the conditional probability p(B_i/A_x)
def conditionalEmail(body , spam) :
  result =1.0
  for word in body:
    result *= conditionalWord(body , spam)
  return result

#classifies a new email as spam or not spam
  def classify(email):
      isSpam = pA * conditionalEmail(email, True) # P (A | B)
      notSpam = pNotA * conditionalEmail(email, False) # P(¬A | B)
      return isSpam > notSpam
#Laplace Smoothing for the words not present in the training set
#gives the conditional probability p(B_i | A_x) with smoothing
def conditionalWord(word, spam):
    if spam:
       return (trainPositive.get(word,0)+alpha)/(float)(positiveTotal+alpha*numWords)
    return (trainNegative.get(word,0)+alpha)/(float)(negativeTotal+alpha*numWords)
