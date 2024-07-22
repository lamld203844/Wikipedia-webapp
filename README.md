# Wiki

Design a Wikipedia-like online encyclopedia.

## Introduction

[Wikipedia](https://www.wikipedia.org/) is a free online encyclopedia that consists of a number of encyclopedia entries on various topics.

Each encyclopedia entry can be viewed by visiting that entry’s page. Visiting https://en.wikipedia.org/wiki/HTML, for example, shows the Wikipedia entry for HTML. Notice that the name of the requested page (HTML) is specified in the route `/wiki/HTML`. Recognize too, that the page’s content must just be HTML that your browser renders.

It can be helpful to store encyclopedia entries using a lighter-weight human-friendly markup language. Wikipedia happens to use a markup language called [Wikitext](https://en.wikipedia.org/wiki/Help:Wikitext), but for this project I’ll store encyclopedia entries using a markup language called [Markdown](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).

By having one Markdown file represent each encyclopedia entry, we can make our entries more human-friendly to write and edit. When a user views our encyclopedia entry, though, we’ll need to convert that Markdown into HTML before displaying it to the user.

## Functionalities

- **Entry Page**: Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry
    - If an entry is exist → render a page that displays the contents of that encyclopedia entry. The title of the page include the name of the entry.
    - If an entry is requested that does not exist, browser present with an error page indicating that their requested page was not found. User can login to create this page. Try login with username = `admin` , password = `123456`
- **Index Page**: In `index.html` you not only see the listing names of all pages in the encyclopedia but can click on any entry name also to be taken directly to that entry page.
- **Search**: You can type a query into the search box in the sidebar to search for an encyclopedia entry. Support suggestions/autocomplete.
    - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
    - If the query does not match the name of an encyclopedia entry, you instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were `ytho`, then `Python` should appear in the search results.
    - Clicking on any of the entry names on the search results page take you to that entry’s page.
- **Random Page**: Clicking “Random Page” in the sidebar will take you to a random encyclopedia entry.

**Admin mode:** some feature only can be access via log in ****

- **New Page**: Clicking “Create New Page” in the sidebar take you to a page where they can create a new encyclopedia entry.
    - You be able to enter a title for the page and, in a `[textarea]`, be able to enter the Markdown content for the page.
    - You be able to click a button to save their new page.
    - When the page is saved,
        - if an encyclopedia entry already exists with the provided title, the you will be presented with an error message.
        - Otherwise, the encyclopedia entry should be saved to disk, and you will be taken to the new entry’s page.
- **Edit Page**: On each entry page, you able to click a link to be taken to a page where you can edit that entry’s Markdown content in a `textarea`.
    - The `textarea` should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial `value` of the `textarea`).
    - You be able to click a button to save the changes made to the entry.
    - Once the entry is saved, you will be redirected back to that entry’s page.

## Installation

- Install dependencies
    
    ```python
    pip install -r requirements.txt 
    ```
    

## Usage

```python
python manage.py runserver
```

- Try admin mode with username `admin` and password `123456`

## Demo

// in progress