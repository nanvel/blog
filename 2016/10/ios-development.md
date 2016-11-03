labels: Draft
        iOS
created: 2016-10-18T19:15
modified: 2016-10-18T19:15
place: Phuket, Thailand
comments: true

# iOS development notes

[TOC]

## Layout

VisualFormat:
```text
V:|-20-[myButton1(>=70@500)]-[MyButton2(==myButton1)]-30-[myButton3]-|
```
`V:` - vertical, default: `H:`
`@500` - priority: 0..1000
`>=70` - height
`-` - standard spacing, 8 points
`-20-` - non standard spacing

See [Visual Format Language](https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/AutolayoutPG/VisualFormatLanguage.html)

[Auto Layout Visual Format Language Tutorial](https://www.raywenderlich.com/110393/auto-layout-visual-format-language-tutorial).

[Self-sizing Table View Cells](https://www.raywenderlich.com/129059/self-sizing-table-view-cells)

### Best practices

**Hit Targets**: Create controls that measure at least 44 points x 44 points so they can be accurately tapped with a finger.

**Text Size**: Text should be at least 11 points so it's legible at a typical viewing distance without zooming.

**Contrast**: Make sure there is ample contrast between the font color and the background so text is legible. 

**Spacing**: Don't let text overlap. Improve legibility by increasing line height or letter spacing.

^ according to [UI Design Do’s and Don’ts](https://developer.apple.com/design/tips/).

Don't use case to emphasize because not all writings systems support it. Use size and color instead.

Use dynamic type.

Colors elicit emotions.

Contrast ration: >4.

iOS font: San Francisco.

`UIFont.systemFont(ofSize: 14)`

## Design

What are we making?

## Story boards

> Given that Interface Builder is heavily touted by Apple as the ideal solution for building UI, I was very reluctant to ditch it, especially given how wordy programmatic layout used to be. Once I saw how concise and declarative doing auto-layout in Swift could be, I decided to give it a shot. After defaulting to no xibs for about a week, I was totally sold. I feel the maintainability of my view code has gone up considerably, a few blocks of Swift code is much more approachable to a new developer than a tangled mess of Interface Builder constraints, and tracking changes over time in version control is also possible where it really wasn’t before.”
>
> Nick Bonatsakis, iOS Team Lead at Raizlabs

Remove story boards: see [How to remove storyboards from your project](https://www.weheartswift.com/remove-storyboard-from-project/).

[Your First iOS App: 100% Programmatically (Xcode 7.2, Swift 2.1)](https://medium.com/@danstepanov/your-first-ios-app-100-programmatically-xcode-7-2-swift-2-1-9946d09610c4)

[IB Free: Living Without Interface Builder and Loving It](https://www.raizlabs.com/dev/2016/08/ib-free-living-without-interface-builder/)

## Views

Subclasses of UIView: UILabel, UIImageView, UIButton, UITextField, UIWindow.

## Links

[Let's Build That App](http://letsbuildthatapp.com/)
