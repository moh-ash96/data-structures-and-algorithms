from code_challenges.left_join.hashtable import Hashtable

def left_join(left_hash, right_hash):
  output = []
  for key in left_hash.keys:
    output.append([key, left_hash.get(key), right_hash.get(key)])

  return output
