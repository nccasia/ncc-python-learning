- [How The Web Works](#how-the-web-works)
  - [Background:](#background)
  - [Questions:](#questions)

## How The Web Works

### Background:

Review the materials below.

* First let's read 
  * [How the internet work](https://developer.mozilla.org/en-US/Learn/Common_questions/How_does_the_Internet_work)
  * [MDN HOW WEB WORKS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
* Next let's watch a few quick examples of [how the internet works](https://www.youtube.com/watch?v=7_LPdttKXPc).
* [how IP addresses work](https://www.youtube.com/watch?v=KFooN7Mu0IM).
* https://bgoonz-blog.vercel.app/docs/articles/how-the-web-works/
* Finally let's tie these things together and watch a video about [DNS - what happens when you type an address into a web browser](https://www.youtube.com/watch?v=72snZctFFtA).
* Lastly, let's read a little about [the anatomy of a URL](https://doepud.co.uk/blog/anatomy-of-a-url)

### Questions:

Now we have a better grasp about the internet, and how some of the things are working. Now, let's answer a few questions to check our understanding. Don't be afraid to do additional research (googleing) for an answer. Fork this gist and answer the following questions:

1. Describe, step by step, what happens when I type `www.example.com` into my browser and try to go to the page?
 - Your browser contacts the RNS server to find the IP address of the server that hosts the site you want.
 - Your browser sends an HTTP request to the server at example's IP address via the internet.
 - That server recieves the request, and sends a 200 response and starts sending the files(in packet form) that we requested to our computer.
 - The files are received on your computer, and are pieced together to render the webpage we asked for.
2.  What does HTTP stand for? HyperText Transfer Protocol
3. 	What protocol does the World Wide Web use? HTTP
4. 	Each computer on the Internet is assigned an IP address, what does IP stand for? 
    Internet Protocol
5. 	What does DNS stand for? DOMAIN NAME SERVER
  * A. Domain Name System
  * B. Digital Number System
  * C. Domain Number System
  * D. Domain Name Service
  * E. Digital Name Service
6. 	How are text domain names matched to their respective numeric IP addresses?
  The text domain names are stored along with the IP address they point to on a Domain Name Server by the Domain Name Registrar.
7. 	What is the client? E and/or C
  * A. A purchaser
  * B. Internet shopping customer (Consumer)
  * C. The software which requests information from a server (browser)
  * D. The server to which a particular computer sends data
  * E. The computer which the IP address belongs to
8. 	What does URL stand for?
    Uniform Resource Locator
9. What does DNS stand for? DOMAIN NAME SERVER
10. what is the `www` portion of a url?
11. What is The markup language used for all web documents? HTML
12. What is the organization that monitors web technologies? 
13. What is the Protocol for transferring web documents on the Internet? HypterText Transfer Protocol
14. What matches the domain names with numeric IP addresses? The DNS