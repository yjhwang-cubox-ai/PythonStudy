try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary['aaaa'])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("somthing")
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")