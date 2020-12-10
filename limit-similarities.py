# Time complexity for both solutions: O(n), where `n` the the length of `input_str`.

# First Solution (using nested loop)
def limit_consecutive_characters(input_str, max_consec_chars):
  if type(input_str) != str:
    return input_str

  result = ''
  
  for char in input_str: # O(n)
    for i in range(max_consec_chars): # O(1)
      if len(result) < i + 1 or result[-1 - i] != char:
        result += char
        break

  return result

# Second Solution (not using nested loop)
def limit_consecutive_characters_2(input_str, max_consec_chars):
  if type(input_str) != str:
    return input_str
    
  result = ''
  last_consecutive_character = None
  consecutive_characters_counter = 0

  for char in input_str: # O(n)
    if char != last_consecutive_character:
      result += char
      last_consecutive_character = char
      consecutive_characters_counter = 1
    elif char == last_consecutive_character and consecutive_characters_counter < max_consec_chars:
      result += char
      consecutive_characters_counter += 1

  return result

if __name__ == '__main__':
  # first solution's test
  print(limit_consecutive_characters('', 3)) # should output: empty string
  print(limit_consecutive_characters('aaab', 2)) # should output: aab
  print(limit_consecutive_characters('aabb', 1)) # should output: ab
  print(limit_consecutive_characters('aabbaa', 1)) # should output: aba
  print(limit_consecutive_characters(None, 1)) # should output: None
  print(limit_consecutive_characters(334, 1)) # should output: 334

  # second solution's test
  print(limit_consecutive_characters_2('', 3)) # should output: empty string
  print(limit_consecutive_characters_2('aaab', 2)) # should output: aab
  print(limit_consecutive_characters_2('aabb', 1)) # should output: ab
  print(limit_consecutive_characters_2('aabbaa', 1)) # should output: aba