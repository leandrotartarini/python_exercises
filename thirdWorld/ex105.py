def notes(* n, sit=False):
  r = {}
  r['total'] = len(n)
  r['maior'] = max(n)
  r['menor'] = min(n)
  r['media'] = sum(n) / len(n)
  if sit:
    if r['media'] >= 7:
      r['situacao'] = 'NICE'
    elif r['media'] >= 5:
      r['situacao'] = 'OK'
    else:
      r['situacao'] = 'BAD'
  return r

resp = notes(5.5, 9.5, 9.5, sit=True)
print(resp)