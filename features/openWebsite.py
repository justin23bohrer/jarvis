import webbrowser

def open_website(site: str):
    site = site.replace(" dot ", ".").replace("dot", ".").replace(" ", "")
    if not site.startswith("http"):
        site = "https://" + site
    webbrowser.open(site)
    return site