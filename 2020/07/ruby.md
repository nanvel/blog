labels: Ruby
        Draft
created: 2020-07-08T12:25
modified: 2022-02-11T14:22
place: Phuket, Thailand

# Ruby notes

[TOC]

Expression oriented.

## Tools

`rvm` - ruby version manager.

`gem install rails` - package manager.

## Program structure

```ruby
#!/usr/bin/ruby -w  # shebang
# -*- coding: utf-8 -*-
# or like this (the above one can be understood by editors):
# coding: utf-8

require 'socket'
...  # code

__END__

...  # data
```

## Syntax

Break to new line:

```ruby
a = 1 +
2 # works because the first line contains not a complete expression

Module1::
  Submodule # same thing

a = Array.new
  .push('example') # works because the first characted is period
```

## Types

Evalutes to false: nil, false

TRUE, FALSE, NIL constants, but lowercase is preferred.

### Literals

Literals = appear directly in source code:

- numbers
- strings
- regular expressions

### Arrays

`<<` - append operator.

### Strings

Strings are mutable.
Use freeze to prevent future modification.

```ruby
"Some text"
"Some text with \""

'Some string'  # no interpolation

# interpolation
"Some text #{1 + 1}"
"Some test #$global_variable_name"
# also can be used sprintf("pi is about %.4f", Math::PI)

%|Some text|

# using %, %q, %Q
# %i - array of symbols
# %q - string
# %r - regular expression
# %s - symbol
# %w - array of strings
# %x - backtick

# multiline
result = <<HEREDOC
This would contain specially formatted text.

That might span many lines
HEREDOC

# Python 2 style
"%d %s" % [3, 'rubies']
```

Embedded documents as multiline comments:
```ruby
=begin Multiline comment ...
Another line ...
=end
```

Multiline:
```ruby
with_newline = 'line 1 \
line2'

without_newline = 'line 1 '\
'line 2'

a = "This string literal
has two lines \
but is written on three."
```

Double quoted `"` string literals support `\t`, `\n`, `\r`, `\"`.

Unicode:
```ruby
"\u{A5}"  # same as \u00A5
```

Regular excpressions:
```ruby
/\d+/

"powerball" =~ /b/
```

Conversion:
```ruby
"1".to_i
"1.1".to_f
```

### Numbers

Numeric:

- Integer (Fixnum (31 bits), Bignum)
- Float
- Complex
- BigDecimal
- Rational

Examples:

- `1_000`
- `0.1`
- `6.02e5` (6.02 * 10^5)
- `0377` (octal)
- `0b1101`
- `0xff`

`1 / 0` -> ZeroDivisionError
`1. / 0` -> Infinity
`0.0 / 0.0` -> NaN

### Symbols

Symbols - immutable interned strings. Can be compared by identity rather than by textual content.

```ruby
:my_symbol
```

### Hashes

```ruby
{ "a" => 1 }
{ a: 1 }
```

### Ranges

```ruby
(1..2)  # includes ending values
(1...2)  # excludes ending values
```

`==` test equally.
`===` for matching and membership.

### Procs (procedures)

```ruby
-> { 1 + 1 }
->(a) { a + 1 }
```

### Blocks

Define variable scope.

Use `{ }` or `do/end`.

```ruby
do |var|
  put 123
end
```

### Struct

