# Portfolio terminal
print('-'*50)
print("Welcome to Yashank's Terminal\nCopyright (c) 2026 Yashank. All rights reserved.")
print("type help or about for more info !")

prefix = 'ysx'

soc = {
    'instagram':'link',
    'github':'link',
    'linkedin':'link',
    'reddit':'link'
}

projects = {
    "portfolio terminal": {
        "desc":" The one you are visiting",
        "status": "live",
        "demo":"link"
    },
}

def getHelp():
    print("Useable commands are (always use 'ysx' as prefix before any command) :\nhelp\nabout\nversion\nexit\nprojects\ninfo project_name\nnew commands soon !!")

def about():
    print("This is a custom terminal made by 'Yashank'.\n type 'help' for more commands.")

def version():
    print("alpha-v1.0")

def socials():
    print("My social account are:")
    for Ac, lnk in soc.items():
        print(f"{Ac}: {lnk}")

def github():
    print("github link - ",soc['github'])

def showProjects():
    print("Avalable projects!")
    for p in projects:
        print(p.capitalize())

def showInfo(pName):
    print(pName)
    for ty, det in projects[pName].items():
        print(f"{ty} : {det}")

commands = {
    'help': getHelp,
    'about': about,
    'ver':version,
    'socials': socials,
    'projects': showProjects,

}

while True:
    print("")
    us = input("$ ").lower()
    if us.startswith(prefix):
        cmd = us[4:]
        if cmd.startswith('info'):
            project_name = cmd[4:].strip()
            if project_name in projects:
                showInfo(project_name)
            else:
                print("Invalid project name!")
        elif cmd in commands:
            commands[cmd]()
        elif cmd == 'exit':
            exit()
        else:
            print(f"Unknown command : {cmd}")
    elif us == 'exit':
        exit()
    else:
        print("Use 'ysx' prefix before any command !!")