# CSS

Start this session with a basic HTML skeleton from the previous session with `<div>`s in place for a header, body, and footer.

We have our basic page layout now, how to we make it look pretty?

## Colors

Let's talk briefly about colors. Remember that computers can only do what we tell them, so how do we describe _exactly_ the color we want?

We can use plain English - if we just want a simple color like red.

If we want a more specific color we need to use either hexadecimal or RGB.

### Hexadecimal

`color: #ffc90c;`

- FF
- C9
- 0C

Each of these pairs of numbers or letters represents either red, green, or blue - RGB.

Hexadecimal notation counts from 0 up to F (16).

So **#FFC09C** means that we want a lot of red, a fair bit of green, and almost no blue. This comes out to yellow.

### RGB

This breaks the color down into red, green, and blue components 'out of' 255, where 0 is none, and 255 is full.

`color: rgb(123,123,123);`

### How do I work out the numbers?

We have access to a color picker in Visual Studio Code to help pick our colors. There are other tools available and all graphics design programs have ways to select colors.

---

So we know how to speak 'colors' but how do we add color to our elements?

## Cascading Style Sheets - CSS

CSS stands for Cascading Style Sheets and specifies how HTML elements should be displayed on a computer, mobile device, or when printed.

CSS can be included in HTML in a couple of different ways. One way is to specify it within the HTML tag:

```html
<table style="width: 80%; height: 80%;">
```

This approach has its downsides though. What if I have lots of tables I want styled the same, but later I decide I want them all to be 90% wide? I have to go and change every one individually! This is why **classes** are important.

Let's put some CSS in the `<head>` section of our HTML document. By doing this, I can apply some CSS to lots of elements at once, for example all images `<img>` on my page.

```html
<head>
    <style>
        body {
            background-color: #FFFFCC;
        }
        img {
            max-width: 90%;
        }
    </style>
</head>
```

---

## Using CSS

We can apply CSS to a whole document or to specific elements, or types of elements.

## Document-wide
For example, we may wish to set a background color or a font across the whole page.

```css
html {
  background-color: #ffffcc;
}
```

```css
body {
    font-family: Arial, Helvetica, sans-serif;
}
```

## Specific elements
Specific elements on a page can also have CSS applied using **classes**. I could set some padding, margins, and centre my text on a navigation bar by doing this:


```css
.navigation-bar {
    padding: 25px;
    margin: 10px;
    text-align: center;
}
```

Example:

The following CSS has been applied to a simple page. You can view the page at `http://scouthack.scouthack\css-example.html`

```css
.green-on-black {
    color: #00ff00;
    background-color: #000000;
}
.black-on-yellow {
    color: #000000;
    background-color: #ffc90c;
}
.red-on-black {
    color: #ff0000;
    background-color: #000000;
}
```

---

## Attributes
There are lots of things we can do with CSS, but let's look at a few common ones:

- text color
    - `color: #ffffcc;`
- background color
    - `background-color: #ffffcc;`
- padding
    - `padding: 0px 10px;` (top/bottom, left/right)
- margins (around an element)
    - `margin: 10px;`
- font
    - `font-family: Arial, Helvetica, sans-serif;`
    - `font-family: courier, courier new, serif;`
    - `font-size: 16px;`
- text align
    - `text-align: top | middle | bottom`
- width and height
    - `width: 250px; height: 90%;`
- borders
    - `border: 1px solid #000;`

---

Spend a bit of time playing around with adding some CSS to your page.

---
**Best practice** is to have a separate CSS file, for example `style.css`. If I specify my CSS in each page individually, if I want to change the background color of my website I would need to change it in every file. By taking this CSS out into a separate CSS file, I can update it once.

We then include this in our webpage with a line of code:

```html
<link rel="stylesheet" href="/css/style.css">
```

Let's create this file now. Move the CSS from your `<head>` section into this new file, and add `<link rel="stylesheet" href="/css/style.css">` in its place.