[Struct](https://ruby-doc.org/core-2.5.0/Struct.html)

```ruby
Customer = Struct.new(:name, :address) do
  def greeting
    "Hello #{name}!"
  end
end

dave = Customer.new("Dave", "123 Main")
```

### `::`

```ruby
Encoding::Converter  # namespace
```

### Loops

```ruby
for i in arr do
  puts i
end
```

```ruby
loop do
	puts 1
	# next
	break
end
```

```ruby
while x > 0:
	puts x
	x = x - 1
end
```

```ruby
until x < 0:
	puts x
	x -= 1
end
```

### Variables

```ruby
CONSTANT = 1
$global_var = 1
@@class_variable = 1
@instance_variable = 1
local_variable = 1
```

Parallel assignment:

```ruby
x, y = 1, 2
```

### Methods

Methods are defined with the `def` keyword. The return value of a method is the value of the last expression evaluated in its body.

```ruby
def say
  # method body goes here
end
```

When a methods is defined outside a class or module, it is effectively a global function (technically, becomes a private method of the Object class).

Methods can be defined on individual objects (singleton methods):
```ruby
def Math.square(x)
  x * x
end

def sefl.my_class_method(x)
  # ...
end
```

Blocks can be passed to methods:
```ruby
def take_block(&block)
  block.call
end

take_block do
  puts "Block call"
end
```

Procs are stored blocks:
```ruby
talk = Proc.new do
  puts "I am talking."
end
```

Assignment methods:
```ruby
def a=(x):
  x + 1
end

# my_object.a = 10  # => 11
```

Qustion mark suffix:
```ruby
def can_call?
  true
end
```

A question mark if used to mark predicates - methods that return a Boolean value.

Exclamation mark suffix: is used to indicate that caution is required with the use of the method.

```ruby
def delete!
end
```

Often exlamation marks is used in mutator method that alters the objects in place.
Example: `#sort` vs `#sort!`.

### Flow control

The value of `nil` is treated the same as `false` and any other value is the same as `true`!

`x = if x < y then x else y end`  - this is an expression.

```ruby
if a == 1
	puts 1
elsif a == 2
	puts 2
else
	puts 'another'
end
```

```text
&& -> and
|| -> or
! - not
```

 Ternary operator:
 ```ruby
 true ? "True" : "Not True"
 ```

```ruby
case a
when 1
	puts 1
when 2
	puts 2
else
	puts 3
end
```

### Iterators

```ruby
numbers = [1, 2, 3]
numbers.each { |n| puts n }
```

### Exceptions

```ruby
begin
	pass
rescue
	pass
end

begin
    answer = number / divisor
rescue ZeroDivisionError => e
  	puts e.message
end
```

### Modules

Similar to class but can not be instantiated.

### Self

In singleton methods - refers to the class:
```ruby
class Dog
  def self.about
    self  # Dog
  end
end
```

### Classes

A class is a collection of related methods that operate on the state of an object.

Classes and modules are "open", and can be modified and extended at runtime.

```ruby
class Customer
   @@no_of_customers = 0  # class variable
   def initialize(id, name, addr)  # when we call new
      @cust_id = id  # instance variables
      @cust_name = name
      @cust_addr = addr
   end
end
```

Extending a class:

```ruby
class Sequence
  include Enumerable
end
```

Overriding methods:

```ruby
def [](index)
end

def *(factor)
end
```

### Memoization

```ruby
def something
  @something = Something.new()
end
```

### Output

```ruby
puts 'Hello!'  # prints the string and appends a newline (unless already ends with a newline)
print 'Hello!'  # prints the string (without appending a newline)
p 'Hello!'  # same a puts + converts objects to string (more programmer friendly)
```

## Debugging

Run inline:
```bash
ruby -e 'puts "Hello world!"'
```

```bash
irb  # interactive ruby
irb --simple-prompt
pry
```

[pry](https://github.com/pry/pry)

```ruby
require 'pry'
binding.pry
```

Documentation:
```bash
ri Math::sqrt
```

## RSpec

### Run

```bash
rspec spec/folder
rspec spec/folter/test_spec.rb
rspec spec/folder/test_spec.rb --example(-e) name
rspec spec/folder/test_spec.rb:25 (code line)
rspec --only-failures (requires config)
```

### Pending

```ruby
if 'does something' do
  pending 'Not implemented yet ...'
  expect().to be()
end
```

### Testing

Expect:
- `.to`
- `.not_to`

Arrays:
```ruby
expect().to match_array
```

`deascribe` and `it` - organization.
`expect` - verification.
`let` - initializes data on deman.
`context` (lias to `describe`) - grouping for setup and examples.
`before` hook - run before each example (can be inside context).

Expect:
- be_empty
- eq

## Links

[Ruby at LaunchSchool](https://launchschool.com/books/ruby/read/introduction)
Learn Ruby the Hard Way by Zed Shaw (to read)
[The Ruby Programming Language](https://www.amazon.com/Ruby-Programming-Language-Everything-Need/dp/0596516177) by David Flanagan, Yukihiro Matsumoto
