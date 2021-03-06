from tkinter import *

window = Tk()
window.title("CL Scribe")
window.minsize(width=700, height=500)
window.attributes("-alpha", 0.95)
window.config(pady=20)

# TITLE
title_label = Label(text="Cover Letter Scribe", relief="raised")
title_label.grid(column=0, row=0)

# PROMPTS
file_name = Label(text="What name would you like to save this file under?")
file_name.grid(column=0, row=1)

greeting = Label(text="Please provide a warm greeting to begin. (Dear...)")
greeting.grid(column=0, row=2)

opening = Label(
    text="Write an opening statement to introduce yourself.\nThis should reference the company and position"
         " being applied for", justify="left")
opening.grid(column=0, row=3)

qualifications = Label(
    text="Now, list your professional qualifications for the position.\nWhat makes you the ideal "
         "candidate?", justify="left")
qualifications.grid(column=0, row=4)

hobbies = Label(
    text="What other things would you like the company to know?\nOther resources, hobbies, anything else "
         "that would make you a better candidate...")
hobbies.grid(column=0, row=5)

conclusion = Label(text="Add a conclusion paragraph hitting all the main points again.\nInclude a few forms of "
                        "contact information and express a desire to speak in person")
conclusion.grid(column=0, row=6)

goodbye = Label(text="End the letter with a goodbye (Sincerely, etc.)\nStretch over two lines!")
goodbye.grid(column=0, row=7)

# USER TEXT
user_file_name = Text(bg="black", fg="white", width=50, height=1)
user_file_name.grid(column=1, row=1)

greeting_text = Text(bg="black", fg="white", width=50, height=1, wrap="word")
greeting_text.grid(column=1, row=2)

opening_text = Text(bg="black", fg="white", width=50, height=3, wrap="word")
opening_text.grid(column=1, row=3)

qualifications_text = Text(bg="black", fg="white", width=50, height=8, wrap="word")
qualifications_text.grid(column=1, row=4)

hobbies_text = Text(bg="black", fg="white", width=50, height=8, wrap="word")
hobbies_text.grid(column=1, row=5)

conclusion_text = Text(bg="black", fg="white", width=50, height=4, wrap="word")
conclusion_text.grid(column=1, row=6)

goodbye_text = Text(bg="black", fg="white", width=50, height=2)
goodbye_text.grid(column=1, row=7)
