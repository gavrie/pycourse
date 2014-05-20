Description
-----------

Create a basic Wiki application using Flask.

The initial functionality is as follows:

- A main page is shown, which can be edited by clicking an 'Edit' link or button
- Each page includes a header with a title and a footer with links or buttons to edit/save/cancel
- Wiki links are implemented by using square brackets syntax, such as `[Main Page]`

Implementation Guidelines
-------------------------

General:

- Pages are stored in memory and are not persistent in the first stage
- Use regular expressions to parse the Wiki syntax
- Write unit tests for parsing pages, and run them using `py.test`. Put all your tests in a `test` directory.

Create a main file named `web.py` that runs your application, and imports further functionality from other modules. Create a package named `wiki` that includes modules for the rest of your application, such as:

    wiki.pages
    wiki.render
    wiki.auth

Use simple string templates to generate your HTML pages by using the string `format` method. For example:

    TEMPLATE_HEADER = """
    <h1>Our Nice Wiki</h1>
    <h2>{title}</h2>
    <hr>
    """

    page = TEMPLATE_HEADER.format(title="Main page")


Advanced Functionality
----------------------

Once your basic Wiki works, start adding functionality according to the list. Other ideas are fine as well.

- Add a table of contents, that shows all existing pages and links to them.
- More Wiki syntax:
    - Itemized lists (bullets, numbering)
    - Headings
    - URL links
    - Text styles (bold, italic)
- Page history - who edited the page and when
- Search the wiki (with regular expressions)
- Add page persistence to files (or to a database with sqlite)
- Export Wiki data to XML
- Use the Flask template engine (jinja2) for your pages instead of string templates
- Authentication - allow editing only with a login and password

# vim:lbr:nolist:wrap
