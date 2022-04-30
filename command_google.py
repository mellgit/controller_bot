import webbrowser


def search_google(search):
    # ссылка для поиска чего либо
    url = f"https://www.google.com/search?q={search}"
    webbrowser.open(url, new=0, autoraise=True)


def open_link(message):
    
    url = message.text  # ссылка для поиска чего либо

    webbrowser.open(url, new=0, autoraise=True)
