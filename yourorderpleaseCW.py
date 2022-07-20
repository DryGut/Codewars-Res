sentence = 'is2 thi1s a3 Test4'
def order():
  ws = []
  for i in range(1, 10):
    for w in sentence.split():
      if str(i) in w:
        ws.append(w)
  return ' '.join(ws)
    

print(order())