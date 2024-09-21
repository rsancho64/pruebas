#! /usr/bin/python3
# basic REPL shell

if __name__ == "__main__" :

    while True:                # L-OOP

        # prompt = "??> "
        # print(eval(input(prompt)))  # packed

        prompt = "v0> "
        cmd = input(prompt)     # R-EAD

        # https://www.tutorialspoint.com/5-simple-ways-to-perform-tokenization-in-python
        # https://dylancastillo.co/posts/nlp-snippets-clean-and-tokenize-text-with-python.html

        cmd = " ".join(cmd.split())     # clean cmd
        tokens = cmd.split(' ')   # pseudotokens !

        print(cmd)             
        print(tokens)

        # oouutt = eval(cmd, {})  # {}: void env.
        # print(oouutt)

        # cmd = eval(cmd)        # E-VAL


