import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser

BG = "#F388F1"
button_BG = "#DE20DA"

screen = tk.Tk()
screen.title("Hacker News")
screen.minsize(1200, 800)
screen.configure(bg=BG)


def clean_list(remove):
    remove.pop(0)
    remove.pop()
    remove.pop()
    remove.pop()


def link_click(web_url):
    webbrowser.open_new_tab(web_url)


target_url = "https://news.ycombinator.com/"
found_links = []

response = requests.get(target_url)
soup = BeautifulSoup(response.text, "html.parser")
list_of_links = []
for link in soup.find_all("a"):
    found_link = link.get("href")
    if "https" in found_link:
        if found_link not in found_links:
            found_links.append(found_link)

clean_list(found_links)

main_label = tk.Label(text="Hacker News Links", bg=BG, font=("times new roman", 15, "italic", "bold"))
main_label.pack()

links_count = len(found_links)
links_found_label = tk.Label(text=f"{links_count} links found!", bg=BG,
                             font=("times new roman", 13, "italic", "bold"))
links_found_label.pack()
main_frame = tk.Frame(screen, width=1000, height=800, bg=BG)
main_frame.pack()

cv = tk.Canvas(main_frame, width=1000, height=800, bg=BG)
sub_frame = tk.Frame(cv, bg=BG)

scroll_bar = tk.Scrollbar(main_frame)
scroll_bar["orient"] = tk.VERTICAL
scroll_bar["command"] = cv.yview

cv["yscrollcommand"] = scroll_bar.set

scroll_bar.pack(side="right", fill=tk.Y)
cv.pack(expand=True, fill=tk.BOTH)
cv.create_window((5, 5), window=sub_frame, anchor="nw")

sub_frame.bind(sequence="<Configure>",
               func=lambda event: cv.configure(scrollregion=cv.bbox(tk.ALL)))

for url in found_links:
    buttons = tk.Button(sub_frame, text=url, height=1, width=140, bg=button_BG,
                        font=("times new roman", 10, "italic", "bold"),
                        command=lambda a=url: link_click(a), borderwidth=8)
    buttons.pack(anchor='w', pady=2)

screen.mainloop()
