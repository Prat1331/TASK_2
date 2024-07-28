import tkinter as tk
import pyshorteners 
import pyperclip 

root = tk.Tk()
root.title('GUI URL Shortener')
root.geometry('400x100')

def shorten():
    url = urlValue.get()
    link = pyshorteners.Shortener()
    shortened = link.tinyurl.short(url)
    msg = f'Shortened URL is {shortened}'
    root.destroy()

    def copyURL():
        copyUrl = pyperclip.copy(shortened)
        win.destroy()

    win = tk.Tk()
    win.title('GUI URL Shortener')
    win.geometry('350x70')

    label = tk.Label(win, text=msg, font=('Montserrat', 10)).pack()
    copyURLBtn = tk.Button(win, text='Copy URL', font=('Montserrat', 10), padx=5, pady=10, command=copyURL).pack(
        pady=10)

    print(f'Shortened URL is {shortened}')

Header = tk.Label(root, text="GUI URL SHORTENER BY CODE MONK", font=('Anton', 20), justify=tk.CENTER).pack(side=tk.TOP)
mainframe = tk.Frame(root).pack(side=tk.LEFT, padx=5)
urlValue = tk.StringVar()
urlLabel = tk.Label(mainframe, text="Enter your URL", font=('Montserrat', 10)).pack(side=tk.LEFT, padx=5)
urlEntry = tk.Entry(mainframe, textvariable=urlValue).pack(side=tk.LEFT, padx=5)
shortUrlBtn = tk.Button(mainframe, text='Shorten URL', font=('Montserrat', 10), command=shorten).pack(side=tk.LEFT, padx=20)

root.mainloop()