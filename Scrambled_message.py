#  Write a Python script to loop through the string and extract the keyword. The keyword is known to be surrounded by the symbols *.

Scrambled_message = "a8*Message#w4f"
keyword = ""
# loop throught the scrambled message
for i in range(len(Scrambled_message)):
    # check if the current character is i
    if Scrambled_message[i] == '*':
        # start extracting the keyword
        keyword = "" 
        for j in range(i+1, len(Scrambled_message)):
            if Scrambled_message[j] == '#':
                 print("Break condition met")
                 break
            else:
                keyword += Scrambled_message[j]

        print("Keyword found:", keyword)