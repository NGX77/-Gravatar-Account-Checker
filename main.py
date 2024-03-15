import requests
import colorama
import hashlib

def get_gravatar_info(email):
    hashed_email = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    gravatar_url = f"https://www.gravatar.com/{hashed_email}.json"

    response = requests.get(gravatar_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

target_email = input("Target >> ")

gravatar_info = get_gravatar_info(target_email)

colorama.init(autoreset=True)

if gravatar_info:
    entry = gravatar_info.get("entry", [])[0]

    print(colorama.Fore.LIGHTMAGENTA_EX + "# Made by NG-X (https://twitter.com/ngx_x)")
    print(colorama.Fore.CYAN + f'# Gravatar Information for {target_email}:')

    print(colorama.Fore.GREEN + f'[+] Username: {entry.get("displayName")}')
    print(colorama.Fore.GREEN + f'[+] Profile URL: {entry.get("profileUrl")}')

    if entry.get("aboutMe") is None:
        print(colorama.Fore.YELLOW + "[!] No About Me Found")
    else:
        print(colorama.Fore.GREEN + f'[+] About Me: {entry.get("aboutMe")}')

    if entry.get("currentLocation") is None:
        print(colorama.Fore.YELLOW + "[!] No Current Location Found")
    else:
        print(colorama.Fore.GREEN + f'[+] Location: {entry.get("currentLocation")}')

    if entry.get("createdAt") is None:
        print(colorama.Fore.YELLOW + "[!] No Created At Found")
    else:
        print(colorama.Fore.GREEN + f'[+] Created At: {entry.get("createdAt")}')
else:
    print("Error")
