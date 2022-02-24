I faced a very hard time working with tinder project because of the following:

It was challenging to click on login by google email because the browser blocked the pop-ups windows for security reasons so after I pass it by changing chrome option by adding this argument 

from this site [List of Chromium Command Line Switches « Peter Beverloo](https://peter.sh/experiments/chromium-command-line-switches/#disable-popup-blocking)

I added like this 

 

```python
# first I import the chrome options 
from selenium.webdriver.chrome.options import Options
# After that I create an insteance that will allow me to add an options to the browser
chrome_option = Options()
chrome_option.add_argument("--disable-popup-blocking")
# And finally I added to my webdriver object
driver = webdriver.Chrome(options=chrome_option)
```

But the thing is after I reached this point I couldn’t login with google email because it showed me that my browser not secure that lead my to search for a solution until I found a good one 

and it was about creating a chrome [localhost](http://localhost) server that allow me to save my account and login directly to tinder as well and I follow the instruction from this video 

[[FIXED] This browser or app may not secure. Try using a different browser - YouTube](https://www.youtube.com/watch?v=FVumnHy5Tzo)

first I added the chrome application to my PATH for later use 

second I created a [localhost](http://localhost) folder on the same destination path where I save my we driver

finally I run this command throw the cmd :

  

```python
chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\WebDriver\bin\localhost
# after that the chrome browser opened and I login with my gmail account 
```

And I need to add an options to my chrome browser as I did before but this time I’m going to use 

`add_experimental_option` because Im going to use chrome as a developer for more details you can found here [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)

So I added like this 

```python
chrome_option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=chrome_option)
```

So now I do not need to login to tender any more because it is already saved in my [localhost](http://localhost) folder 

and tinder use my Gmail login to let me login their site.

One last step was I need to start the chrome as a [localhost](http://localhost) each time so to do that throw the code I used this line 

```python
subprocess.Popen(r"chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\WebDriver\bin\localhost", shell=True)
```

So All what I did is just created one function that swap_unlike because it is a testing account and I don’t want to heart any one feeling :

This how I wrote the unlike function:

```python
def swap_unlike():
    one_minutes = time.time() + 60
    while True:
        if time.time() < one_minutes:
            wait = WebDriverWait(driver, 15)
            dislike = wait.until(ec.element_to_be_clickable((By.TAG_NAME, 'body')))
            dislike.send_keys(Keys.LEFT)
        else:
            break
        time.sleep(1)
```

So it will just swap unlike for a 30 seconds because there is a 1 second sleep for each loop.

I wrote this Solution because I saw too much people struggling with tinder day 50 project.