labels: Draft
        JS
        NodeJS
created: 2016-08-13T15:27
place: Japan, Tokyo
comments: true

# Node.js environment notes

[TOC]

## Babel

### Example project structure

```text
- source/
-- index.js
-- another.js
- build/
- package.json
- .babelrc
```

### Requirements

```bash
npm init
npm install --save-dev babel-cli
npm install --save-dev babel-preset-es2015 babel-preset-stage-0
```

### Babel configuration

```json
{
  "presets": ["es2015", "stage-0"]
}
```

### Transpile

Add "build" target to the package.json:
```text
"scripts": {
  "build": "babel -w source/ -d build -s"
}
```

Key `-w` - watch changes.
Key `-s` - generate sourcemaps.

```bash
npm build
```

## Links

[Configuring babel 6 for node.js by on jsrocks.org](http://jsrocks.org/2016/01/configuring-babel-6-for-node-js/)
