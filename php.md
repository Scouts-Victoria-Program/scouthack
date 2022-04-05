# PHP - Personal Home Page - then PHP Hypertext Preprocessor
## Introduction to PHP
Think about a website that has a shopping cart - if I visit the website and put $1,000,000 worth of goodies in my shopping cart. Then Luke visits - and breaks it by removing everything <br /><span style="font-size: 32pt; margin: 50%; text-align:center">😱</span><br />
We are now locked in a battle of me adding my goodies and checking out before Luke removes them - Or we get the server to serve me a different page to Luke. The problem here is that we **have** to serve HTML. So we change the HTML before we send it out. There are many ways to do this - but we are going to look at PHP first. Mainly, because it's *easy*.
## How to we make a HTML file PHP?
Existing files are .html - we change them to .php. That's it. We only inject PHP where something needs to happen. A server like Apache2 will render the PHP for us - but for all the elements that don't change, we just leave it as plain HTML <br />
<span style="font-size: 32pt; margin: 50%; text-align: center">🙃</span>
> Note - Now that these files are PHP, they **have** to be served - unlike our HTML files we **cannot** open these locally as our computers won't do the preprocessing. Of course we can use programs like *XAMPP* to serve locally
## What about when we want to add PHP then?
PHP uses funky symbols to tell the server when to start and when to stop processing the PHP elements. We start a PHP block using `<?php` and then end it with `?>`. From time to time people might start with only `<?` - this will work a lot of the time but it's a shortcut, it's improper, and after you have spent 30 days developing code on your local machine, you then deploy it to the server and suddenly everything breaks because the server decides no no, you must code properly. So for today I want to see proper `<?php` opens and `?>` closes.
## The delimiter ;
What is a delimiter? In programming languages we need to tell the computer when we have stopped giving it a command. In some languages we start a new line, PHP doesn't care about lines or spaces or things. We simply end a command using the semi-colon. **Just like CSS**. At some point you will forget this - but that's okay. You will get the hang of it.
## The first basic command and variables
The simplest PHP command simply prints some text. We can use `echo` to echo the text. So if I want to display *Hello World* to the user I simply write
```
<?php echo("Hello world"); ?>
```
Of course this makes no sense - because we could just not use PHP and write Hello World. <br />
When we want to store a variable for use later. In PHP to store a variable we use the $ symbol. PHP is not *a typed language* which means we don't need to declare a type for each variable, we can just create variables on the fly. This means we can simply write:
```
<?php
$our_text = "Hello world";
echo($our_text);
?>
```
This still isn't super helpful - but we are getting somewhere.<br />
Let's now say we want to display the current time/date.
```
<?php
$our_text = date('H:i d-m-Y');
echo($our_text);
?>
```
What's happening here? The `date` function takes a `string` which represents the way we should display the date. This means if we wanted to display the date format in American format we would write
```
date('m-d-Y');
```
## Let's pull some actual data from somewhere! GET and POST params!
There are two **major** ways to esnd data to a PHP page - there are many more ways but we are going to focus on `GET` and `POST` params<br />
GET params sit in the URL. The URL is entered followed by `?` so we can set a user get param by changing our url to `http://[[EXISTING_URL]]/?user=matt`. Then we can go
```
<?php
$our_text = $_GET['user'];
echo('Hello ' . $our_text);
?>
```
Which will now print `Hello matt`<br />
Of course we should be testing to check that the parameter exists before we try and read from it. We should also probably specify a fallback if it doesn't exist.
> You will note that the form we previously created currently sends all data via GET params - you will now _start_ to get the idea of how we can pull data through - but there's a neater way we will use in a minute
## Let's use an IF statement!!! 😁
Some of the most common statements in programming - IF statements. `IF scenario [DO SOMETHING] ELSE [DO SOMETHING ELSE]`<br />
In PHP we do this as follows:
```
<?php
if (array_key_exists('user', $_GET)):
    $our_text = $_GET['user'];
else:
    $our_text = "user";
endif;
echo("Hello " . $our_text);
?>
```
> IF statements exist in many many computer languages. If we have more possible options we can also use things like _else if_ to require another condition, or move to switch statements to compare many different possible options
## Let's do some POSTing
GET is not elegant nor secure because we can all see it, etc. An alternative is to POST our data using a form - we start in HTML
```
<form action="/post.php" method="POST">
    <input type="text" name="user" />
    <input type="submit" value="Send form" />
</form>
```
This sends our form to `post.php` with the POST param `user`.
Similar to `GET` params you will need to this time target the `$_POST` array. <br />
YAY! Data comes through
## What are we going to do with the data?!?!
We could turn it into an email - but this requires an email server as well - or we could store it in a database. But Luke came up with a great idea to save us time, so we are just going to write it to a file!
## fwrite - file write.
To write to a file - we first open a file. We have to tell computers everything so don't assume it knows where we want to store it. We should also close the file - although with only one user it won't be the end of the world if we don't - but we are going to.
```
$ourFile = fopen('./contact.txt', 'a');
```
The first argument is the filelocation, the second tells us *HOW* to open it - in this case a which stands for append. That way we don't loose any old data
Assuming we have already stored our data in `$our_text` we can now store it with
```
fwrite($ourFile, $our_text);
```
Of course the problem here is we have no idea where one form ends and the next begins - indeed we need a delimiter! We can use a new line (or two).
```
fwrite($ourFile, $our_text . '\n\n');
```
**REMEMBER** we need to close the file to be neat and tidy. It won't really matter in our case but it's a good habbit to get into
```
fclose($ourFile);
```
Now let's try getting a bit more creative.
Try and create a contact form with a name, subject, and message.
Let me know if you have questions<br /><span style="font-size: 32pt; margin: 50%">😁</span>
