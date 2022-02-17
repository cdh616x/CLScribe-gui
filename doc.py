from docx import Document
import ui

document = Document()

def file_namer():
    file = ui.user_file_name.get("1.0", ui.END).strip()
    for n in document_components:
        x = str(n.get("1.0", ui.END))
        document.add_paragraph(x)
        document.save("./output/" + file + ".docx")
    # file = ui.user_file_name.get("1.0", ui.END)
    # for n in document_components:
    #     x = str(n.get("1.0", ui.END))
    #     with open("../.././Desktop/" + file + ".doc", "a") as cover_letter:
    #         cover_letter.write(x + "\n")
def restore():
    for n in document_components:
        n.delete("1.0", ui.END)


# BUTTONS
submit = ui.Button(text="Create Document", command=file_namer)
submit.grid(column=1, row=0)

restore = ui.Button(text="Restore", command=restore)
restore.grid(column=1, row=8)

document_components = [ui.greeting_text, ui.opening_text, ui.qualifications_text, ui.hobbies_text, ui.conclusion_text,
                       ui.goodbye_text]

ui.window.mainloop()