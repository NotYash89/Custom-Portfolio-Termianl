import tkinter as tk

PROMPT = "ysx:~$ "

app = tk.Tk()
app.title("YSX Terminal")
app.geometry("1000x700")
app.configure(bg="black")

terminal = tk.Text(app,bg="black",fg="white",insertbackground="white",font=("JetBrains Mono", 15),relief="flat",wrap="word")
terminal.pack(fill="both", expand=True,padx=15,pady=15)
terminal.insert("end","Welcome to Yashank's Terminal\n""Copyright (c) 2026 Yashank. All rights reserved.\nType 'help' to get started.\n\n")
terminal.insert("end", PROMPT)

commands = {
    "help": "Available commands:\nhelp\nabout\nversion\nsocials\nclear\nMore commands soon!",
    "about": "This is a custom terminal portfolio made by Yashank.",
    "version": "alpha-v1.0",
    "socials": """Instagram : link
Github    : link
LinkedIn  : link
Reddit    : link"""
}


def get_current_command():
    line = terminal.get("insert linestart", "insert lineend")
    return line.replace(PROMPT, "").strip()


def execute_command(event=None):
    command = get_current_command().lower()

    terminal.insert("end", "\n")

    if command == "clear":
        terminal.delete("5.0", "end")

    elif command in commands:
        terminal.insert("end", commands[command] + "\n")

    elif command:
        terminal.insert("end", f"Unknown command: {command}\n")

    terminal.insert("end", "\n" + PROMPT)
    terminal.see("end")

    return "break"



def protect_prompt(event):
    current_line = terminal.get("insert linestart", "insert lineend")

    if not current_line.startswith(PROMPT):
        terminal.mark_set("insert", "end-1c")

    return None


terminal.bind("<Return>", execute_command)
terminal.bind("<Key>", protect_prompt)

terminal.focus()

app.mainloop()