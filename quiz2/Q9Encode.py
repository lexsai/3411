def main():
  message = "aacabacaabbacab"
  
  dict = [(0, "", "")]

  while message != "":
    max_index = 0
    for index, (source_index, add_char, word) in enumerate(dict):
      if message.startswith(word) and len(word) > len(dict[max_index][1]):
        max_index = index

    print(max_index)

    if dict[max_index][2] == message:
      break

    x = len(dict[max_index][2])
    dict.append((max_index, message[x], dict[max_index][2] + message[x]))

    message = message[len(dict[max_index][2] + message[x]):]

    print(dict)
    print(message)

  print("!!!!!!!! CHECK 'last dictionary entry' ANSWER FORMAT!!!!!!!")
  print()

if __name__ == "__main__":
  main()
