from tkinter import *

# FUNCTIONS
def file_namer():
    file = user_file_name.get("1.0", END)
    print(file)


# UI SETUP
window = Tk()
window.title("CLScribe")
window.minsize(width=500, height=300)
window.attributes("-alpha", 0.95)
window.config(pady=20)

# TITLE
title_label = Label(text="Cover Letter Scribe", relief="raised")
title_label.grid(column=0, row=0)

# PROMPTS
file_name = Label(text="What name would you like to save this file under?")
file_name.grid(column=0, row=1)

greeting = Label(text="Please provide a warm greeting to begin.")
greeting.grid(column=0, row=2)

opening = Label(text="Write an opening statement to introduce yourself.\nThis should reference the company and position"
                     " being applied for", justify="left")
opening.grid(column=0, row=3)

qualifications = Label(text="Now, list your qualifications for the position.\nWhat makes you the ideal candidate?",
                       justify="left")
qualifications.grid(column=0, row=4)


# USER TEXT
user_file_name = Text(bg="black", fg="white", width=50, height=1)
user_file_name.grid(column=1, row=1)

greeting_text = Text(bg="black", fg="white", width=50, height=2, wrap="word")
greeting_text.grid(column=1, row=2)

opening_text = Text(bg="black", fg="white", width=50, height=4, wrap="word")
opening_text.grid(column=1, row=3)


# BUTTONS
submit = Button(text="Create Document", command=file_namer)
submit.grid(column=2, row=0)


file_namer()

window.mainloop()

