def main():
  message = "s3s2s1s4s1"
  comma_code_len = 4

  code = {}

  for i in range(1, comma_code_len + 1):
    code["s" + str(i)] =  (i-1) * "1" + "0"
  
  code["s" + str(comma_code_len + 1)] = comma_code_len * "1" 

  print(code)

  encoded_message = ""
  while message != "":
    for symbol, word in code.items():
      if message.startswith(symbol):
        encoded_message += word
        message = message[len(symbol):]

  print(encoded_message)

if __name__ == "__main__":
  main()
