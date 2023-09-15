![](img/network-diagram-crop.png) <!-- .element style="max-height: 750px" -->

---

![](img/network_hardware.jpg) <!-- .element style="max-height: 750px" -->

---

![](img/switch_ports.jpg) <!-- .element style="max-height: 750px" -->

---

# HTML page overview

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <div id="div_content">
        <section>
            <!--x block header x-->
        </section>
        <section>
            <!--x block content x-->
        </section>
        <section>
            <!--x block footer x-->
        </section>
    </div>
</body>
</html>
```

Notes:

# Create skeleton HTML document

This `index.html` is the base for the website we're going to build.

It starts with the basic HTML tag and the `<head>` tag, which contains
some important information to tell the browser how to display the page.
It also includes a space to put the `<title>` of our page, which will
appear at the top of the web browser window.

The `<body>` tag is where all the action happens. Inside this tag, we
have a `<div>` tag. `<div>` tags are block elements, as opposed to
inline elements. Inline elements flow across a page like text, and can
have line breaks etc., while block elements behave as if they're inside
a box, and everything needs to work around them.

This `<div>` tag will be used as the "container" for our web page. This
is so that later on we can write code to describe how our content should
behave, and apply it to this `<div>`. Note also that the `<div>` has an
ID of "div_content". In a web page, each ID must be unique, meaning that
if we ever need to refer to this `<div>`, we can use the ID
'div_content', and the browser will know what we mean.

Inside 'div_content', we have three `<section>` elements. These sections
are for our "header", "content", and "footer".

---

# HTML page detail

```html [13-19|21-43|45-53|54-60]
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>

<body>
    <div id="div_content">
        <section>
            <!--x block header x-->
            <header>
                <!-- Put your menu links here -->
            </header>
            <!--x endblock header x-->
        </section>

        <section>
            <!--x block content x-->

            <div id="div_first_content">
                <div id="div_patrol_logo">
                    <!-- Put your Patrol logo here! -->
                </div>

                <div id="div_headings_paragaphs">
                    <!-- Heading and Paragraphs -->
                </div>
            </div>
            <div id="div_second_content">
                <div id="div_unordered_list">
                    <!-- Unordered list-->
                </div>
                <div id="div_ordered_list">
                    <!-- Ordered list -->
                </div>
                <div id="div_more_paragraphs">
                    <!-- Paragraph -->
                </div>
            </div>

            <div id="div_third_content">
                <div id="div_table">
                </div>
                <div id="div_program_link">
                </div>
            </div>

            <!--x endblock content x-->
        </section>

        <section>
            <!--x block footer x-->
            <footer>
            </footer>
            <!--x endblock footer x-->
        </section>
    </div>

</body>

</html>
```

Notes:

We've added in some elements that look `<!-- like this -->`. These are
HTML "comment" elements. The browser ignores them, but they are useful
to us to explain what we're doing. Some of the comments we've added look
`<!--x like this x-->`, with `x` characters at either end. These are
just regular comments, except that we've made them look a little
different so we can refer to them later, and we want to ensure we can
distinguish them from the rest of our comments.

Looking at the comments, you can see the bits that make clear where the
"header", "content", and "footer" of our document are.

There are also various other comments in there that are acting as
place-holders for more content we'll be adding later on.

In our content section, we have three separate code blocks:
- div_first_content: Here we'll be putting an image and some text.
- div_second_content: Here we'll be putting some lists and more text
- div_third_content: Here we'll be putting a table and a link to
  another page

This file looks big and complicated, but when you look at it in small
chunks, it should make sense.

---

# Final layout preview

![](img/layout_preview_large.png)

Notes:

In almost all cases, only the inner-most divs have visible content; the outer divs are just used for structuring these inner-divs.

<table>
<tr><td style="border: 1px solid" colspan="12">header</td></tr>
<tr><td style="border: 1px solid" colspan="3">div_patrol_logo</td><td style="border: 1px solid" colspan="9">div_headings_paragraphs</td></tr>
<tr><td>&nbsp;</td></tr>
<tr><td style="border: 1px solid" colspan="4">div_unordered_list</td><td style="border: 1px solid" colspan="4">div_ordered_list</td><td style="border: 1px solid" colspan="4">div_more_paragraphs</td></tr>
<tr><td>&nbsp;</td></tr>
<tr><td style="border: 1px solid" colspan="9">div_table</td><td style="border: 1px solid" colspan="3">div_program_link</td></tr>
<tr><td style="border: 1px solid" colspan="12">footer</td></tr>
</table>

---
# Final web page preview
![](img/final_web_page_preview.png) <!-- .element style="max-height: 650px" -->
----
# Final web page preview
![](img/final_web_page_preview_with_borders.png) <!-- .element style="max-height: 650px" -->
----
# Final web page preview
![](img/final_web_page_preview_with_borders_colours.png) <!-- .element style="max-height: 650px" -->

---
# For comparison
![](img/layout_preview_large.png) <!-- .element style="max-width: 690px; vertical-align: middle" -->
![](img/final_web_page_preview_with_borders_colours.png) <!-- .element style="max-width: 690px; vertical-align: middle" -->
