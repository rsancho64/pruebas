#! /usr/bin/python3

if __name__ == "__main__":

    while True:
        
        ## entrada
        prompt = "??> "
        cmd = input(prompt)
        tok = cmd.split() # : lista de tokens
        print(tok) 

        ## proceso
        if tok[0] == "exit":
            print("bye!")
            exit(0)
        if tok[0] == "help":
            print("ayuda en construccion...")
            continue
        if tok[0] == "date":
            import subprocess
            subprocess.run(["date"])
            continue

        cmd = " ".join(tok)
        print("cmd**: ", cmd)
        val = eval(cmd, {})
        print(val)

        




