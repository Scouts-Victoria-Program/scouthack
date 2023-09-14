# Friday night

1. Set up laptops
2. Why don't we have internet?
3. Distinction between LAN/Ethernet/Wifi/Internet

# Saturday morning

## Setting up dev environment

1. log into computer. Username and pasword are both `scouthack`
2. Open Visual Studio Code (should be on the Desktop)
3. Click the blue rectangle with two arrows in it at the bottom-left of the screen
4. Select "Connect to Host..." from the menu that appears at the top
5. Type in "username@username.scouthack" and <kbd>Enter</kbd>
6. The first time you connect, you will be told:
   > "username.scouthack" has fingerprint "BIG LONG STRING OF CHARACTERS".
   > Are you sure you want to continue?
7. Select "Continue"
8. Enter your password when propmpted, and press <kbd>Enter</kbd>
9. Click the Explorer (the paper icon in the top-left)
10. Select "Open Folder"
11. In the pop-up that appears, select the `code` folder and select "OK".
12. Enter your password again, if prompted
13. If asked "Do you trust the authors of the files in this folder?", select "Yes, I trust the authors"

## Creating your first web page

1. Create a new file called `index.html`
2. Type "Hello world" in the file, and press <kbd>Ctrl</kbd>+<kbd>S</kbd> to save the file
3. Press <kbd>Ctrl</kbd>+<kbd>\`</kbd>. The <kbd>\`</kbd> is to the left of the <kbd>1</kbd> on the top-left of the keyboard. This will open up a Terminal at the bottom of your editor
4. In the terminal, type `python -m http.server 80` and press <kbd>Enter</kbd>
5. On the Desktop of the computer, or the applications menu at the top-left, open Firefox, and browse to http://username.scouthack
6. You should see your "Hello world" message.

### HTML tags

The various elements that make up HTML are created using tags. A tag looks like `<this>`. That is, it's one or more words, surrounded by angle brackets. These angle brackets are also known as the less-than and greater-than signs.

You can type these on your keyboard by holding <kbd>Shift</kbd>+<kbd>,</kbd> for `<` (less-than), and <kbd>Shift</kbd>+<kbd>.</kbd> for `>` (greater-than).

Most HTML elements require both an start tag, and an end tag. For example, the HTML element has a start tag which looks like `<html>`, and an end tag which looks like `</html>`.

Notice that the end tag includes a <kbd>/</kbd>, which is on your keyboard between the <kbd>.</kbd> and the <kbd>Right Shift</kbd> keys; the same key as the <kbd>?</kbd>.

Some elements, known as "void elements", don't have an end tag or closing tag. We'll see an example of this soon.

### Headings

The first thing we'll do to format our HTML is to add some headings. HTML supports 6 levels of headings. To use these, we surround our heading content in HTML tags `<h1></h1>` through to `<h6></h6>`. If you use another number, such as `<h7></h7>`, it won't do anything interesting.

```html
<h1>This is a heading</h1>
<h2>This is a smaller heading</h2>
<h3>A level 3 heading</h3>
<h4>A level 4 heading</h4>
<h5>A level 5 heading</h5>
<h6>A level 6 heading</h6>
<h7>Not a valid heading</h7>
```

> <h1>This is a heading</h1>
> <h2>This is a smaller heading</h2>
> <h3>A level 3 heading</h3>
> <h4>A level 4 heading</h4>
> <h5>A level 5 heading</h5>
> <h6>A level 6 heading</h6>
> <h7>Not a valid heading</h7>

### Paragraphs

Now let's create a paragraph. Paragraphs are used for the regular text you see in a web page, like this sentence you're reading right now. To make a paragraph, we use the `<p></p>` tags, like this:

```html
<p>
    This is a paragraph.
    It has some text in it.
    The text is spread over multiple lines.
</p>
```

> <p>
>     This is a paragraph.
>     It has some text in it.
>     The text is spread over multiple lines.
> </p>

### Line-breaks

If you look at the above example, you'll see that there are actually 3 lines of text inside the `<p>` element, but it all displays on a single line. This is because in HTML, you need to explicitly tell it if you want to start on a new line. We do this using the `<br>` (break) tag. Earlier, we mentioned that some elements (known as "void elements") don't have a closing tag. The `<br>` tag is one of these, so we write it as `<br>`, and not `<br></br>`. Below is another paragraph, this time with some line-breaks added:

```html
<p>
    To create new lines in HTML,<br> We need to use the &lt;br&gt; (or 'break') tag.<br>
    Lines do not otherwise get split automatically.
</p>
```

> <p>
>     To create new lines in HTML,<br> We need to use the &lt;br&gt; (or 'break') tag.<br>
>     Lines do not otherwise get split automatically.
> </p>

### Text formatting

We can also make text <strong>bold</strong> using `<strong></strong>`, and <em>italicised</em> using `<em></em>`:

```html
<p>
    Here is some text which has <strong>some parts which are bold</strong>, as well as <em>some parts win italics</em>.<br>
    <br>
    If we wanted to get <em>really</em> fancy, we could also <u>underline some text</u>, or <del>put a line through it.</del>
