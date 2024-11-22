def main():
  encoded_message = "11011111011100"
  comma_code_len = 4

  code = {}

  for i in range(1, comma_code_len + 1):
    code[(i-1) * "1" + "0"] = "s" + str(i)
  
  code[comma_code_len * "1"] = "s" + str(comma_code_len + 1)

  print(code)

  decoded_message = ""
  while encoded_message != "":
    for word, symbol in code.items():
      if encoded_message.startswith(word):
        decoded_message += symbol
        encoded_message = encoded_message[len(word):]

  print(decoded_message)

if __name__ == "__main__":
  main()
