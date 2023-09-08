import sys
import os
import requests
import subprocess

def search_module(module_name):
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    search_url = f"{base_url}?keyword={module_name}"

    response = requests.get(search_url)
    data = response.json()

    return data

def search_exploits(query, exploit_source):
    results = []

    if exploit_source == "github":
        query = query.lower()
        search_url = f"https://api.github.com/search/repositories?q={query}+in:title+in:readme"
        response = requests.get(search_url)
        data = response.json()
        results.extend(data.get("items", []))

    return results

def main():
    if len(sys.argv) < 2:
        print()
        print(" _      ___       _  _         ____             _  ___  _ _           _______      ______  ")
        print("| |    / _ \     | || |       |___ \           | |/ _ \(_) |         / ____\ \    / /___ \ ")
        print("| |   | | | | ___| || |_ ______ __) |_  ___ __ | | | | |_| |_ ______| |     \ \  / /  __) |")
        print("| |   | | | |/ __|__   _|______|__ <\ \/ / '_ \| | | | | | __|______| |      \ \/ /  |__ < ")
        print("| |___| |_| | (__   | |        ___) |>  <| |_) | | |_| | | |_       | |____   \  /   ___) |")
        print("|______\___/ \___|  |_|       |____//_/\_\ .__/|_|\___/|_|\__|       \_____|   \/   |____/ ")
        print("                                         | | ")                                              
        print("                                         |_| ")                                            

        print("By Bl4dsc4n - l0c4-3xpl0it-CV3 - v.0.1")
        print()
        print("Ps: Use com sabedoria, qualquer ato ilicito é de sua responsabilidade!!!")
        print()
        print("Uso: python3 script.py <CVE ou Software>")
        print("Exemplo: python3 script.py laravel")
        sys.exit(1)
    print()
    module_name = " ".join(sys.argv[1:]).lower()
    cve_result = search_module(module_name)
    github_query = f"{module_name}+exploit+OR+{module_name}+cve"

    if "result" in cve_result and "CVE_Items" in cve_result["result"]:
        cves = cve_result["result"]["CVE_Items"]

        print("Informações sobre CVEs:")
        for cve in cves:
            cve_id = cve["cve"]["CVE_data_meta"]["ID"]
            description = cve["cve"]["description"]["description_data"][0]["value"]
            published_date = cve["publishedDate"]
            print("CVE ID:", cve_id)
            print("Data de Publicação:", published_date)
            print("Descrição:", description)
            print("-" * 50)

        github_exploit_result = search_exploits(github_query, "github")
        if github_exploit_result:
            print("Links de exploits no GitHub:")
            for item in github_exploit_result:
                print("URL:", item.get("html_url"))
            print("=" * 80)

    processo = subprocess.Popen(['python', '3xpl0it-nucl3i.py'], stdin=subprocess.PIPE)
    processo.communicate(input=module_name.encode())    

if __name__ == "__main__":
    main()
