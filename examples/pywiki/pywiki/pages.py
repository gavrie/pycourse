pages = {
    "Main Page": """This is the main page of our Wiki. It has some nice stuff. See the [Second Page] and [Third Page]! """,
    "Second Page": """The second page. See also the [Main Page].""",
    "Third Page": """The third page.""",
}

def get_page(title):
    return pages.get(title)

def set_page(title, content):
    pages[title] = content
