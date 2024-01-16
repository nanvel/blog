labels: Draft
        Rust
created: 2022-12-09T23:37
modified: 2023-12-29T18:19
place: Bangkok, Thailand
comments: false

# Rust notes

loc: 66

[TOC]

## Study

- (done) Programming Rust (2nd edition) by Jim Blandy, Jason Orendorff, and Leonora F. S. Tindall
- Review Programming Rust
- (done) https://github.com/rust-lang/rustlings
- [The Rust Prograsmming Language](https://doc.rust-lang.org/book/) (in progress)
- [Geme of life tutorial](https://rustwasm.github.io/wasm-bindgen/introduction.html)
- check rust std modules https://doc.rust-lang.org/std/#modules

## Cargo

Cargo is Rust's:

- compilation manager
- package manager
- general-purpose tool

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

rustc main.rs
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

Zero-tuple, or unit type: `()`.

Rust uses unit type where there is no meaningful value to carry.

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

Methods like filtering, sorting, etc. are provided as methods on slices. Rust implicitly converts a reference to an array to a slice.

#### Pointer types

- references
- boxes
- unsafe pointers

Box (allocates memory on the heap):
```rust
let t = (12, "eggs")
let b = Box::new(t)  // Box<(i32, &str)>
// when b goes out of scope - memory freed on heep
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

!!! note "Private and public fields"
    A struct's fields, even private fields, are accessible throughout the module where the struct is declared, and its submodules. Outside the module, only public fields are accessible.

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

#### Vectors

`Vec<T>` is a resizable array of elements of type T, allocated on the heap.

```rust
let mut primes = vec![2, 3, 5];
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

### Match

```rust
match (T:from_str(&s[..index]), T::from_str(&s[index + 1..])) {
    (Ok(l), Ok(r)) => Some((l, r)),
    _ => None,
}
```

### Functions

All Rust functions are thread-safe.

```rust
def five() -> i32 {
    5
}
```

### Closures

Can be called as if it were a function.

### Iterators

`.iter()` - [doc](https://doc.rust-lang.org/std/iter/index.html)

`.collect()` - iterator back to collection.

### Library

Turn a program into a library:

- `src/main.rs -> src/lib.rs`
- add `pub` to `lib.rs` for public features
- `src/bin/program_name.rs` - move `main` here
- `cargo run --bin program_name`

### Modules

A package can have only one lib or/and one or more binaries.

```text
src/main.rs  // binary with the package name
src/lib.rs  // lib with the package name
src/bin/*.rs  // other binaries
```

Import:
```rust
use std::fs::{self, File};
use std::io::prelude::*;
use std::io::Result as IOResult;
use super::AminoAcid;
use crate::proteins::AminoAcid;
use ::image::Puxels;  // image crate
use self::image::Sampler;  // image module
pub use self::image::Sampler;
```

Naming a module a `prelude` is just a convention that tells users it's ment to be imported using `*`.

#### Statics and constants

Modules can also define statics and constants.

```rust
pub const ROOM_TEMPERATURE: f64 = 20.0;
pub static ROOM_TEMPERATURE: f64 = 20.0;
```

Constant - similar to `c++ #define` (compiled into code in every place it is used).

Static - a variable that is being set before program start (use for larger amounts of data).

### Traits

A trait as a collection of methods that types can implement.

For any type T that implements the FromStr trait.
```rust
<T: FromStr>
```

### Macros

The `!` character marks a macro invocation.

Examples:
```rust
assert!
debug_assert!
format!("Example {}", arg)
```

### Memory management

`move` - indicates that closure takes ownership of the variables it uses.

Rust enforces a "single writer or multiple readers" rule: either can read and write the value, or it can be shared by any number of readers, but never both at the same time.

[Stack vs heap](https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/the-stack-and-the-heap.html):

- stack objects are copied
- heap objects are moved (pointer of a moved objects is being invalidated)
- stack is faster and used for known fixed-size memory allocation
- heap is slower and used when the memory allocation size is unknown

## [rustup](https://rustup.rs/)

`rustup` - a command line tool for managing Rust versions and associated tools.
`rustup update` - update to new version.
`rustup doc`
`rustup doc --std`

## Libs

[Egui](https://github.com/emilk/egui) - an easy-to-use GUI in pure Rust

[Web frameworks](https://www.arewewebyet.org/topics/frameworks/) - backend and frontend

[Awesome rust](https://github.com/rust-unofficial/awesome-rust) - a curated list of Rust code and resources

[Leptos](https://www.youtube.com/watch?v=eipr8zYP2T0) - build both frontend and backend

## App with multiple targets

Structure:

- backend
- common
- frontend
- Cargo.toml

### Workspaces

A workspace is a set of packages that share the same Cargo.lock and output directory.

Using [cargo-workspaces](https://doc.rust-lang.org/book/ch14-03-cargo-workspaces.html):
```shell
cargo new --lib common
cargo new backend
cargo new frontend
cargo workspaces init
```

## Links

[The Rust Prograsmming Language](https://doc.rust-lang.org/book/)
[Programming Rust (2nd edition)](https://www.amazon.com/Programming-Rust-Fast-Systems-Development-ebook/dp/B0979PWD4Z/) by Jim Blandy, Jason Orendorff, and Leonora F. S. Tindall
[Let's Get Rusty](https://www.youtube.com/@letsgetrusty) on YouTube
[Rust Language Cheat Sheet](https://cheats.rs/)
[Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/intro.html)

### To read

- https://pragprog.com/titles/khrust/programming-webassembly-with-rust/
- [Yew.rs and Actix Web](https://codevoweb.com/build-full-stack-app-with-rust-yew-and-actix-web/)
