labels: Blog
        Bash
created: 2014-04-05T00:00
place: Starobilsk, Ukraine
comments: true

# [bash] Copy user from one htpasswd file to another

Let's imagine: we have two sites on one host, access to both is restricted, used basic HTTP authentication where passwords are stored in htpasswd file. One user already registered on one site and we want to add him to another one and leave the same username and password.

```bash
#! /bin/sh

USAGE_ERROR="Usage: $SCRIPTNAME {copyuser username}"

SOURCE_HTPASSWD=/folder/site1/.htpasswd
TARGET_HTPASSWD=/folder/site2/.htpasswd

USER=user
HOST=host

copy_user() {
    command="test -f $TARGET_HTPASSWD || exit 1"
    command="test -f $SOURCE_HTPASSWD || exit 1"
    command="${command} ; cp $TARGET_HTPASSWD \"$TARGET_HTPASSWD.bak\""
    command="${command} ; grep -qw $1 $TARGET_HTPASSWD && exit 0"
    command="${command} ; grep -qw $1 $SOURCE_HTPASSWD || exit 1"
    command="${command} ; cat $SOURCE_HTPASSWD | grep ^$1: | awk \"NR == 1\" >> $TARGET_HTPASSWD"
    echo -e $command | ssh $USER@$HOST 2>/dev/null
}

case "$1" in
    copyuser)
        if [ $2 ]; then
            copy_user $2
        else
            echo $USAGE_ERROR
            exit 1
        fi
    ;;
    *)
        echo $USAGE_ERROR
        exit 1
    ;;
esac
exit $?
```

## Usage example

Create two htpasswd files and add few users:
```bash
nanvel$ /usr/sbin/htpasswd -b -c .htpasswd1 izumi izumipass
Adding password for user izumi
nanvel$ /usr/sbin/htpasswd -b .htpasswd1 yui yuipass
Adding password for user yui
nanvel$ /usr/sbin/htpasswd -b -c .htpasswd2 misaka misakapass
Adding password for user misaka
nanvel$ /usr/sbin/htpasswd -b .htpasswd2 adzusa adzusapass
Adding password for user adzusa
```

As a result, I have two files:
```bash
nanvel$ cat .htpasswd1
izumi:$apr1$IFUc4Sgr$EWXwKc5MpairBuuoyWaTj0
yui:$apr1$FeI4sM9r$qOHL9H6njqZ0Qe5QAUG6N0

cat .htpasswd2
misaka:$apr1$Zg/Wq3Tl$uOPB4IaQmklCGqcEqEJFP.
adzusa:$apr1$fwUSR8yI$LJlsvnFAmTAIvPbOVeqXS/
```

Let's try to copy ```izumi``` to ```.htpasswd2```:
```bash
nanvel$ bash copyuser.sh copyuser izumi
nanvel$ echo $?
0

nanvel$ cat .htpasswd1
izumi:$apr1$IFUc4Sgr$EWXwKc5MpairBuuoyWaTj0
yui:$apr1$FeI4sM9r$qOHL9H6njqZ0Qe5QAUG6N0

nanvel$ cat .htpasswd2
misaka:$apr1$Zg/Wq3Tl$uOPB4IaQmklCGqcEqEJFP.
adzusa:$apr1$fwUSR8yI$LJlsvnFAmTAIvPbOVeqXS/
izumi:$apr1$IFUc4Sgr$EWXwKc5MpairBuuoyWaTj0

nanvel$ cat .htpasswd2.bak
misaka:$apr1$Zg/Wq3Tl$uOPB4IaQmklCGqcEqEJFP.
adzusa:$apr1$fwUSR8yI$LJlsvnFAmTAIvPbOVeqXS/
```

## Run script from python code

```python
import subprocess


proc = subprocess.Popen(
    ['bash', PATH_TO_SCRIPT, username],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = proc.communicate()[0]
code = proc.poll()
```
