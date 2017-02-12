labels: Draft
        Bash
created: 2017-02-12T12:26
modified: 2017-02-12T12:26
place: Phuket, Thailand
comments: true

# Tmux notes

[TOC]

## Prefix

Try `Ctrl + b`, `Cntrl + a`, `Ctrl + q`.

## Session

List:
```
tmux list-sessions
```

Create:
```
tmux new -s <session_name>
```

Attach to an existing session:
```
tmux attach -t <session_name>
```

Detach:
```
tmux detach
```
