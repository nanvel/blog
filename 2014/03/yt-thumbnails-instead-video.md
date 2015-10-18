labels: Blog
        JS
created: 2014-03-22T00:00
place: Starobilsk, Ukraine

# Show thumbnails instead of youtube video player

![Video thumbnail vs video player](thumbnail_and_video.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Video</title>
    <style>
        body {
            padding: 20px;
        }
        .content {
            margin: 0 auto;
            width: 642px;
        }
        .yt-video {
            margin-top: 20px;
            overflow: hidden;
            position: relative;
            border: 1px solid #999999;
            width: 640px;
            height: 360px;
            cursor: pointer;
        }
        .yt-video:first-child {
            margin-top: 0;
        }
        .yt-video img {
            margin-top: -60px;
        }
        .yt-thumb:after {
            content: url('play_button_overlay.png');
            position: absolute;
            left: 129px;
            top: 75px;
        }
    </style>
</head>
<body>
    <div class="content">
        <div class="yt-video" data-vid="bn5RiQCjtug"></div>
        <div class="yt-video" data-vid="RAninNKS2a8"></div>
    </div>
    <script>
        var nodeList = document.querySelectorAll('.yt-video');
        for (var i=0, node; i<nodeList.length; i++) {
            node = nodeList[i];
            node.innerHTML = '<img src="http://img.youtube.com/vi/' + node.getAttribute('data-vid') + '/sddefault.jpg">';
            node.className = node.className + ' yt-thumb'
            node.onclick = function() {
                this.innerHTML = '<iframe width="640" height="360" src="http://www.youtube.com/embed/' + this.getAttribute('data-vid') + '?autoplay=1" frameborder="0" allowfullscreen></iframe>';
                this.className = this.className.split(' yt-thumb').join('');
                this.onclick = null;
            }
        }
    </script>
</body>
</html>
```
