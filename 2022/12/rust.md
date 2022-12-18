labels: Draft
        Rust
created: 2022-12-09T23:37
modified: 2022-12-09T23:37
place: Bangkok, Thailand
comments: false

# Rust notes

[TOC]

## Cargo

[Cargo book](https://doc.rust-lang.org/cargo/index.html)

```text
cargo --version
cargo build
cargo build --release
cargo check
cargo test
cargo doc
cargo doc --open  # docs for each of dependencies
cargo new <project name>
caego update  # update dependencies
cargo run
cargo publish  # publish a library to crates.io
```

## Rust

Default imports from stdlib: https://doc.rust-lang.org/std/prelude/index.html


```bash
rustc --version

rustc main.ru
./main
```

Open the Rust book locally:
```bash
rustup docs --book
```

### Output

```rust
println!("Output ...")
```

### Input

```rust
use std::io;

let mut guess = String::new();
io::stdin().
    .read_line(&mut guess)
    .expect("Failed to read line!")
```

### Variables

Variables are immutable by default.

```rust
let apples = 5;
```

### Types

#### Numbers

```text
i8, i32 (default), u32, i64, u64
```

#### Tuple

```rust
let tup: (i32, f64, u8) = (600, 6.4, 1);

let five_hundred = tup.0
```

#### Array

```rust
let a: [i32, 5] = [1, 2, 3, 4, 5];
let a = [3; 5];  // [3, 3, 3, 3, 3]
let i = a[0];
```

References:
```rust
let a = [1, 2, 3, 4, 5];

let slice = &a[1..3];

assert_eq!(slice, &[2, 3]);
```

#### Struct

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

let user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
};
```

Shorthand:
```rust
fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}
```

Tuple struct:
```rust
struct Color(i32, i32, i32);
```

Update:
```rust
let user2 = User {
    email: String::from("another@example.com"),
    ..user1
};
```

Methods:
```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}
```

Associated functions (clss methods):
```rust
impl Rectangle {
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

let sq = Rectangle::square(3);
```

#### Enum

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn call(&self) {

    }
}

let m = Message::Write(String::from("Test"));
m.call()
```

`Option` enum:
```python
let some_number = Some('a') // Option<char>
let absent_number: Option<i32> = None;
```

### Expressions

Statement:
```rust
let y = 1;
```

Expression inside `{}`:
```rust
let y = {
    let x = 0;
    x + 1
}
```

Expressions do not end with `;`.

### Functions

```rust
def five() -> i32 {
    5
}
```

### Modules

A package can have only one lib or/and one or more binaries.

```text
src/main.rs  // binary with the package name
src/lib.rs  // lib with the package name
src/bin/*.rs  // other binaries
```

## rustup

`rustup` - a command line tool for managing Rust versions and associated tools.
`rustup update` - update to new version.
`rustup doc`

## Links

[The Rust Prograsmming Language](https://doc.rust-lang.org/book/)
