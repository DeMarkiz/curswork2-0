import tkinter as tk


def show_message(message):
    root = tk.Tk()
    root.title("Message")

    label = tk.Label(root, text=message, padx=20, pady=20)
    label.pack()

    button = tk.Button(root, text="OK", command=root.destroy, padx=20, pady=10)
    button.pack()

    root.mainloop()


# Использование функции
show_message("Hello! This is a message in a separate window.")