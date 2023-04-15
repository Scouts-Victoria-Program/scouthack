# ScoutHack Web Dev 1.0 course

[courseMaterial.md](courseMaterial.md) is a not-particulary up-to-date guide to help scouts get their dev environment up and running, and an intro to the Linux command line (very little of which they need, because we walk them through the few commands they need as we go).

Any [reference to PHP](php.md) is deprecated, as we've largely switched to Flask.

I don't see instructions for how to get the scouts to build a Flask app in this repo, but it *does* include the [website they'll be building](flask_website_example/), which is a simple [single file](flask_website_example/website.py) app with a handful of HTML templates and static files. This is the *last* thing scouts do on Sunday, after we've taught them HTML and CSS basics.

As far as I know, this is the [latest version of the CSS instructions](css.md).

I don't see any documentation in here for the HTML component, either, but I'm sure there was some somewhere. I'll see if I can dig it up.

Ignore the [book](book/) dir for now. My plan is to tidy up thess `.md` files in the root of the repo and put them into `book/` which can then be generated as HTML using [mdbook](https://rust-lang.github.io/mdBook/), but it's currently just an empty template.

The structure of the weekend, broadly, is as follows:

## Friday night

* Welcome participants
* Have them each set up their computers
    * connect the laptops to keyboard, mouse, screen, network, and boot them up
* Discuss basic networking
    * why do I have network access but no internet? Where will we be working?
* Basic intro to Xubuntu
    * here's VS code, and Firefox
    * here's how to set up VS code to use an environment on a remote server using the [SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) (Each scout gets a user account with full sudo access on a remote Debian (or is it Ubuntu? need to check) Docker container)
* How to create a basic HTML web page and browse to it, either on the local filesystem, or via HTTP to their personal server
* How HTML works, basic tags, etc

## Saturday

* Intro to CSS and Bootstrap

## Sunday

* Putting it all together with Flask
