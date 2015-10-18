labels: Blog
        CSS
created: 2013-07-06T00:00
place: Starobilsk, Ukraine

# Play icon using pure css

![Play icon using pure css](play_icon.png)

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Play icon using pure css</title>
        <style>
            body {
                background-color: #fff;
                margin: 0;
                padding: 0;
            }
            .block {
                position: relative;
                width: 200px;
                height: 200px;
            }
            .play-button {
                width: 100px;
                height: 100px;
                position: absolute;
                top: 48px;
                right: 48px;
                border: 4px solid #222;
                border-radius: 54px;
            }
            .play-button span {
                position: absolute;
                top: 14px;
                left: 30px;
                width: 0;
                height: 0;
                border-top: 36px solid transparent;
                border-bottom: 36px solid transparent;
                border-left: 60px solid #222;
            }
        </style>
    </head>
    <body>
        <div class="block">
            <span class="play-button">
            <span></span>
        </span>
        </div>
    </body>
</html>
```

Links:

- [http://www.youtube.com/watch?v=4SdDPsdOjJw](http://www.youtube.com/watch?v=4SdDPsdOjJw)
