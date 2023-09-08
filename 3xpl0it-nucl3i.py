import sys
import os
import subprocess
import shlex
import fileinput

def main():
    if len(sys.argv) == 2:
        keyword = sys.argv[1].lower()
    else:
        # Verifique se há entrada via pipe
        try:
            input_text = sys.stdin.read().strip().lower()
            if input_text:
                keyword = input_text
            else:
                print("Nenhum argumento ou entrada via pipe fornecido.")
                return
        except KeyboardInterrupt:
            print("Nenhum argumento ou entrada via pipe fornecido.")
            return

    templates_dir = "../.local/nuclei-templates/"

    print("Resultados da pesquisa nos templates Nuclei:")

    # Crie uma lista de palavras para pesquisa
    grep_keywords = keyword.split()

    cmd = f"grep -rlE --include=*.yaml 'tags:.*("
    
    for kw in grep_keywords:
        if not kw.isdigit():
            cmd += f"\\b{shlex.quote(kw)}\\b|"
    
    cmd = cmd[:-1]  # Remova o último caractere "|" extra

    cmd += f")' {templates_dir}"
    
    output = subprocess.run(cmd, shell=True, text=True, capture_output=True)

    if output.returncode == 0:
        for line in output.stdout.splitlines():
            print(line)
    else:
        print("Nenhum resultado encontrado.")

if __name__ == "__main__":
    main()