</p>
```

> <p>
>     Here is some text which has <strong>some parts which are bold</strong>, as well as <em>some parts win italics</em>.<br>
>     <br>
>     If we wanted to get <em>really</em> fancy, we could also <u>underline some text</u>, or <del>put a line through it.</del>
> </p>

Note that it's also possible to use `<b></b>` to create <b>bold text</b>, and `<i></i>` to put <i>text in italics</i>, but this is discouraged and usualyl not you want.

### Images

We can also add images to our HTML. This is done using the `<img>` element. Like the `<br>` element, `<img>` is a void element with no closing tag.

To add an image, we need to specify which image file our image is in. Here's how we do that:

```html
<img src="scout_logo.png">
```

And here's what that looks like:

> <img src="scout_logo.png">

### HTML Attributes

We've just done something new. In addition to our `<img>` tag, we've got this `src=` bit. This is called an "attribute". Most HTML tags can have attributes. They are usually of the form `attribute-name="some attribute value"`, though some of them are *just* a name.

For the `<img>` tag, the `src` attribute tells the computer where to find the image we want it to display, by providing the file name. If you take a look at the JupyterLab file browser on the left, you'll see the file for the image we're loading here.

### Links

One of the big benefits of HTML is its ability to create links between web pages. This is done using the HTML anchor tag, written as `<a></a>`. The full format is `<a href="linked_page.html">description goes here</a>`. The `href` attribute specifies the location of the page we want to link to, and the content of the tag (the `description goes here` bit) is what we see on the page and then click on.

Take a look below.

Note that when you click the link, the new page will be opened in a file tab inside JupyterLab, and you'll need to close it or click on this tab again to get back here:

```html
<a href="linked_page.html">description goes here</a>
```

> <a href="linked_page.md">description goes here</a>

Now that we can create links between web pages, and add images to them, we have all the tools we need to make a web site (where a "site" is a collection of "pages") with quite a lot of content. Before we start working on that, though, let's just cover off a few other formatting things that will make our pages a bit easier to read.

### Lists

In HTML, you can create two different types of lists. Ordered lists, and unordered lists. Ordered lists have numbers (or letters) in front of them, and unordered lists just use a bullet point or similar.

To create an ordered list, we use the `<ol></ol>` element (`ol` stands for "ordered list").

To create an *unordered* list, we use the `<ul></ul>` element (for "unordered list").

Then, inside those element tags, we create our "list items", designated by `<li></li>` elements. Here are a couple of examples:

```html
<ol>
    <li>one fish</li>
    <li>two fish</li>
    <li>red fish</li>
    <li>blue fish</li>
</ol>

<ul>
    <li>apples</li>
    <li>bananas</li>
    <li>oranges</li>
    <li>kittens</li>
</ul>
```
And here's how they look:

> <ol>
>     <li>one fish</li>
>     <li>two fish</li>
>     <li>red fish</li>
>     <li>blue fish</li>
> </ol>
>
> <ul>
>     <li>apples</li>
>     <li>bananas</li>
>     <li>oranges</li>
>     <li>kittens</li>
> </ul>

### Tables

The last bit of formatting we're going to look at for now is HTML tables. Besides from the `<table></table>` element, a HTML table can contain:

* A header (`<thead></thead>`)
* Some column headings (`<th></th>`)
* A body (`<tbody></tbody>`)
* Some rows (`<tr></tr>`)
* Some columns, or "divisions" (`<td></td>`)

Here's how a basic HTML table might be written:
```html
<table>
    <thead>
        <tr>
            <th>Heading for column 1</th>
            <th>Heading for column 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1A</td>
            <td>2A</td>
        </tr>
        <tr>
            <td>1B</td>
            <td>2B</td>
        </tr>
    </tbody>
</table>
```
And here's how it turns out:

> <table>
>     <thead>
>         <tr>
>             <th>Heading for column 1</th>
>             <th>Heading for column 2</th>
>         </tr>
>     </thead>
>     <tbody>
>         <tr>
>             <td>1A</td>
>             <td>2A</td>
>         </tr>
>         <tr>
>             <td>1B</td>
>             <td>2B</td>
>         </tr>
>     </tbody>
> </table>

## A complete HTML document

So far, we've been putting HTML tags into a text file, but in its current form, it's not actually valid HTML.

A basic valid HTML document looks like this:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>This is the web page's title</title>
</head>
<body>
    Hello World! This is the web page's content
</body>
</html>
```

You can see that it has some bits at the top that tell the computer it's a HTML file. It also includes a `<head>` element where we add some other information, including a `<title>` element which specifies the title of our web page; this is what appears as the name of your browser's window or tab when the page is open.

All the bits we've written so far would appear inside the `<body>` element, which is where the main part of the web page lives.

Now that we've got the basics of HTML, we'll start working on a complete HTML web page example that will be the basis for the website we're making this weekend.
