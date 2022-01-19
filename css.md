# CSS
CSS stands for Cascading Style Sheets and specifies how HTML elements should be displayed on a computer, mobile device, or when printed.

Today we will focus on the basics of how to style the webpage you've already started putting together.

---

## Attributes
There are lots of attributes available, but let's look at a few common ones:

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
Specific elements on a page can also have CSS applied using **classes**.



```css
.my-div {
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
## Colors - what exactly does #FFC90C mean?
There are a few ways of telling a computer what color you want. One is using **hexadecimal notation**.

Let's break **#FFC90C** down into three parts:

- FF
- C9
- 0C

Each of these pairs of numbers or letters represents either red, green, or blue - RGB.

Hexadecimal notation counts from 0 up to F (16).

So **#FFC09C** means that we want a lot of red, a fair bit of green, and almost no blue. This comes out to yellow.

---

## Using CSS on your website

CSS can be included in HTML in a couple of different ways.

One way is to specify it within the HTML tag:

```html
<table style="width: 80%; height: 80%;">
```

This approach has its downsides though. What if I have lots of tables I want styled the same, but later I decide I want them all to be 90% wide? I have to go and change every one individually! This is why **classes** are important.

Let's put some CSS in the `<head>` section of our HTML document.

```html
<head>
    <style>
        body {
            background-color: #FFFFCC;
        }
    </style>
</head>
```

**Best practice** is to have a separate CSS file, for example `style.css`. Like the `table ` example above, if I wanted to change the background color of all pages on my website I would still need to change it in every document.

We then include this in our webpage with a line of code:

```html
<link rel="stylesheet" href="/css/style.css">
```