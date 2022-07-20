#problema kyu 6 do codewars

def meeting():
  s = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
  
  b = list([a.strip().replace(';', ',') for a in el.split(':')] for el in s.split(';'))
    
  c = ''.join(sorted('({}, {})'.format(i[1].upper(), i[0].upper()) for i in b))
    
  return c
  
  
  print(c)
            
meeting()