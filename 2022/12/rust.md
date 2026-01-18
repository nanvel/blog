labels: Draft
        Rust
created: 2022-12-09T23:37
modified: 2024-12-25T16:17
place: Bangkok, Thailand
comments: false

# Rust notes

[TOC]

## Study

- (done) Programming Rust (2nd edition) by Jim Blandy, Jason Orendorff, and Leonora F. S. Tindall
- (done) https://github.com/rust-lang/rustlings
- (done) [The Rust Prograsmming Language](https://doc.rust-lang.org/book/)
- (done) Review Programming Rust
- (done) actix-web docs
- (done) [Tokio docs](https://docs.rs/tokio/latest/tokio/)
- Cleanup notes
- [Rust docs](https://doc.rust-lang.org/reference/attributes/derive.html)
- [Game of life tutorial](https://rustwasm.github.io/wasm-bindgen/introduction.html)
- Check rust std modules https://doc.rust-lang.org/std/#modules
- [api guidelines](https://rust-lang.github.io/api-guidelines/about.html)
- [nomicon](https://doc.rust-lang.org/nomicon/vec/vec.html)
- [bechmark tests](https://doc.rust-lang.org/unstable-book/library-features/test.html)
- [std lib](https://doc.rust-lang.org/std/index.html)
- [serde](https://serde.rs/)

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
eprintln!("Error ...")
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

Handling overflow:
- `wrapping_*`
- `checked_*` - Return the None value if there is overflow
- `overflowing_*` - return the value and a boolean indicating whether there was overflow
- `saturating_*`

#### String

Both String and str slices are utf-8 encoded.

String literals are string slices stored in the program binary.

```rust
let s = String::new();
let s = String::from("initial contents");
let s = "initial contents".to_string();
let s = r"c:\..."  // raw string
```

Concat:

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2; // note s1 has been moved here and can no longer be used

let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{s1}-{s2}-{s3}");
```

Iterate:

```rust
for c in "Word".chars() {}
for b in "Word".bytes() {}
```

String slice (stir):
```
&str
```

String literals are slices.

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

#### Smart pointers

Smart pointers, on the other hand, are data structures that act like a pointer but also have additional metadata and capabilities.

In many cases, smart pointers own the data they point to.

- Arc - atomic reference count
- Rc - non thread-safe

A value owned by Rc is immutable.

References should never outlive their referents.

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

    Enum fields are public if enum has pub.

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

#### Collections

Python -> Rust:
```text
list -> Vec<T>
collection.deque -> VecDeque<T>
- -> LinkedList<T>
heapq -> BinaryHeap<T> where T: Ord
dict -> HashMap<K, V> where K: Eq + Hash
- -> BTreeMap<K, V> where K: Ord
set -> HashSet<T> where T: Eq, Hash
- -> BTreeSet<T> where T: Ord
```

#### Vectors

`Vec<T>` is a resizable array of elements of type T, allocated on the heap.

```rust
// let v: Vec<i32> = Vec::new();
// v.push(2)
let mut primes = vec![2, 3, 5];

primes.push(6)
let does_not_exist = &primes[100];
let does_not_exist = primes.get(100);

for i in &primes {
    println!("{i}");
}
```

Vectors can store enumes.

Buffer large enough to hold the items:
```rust
Vec::with_capacity(1000)
```

#### Hash Map

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

`scores.insert` - overrides.
`scores.entry` - inserts if not present.

Update values:
```rust
for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}
```

#### Custom types

```rust
type Kilometers = i32;
type Thunk = Box<dyn Fn() + Send + 'static>;
```

#### Never type

`!`

Never returns, divergent function:
```rust
fn bar() -> ! {
    // --snip--
}
```

#### Function type

- `Fn` - closure trait
- `fn` - function type

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

fn main() {
    let answer = do_twice(add_one, 5);

    println!("The answer is: {answer}");
}
```

Unlike closures, `fn` is a type rather than a trait.

Closure can be returned:
```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
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

### Loops

Loops are expressions, they return `()` by default, by can return something useful using break.

### Functions

All Rust functions are thread-safe.

```rust
def five() -> i32 {
    5
}
```

### Closures

Can be called as if it were a function.

Anonymous functions that capture their environment.

Can create the closure in one place and then call the closure elsewhere to evaluate it in a different context.

```rust
fn  add_one_v1   (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x|             { x + 1 };
let add_one_v4 = |x|               x + 1  ;
```

Closures can capture values from their environment in three ways, which directly map to the three ways a function can take a parameter: borrowing immutably, borrowing mutably, and taking ownership. The closure will decide which of these to use based on what the body of the function does with the captured values.

Traits:

- `FnOnce`
- `FnMut`
- `Fn`

### Iterators

`.iter()` - [doc](https://doc.rust-lang.org/std/iter/index.html)

`.collect()` - iterator back to collection.

```rust
let v1 = vec![1, 2, 3];

let mut v1_iter = v1.iter();

assert_eq!(v1_iter.next(), Some(&1));
assert_eq!(v1_iter.next(), Some(&2));
assert_eq!(v1_iter.next(), Some(&3));
assert_eq!(v1_iter.next(), None);
```

- `iter` method produces an iterator over immutable references
- `into_iter` iterator that takes ownership and returns owned values
- `iter_mut` iterate over mutable references

```rust
let v1: Vec<i32> = vec![1, 2, 3];
let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();
assert_eq!(v2, vec![2, 3, 4]);

shoes.into_iter().filter(|s| s.size == shoe_size).collect()
```

### Library

Turn a program into a library:

- `src/main.rs -> src/lib.rs`
- add `pub` to `lib.rs` for public features
- `src/bin/program_name.rs` - move `main` here
- `cargo run --bin program_name`

### Modules

A package can have only one lib or/and one or more binaries.
A package can have multiple binary crates by placing files in the src/bin directory.

```text
src/main.rs  // binary with the package name
src/lib.rs  // lib with the package name
src/bin/*.rs  // other binaries
```

#### Declare a module

`mod garden`:

- Inline, within curly brackets that replace the semicolon following mod garden
- In the file src/garden.rs
- In the file src/garden/mod.rs (`mod.rs` is deprecated, old style)

#### Use

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

#### Pub

`pub` - make it public.

Without pub - can be used in the same module or in children modules.

`pub(crate) fn ...` - available anywhere inside crate.

`pub(super)` - visible to the parent module.

#### Statics and constants

Modules can also define statics and constants.

```rust
pub const ROOM_TEMPERATURE: f64 = 20.0;
pub static ROOM_TEMPERATURE: f64 = 20.0;
```

Constant - similar to `c++ #define` (compiled into code in every place it is used).

Static - a variable that is being set before program start (use for larger amounts of data).

A subtle difference between constants and immutable static variables is that values in a static variable have a fixed address in memory. Using the value will always access the same data. Constants, on the other hand, are allowed to duplicate their data whenever they’re used. Another difference is that static variables can be mutable. Accessing and modifying mutable static variables is unsafe.

### Errors

Errors:

- recoverable
- unrecoverable

Panic in examples, prototype code, and tests, or when have more information than the compiler.

Option vs Result:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}

enum Option<T> {
    Some(T),
    None,
}
```

Do not unwind stack on panic:

```toml
[profile.release]
panic = 'abort'
```

Error propagation with `?`:
```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

`?` can also be used on Option.

`panic!` is per thread.

### Traits

Traits - defining shared behavior.

A trait as a collection of methods that types can implement.

Traits are similar to a feature often called interfaces in other languages, although with some differences.

For any type T that implements the FromStr trait.
```rust
<T: FromStr>
```

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}
```

With associated types, we don’t need to annotate types because we can’t implement a trait on a type multiple times:
```rust
impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {}
}
```

### Lifetimes

lifetimes: a variety of generics that give the compiler information about how references relate to each other.
Lifetimes allow us to give the compiler enough information about borrowed values so that it can ensure references will be valid in more situations than it could without our help.

The main aim of lifetimes is to prevent dangling references, which cause a program to reference data other than the data it’s intended to reference.

The lifetime of the reference returned by the longest function is the same as the smaller of the lifetimes of the values referred to by the function arguments:
```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

The function signature now tells Rust that for some lifetime `'a`, the function takes two parameters, both of which are string slices that live at least as long as lifetime `'a`.

The function signature also tells Rust that the string slice returned from the function will live at least as long as lifetime `'a`.

An instance of ImportantExcerpt can’t outlive the reference it holds in its part field:
```rust
struct ImportantExcerpt<'a> {
    part: &'a str,
}
```

All string literals have the 'static lifetime, which we can annotate as follows:
```rust
let s: &'static str = "I have a static lifetime.";
```

Lifetime and generic:
```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

### Generics

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

The type `Point<f32>` will have a distance_from_origin method; other instances of `Point<T>` where T is not of type f32 will not have this method defined.

We can use trait bounds to specify that a generic type can be any type that has certain behavior.

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

pub fn notify<T: Summary>(item: &T) {
    println!("Breaking news! {}", item.summarize());
}

pub fn notify(item1: &impl Summary, item2: &impl Summary) {}

pub fn notify<T: Summary>(item1: &T, item2: &T) {}

pub fn notify(item: &(impl Summary + Display)) {}
pub fn notify<T: Summary + Display>(item: &T) {}

fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {}
fn some_function<T, U>(t: &T, u: &U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{}

fn returns_summarizable() -> impl Summary {} // doesn't work for multiple types returned
```

#### Turbofish

`::<>`. This helps the inference algorithm understand specifically which collection you're trying to collect into.

```rust
let a = [1, 2, 3];

let doubled = a.iter().map(|x| x * 2).collect::<Vec<i32>>();
```

### Attributes

Attributes are metadata about pieces of Rust code.

### Macros

Fundamentally, macros are a way of writing code that writes other code, which is known as metaprogramming.

The `!` character marks a macro invocation (declarative macro).

Examples:
```rust
assert!
debug_assert!
format!("Example {}", arg)
```

Types:

- Custom `#[derive]` macros that specify code added with the derive attribute used on structs and enums
- Attribute-like macros that define custom attributes usable on any item
- Function-like macros that look like function calls but operate on the tokens specified as their argument

### Memory management

`move` - indicates that closure takes ownership of the variables it uses.

Rust enforces a "single writer or multiple readers" rule: either can read and write the value, or it can be shared by any number of readers, but never both at the same time.

[Stack vs heap](https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/the-stack-and-the-heap.html):

- stack objects are copied
- heap objects are moved (pointer of a moved objects is being invalidated)
- stack is faster and used for known fixed-size memory allocation
- heap is slower and used when the memory allocation size is unknown

## Testing

Change a function into a test function, add `#[test]` on the line before `fn`.

```rust
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
```

```shell
cargo test
```

Macros:

- `assert!(bool)`
- `assert_eq!()`
- `assert_ne!()`


```rust
#[test]
fn it_works() -> Result<(), String> {
    let result = add(2, 2);

    if result == 4 {
        Ok(())
    } else {
        Err(String::from("two plus two does not equal four"))
    }
}
```

Running a single test:
```shell
cargo test example_test
```

We can run all the tests in a module by filtering on the module’s name.

Tests:

- unit (same files as the code with `#[cfg(test)]`)
- integration (external to the library: `tests/integration_test.rs`)

Rust’s privacy rules do allow you to test private functions.

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

minifb + raqote for graphical desktop app.

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

## Vocabulary

System programming: resource-constrained programming.

## Links

[The Rust Prograsmming Language](https://doc.rust-lang.org/book/)
[Programming Rust (2nd edition)](https://www.amazon.com/Programming-Rust-Fast-Systems-Development-ebook/dp/B0979PWD4Z/) by Jim Blandy, Jason Orendorff, and Leonora F. S. Tindall
[Let's Get Rusty](https://www.youtube.com/@letsgetrusty) on YouTube
[Rust Language Cheat Sheet](https://cheats.rs/)
[Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/intro.html)
[blessed.rs - recommended crates](https://blessed.rs/crates)

### To read

- https://pragprog.com/titles/khrust/programming-webassembly-with-rust/
- [Yew.rs and Actix Web](https://codevoweb.com/build-full-stack-app-with-rust-yew-and-actix-web/)
