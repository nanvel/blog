labels: Draft
created: 2023-09-23T11:55
modified: 2023-09-23T11:55
place: Bangkok, Thailand
comments: false

# eXtreme Programming

[TOC]

[eXtreme Programming](http://www.extremeprogramming.org/) (XP) is a type of agile software development.

Beneficial elements of traditional software engineering practices are taken to "extreme" levels.

Developed by [Kent Beck](https://en.wikipedia.org/wiki/Kent_Beck) during his work on the Chrysler Comprehensive Compensation System payroll project (became the project leader in March 1996). He wrote a book on the methodology ([Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change-ebook/dp/B00N1ZN6C0/), published in October 1999).

Progamming vs eXtreme Programming: my work in a garden vs master gardener.

XP teams produce quality software at a sustainable pace.

XP paradigm: stay aware, adapt, change.
Everything in software changes: requirements, design, business, technology, team, team members.
The problem doesn't change, because change is going to happen; the problem, rather, is our inability to cope with change.

## Values -> (principles) -> practices

Concentrate on practices and stop thinkings, this is why values and principles.

Values:
- Communication
- Simplicity
- Feedback
- Courage
- Respect

Principles:
- Humanity
- Economics
- Mutual Benefit
- Self-Similarity
- Improvement
- Diversity
- Reflection
- Flow
- Opportunity
- Redundancy
- Failure
- Quality
- Baby Steps
- Accepted Responsibility

Each practice is an experiment in improving effectivenes, comunication, confidence, and productivity.

Practices:
- Sit Together
- Whole Team
- Informative Workspace
- Energized Work
- Pair Programming
- Code Reviews
- Stories
- Weekly Cycle
- Quarterly Cycle
- Slack
- Ten-Minute Build
- Continuous Integration
- Test-First Programming
- Incremental Design
- Delaying Decisions
- Code Simplicity and Clarity

Activities:
- Coding
- Testing
- Listening
- Designing

Goals:
- Software quality
- Responsiveness to changing requirements

## Addressing the risks

Spike solution to reduce risk.

Addressing the risks:
- short release cycles (with one week iterations)
- implementing highest priority features first
- less to go wrong before release when the value of software is greatest
- ensure quality baseline with tests, always keeps system in deployable condition
- problems are not allowed to accumulate
- defect rate: programmers written tests + customer feature tests
- business-oriented people are first class members of the team, specifications are being continuously refined during development
- programmers accept responsibility for estimating and completing theit own work (not being asked to do impossible)
- human contact, reduce loneliness
- new team members are encouraged to gradually accept more and more responsibility and are assisted along
- assumes that you see yourself as a part of a team
- assumes that you want to grow, to improve skills, improve relationships
- assumes you are willing to make changes to meet those goals

### Cost of change

The automated tests, the continual practice of improving the design, and the explicit social process all contribute to keep the cost of change low.

### Testing

Response to defect - write an automated test that demonstrates the defect.

### Defects

Until the team has developped a sense of collective responsibility, no one is responsible and quality will deteriorate.

5 Why by Taiichi Ohno.

## Design

Keep the design investment in proportion to the needs of the team of the system so far.
The question is not whether or not to design, the question is when to design. Incremental design suggests that the most effective time to design is in the light of experience.

In software development "perfect" is a verb, not an adjective.
Excelence in software development through improvement.

XP pushes incrementalism of design to the limit, sugegsting that projects run more smoothly if design is part of daily business.

BDUF (big design upfront) -> LDUF (little design upfront).

For some projects. only experience (not instinct or thought) will result in enough understanding to produce a good enough design.

## Development

### Quality

Time and cost are generally set outside the project. That leaves quality as the only variable you can manipulate.

Simplicity: to make system simple today is hard, when have to regain simplicuty later - must find a way from where you are to where you want to be.

Pushing quality higher often results in faster delivery; while lowering quality standards often results in later, less predictable delivery.
Quality isn't a purely economic factor. People need to do work they are proud of.

If the people who need to work with it don't understand it, it isn't simple for them.
Less, code, tests, documents.

The greatest waste is the waste of overproduction.
Taiichi Ohno (TPS)
Waste: fat requirements, elaborate architecture that never used, code not being integrated for months, documentation no one reads until it becomes irrelevant or misleading.

Simplicity:
- look what can be removed, simplified, become more readable
- be cautios to adding new advanced technologies
- readable top to bottom as a poem

Build something simple is more difficult than build something complicated.
Maintaining simple is easy and maintaining complicated is difficult.

High quality:
- high quality is cheaper
- high quality if more fun and satisfaction

### Testing

Automated tests break the stress cycle (stress <-> mistakes).

Test first programming:
- stating explicitly and objectively what the program is supposed to do
- coupling and cohession, if it is hard to write a test - a signal of design problem. Losely coupled, highly cohessive code is easy to test
- trust, it is hard to trust the author of code without tests
- rhythm - it is easy to get lost, clearer what to do next: test-code-refator-repeat

In XP, test and code can be written in either orders.

Running tests gives the team a valid basis for confidence as it moves quickly in unanticipated directions.

Static analysis tools can be used with test-first style.
Static verification is a valid form of double-checking, particularly for defects that are hard to reproduce dynamically.

Tests -> Immediate feedback -> satisfaction.

### Mutualy beneficial

XP solves the communication with-the-future problem in mutually beneficial ways (benefit me now, me/others later, my customers):
- tests (design and implement better today)
- refactor (remove accidental complexity, satisfaction, fewer defects, easier to understand for others)
- use names for coherent and explicit set of metaphors

### Pair programming

Pair programming:
- keep each other on task
- brainstorm refinment to the system
- clarify ideas
- take initiative when partner is stuck
- hold each other accountable to the team's practices

Pair programming - performance is similar to two people working independently.

## Team

What matters is not how any given given person in team behaves as much as how the individuals behave as part of a team and as part of an organization.
Example: coding styles, which libraries to use, etc. Are willing to work towards better solution, discuss?
Individual freedom at all costs don't help the team to succeed.
Everyone focus on what is important to the team: comunication, simplicity, feedback, courage, respect.

Valuable employees in XP:
- act respectful
- play well with others
- take initiative
- deliver on their commitments

Courage: when problems arise in developments, most often someone already knows the solution, but that knowledge doesn't get through t someone with the power to make the change.

If members of a team don't care about a project, nothing can save it.

The team's may meet your own long-term individual goals, so are worth some amoung of sacrifice.
Always sacrificing your needs for the team's doesn't work.

Diversity: two ides about a design present an opportunity, not a problem.

What if conflict? Every team has conflict. The question is whther they resolve it productively.

Analyze why succeeded or failed. Don't try to hide mistakes, expese them and learn from them.

To reach excellence, problems need to turn into opportunities for learning and improvement, not just survival.

Responsibility can not be assigned; it only can be accepted.
With responsibility comes authority.
Assigned -> estimate the work.
Implement story -> responsible for design, implementation and testing.

Keep effective teams together.

By mostly keeping teams together and yet encouraging a reasonable amount of rotation, the organization gets the benefits of both stable teams and of consistently spread knowledge and experience.
When grows capability, keep load constant and reduce size - frees people to form new teams. If has too few members - merge with another too small team.

Find a workspace that is effective for your team:
- good food
- environment
- comfort
- etc.
With a little encouragement, teams can shape their own space.
Software development is a game of insight, and insight comes to the prepared, rested, relaxed mind.

Toyota Production System: make the quality of line good enough that there is no need for downstream quality assurance. This implies that everyone is responsible for quality.

Working together can accomplish more that the sum of its members' reparate efforts.

Courage: tell the truth about progress and estimates, throw away code if doesn't work, change if found a way to improve it, fix if you found a problem, try out new things if think they could work better.

It is about being open about what we are capable of doing and then doing it. And, allowing and expecting others to do the same. It is about getting past our adolescent surety that "I know better than everyone else and all I need is to be left alone to be the greatest." It is about finding our adult place in the larger world, finding our place in the community including the realm of business/work. It is about the process of becoming more of our best selves and in the process our best as developers.

It is not my job to "manage" someone else's expectations. It is their job to manage their own expectations. It is my job to do my best and to communicate clearly.
If we give weekly updates, then customers can manage their expectations.

Fully appreciating yourself for total effort today.

## Other

Flat management structure (managers, customers, and developers are all equal partners in a collaborative team).

Expecting changes: time passes and the problem is better understood -> changes.

Put in all the design you can before you begin implementation because you'll never get another chance (study was showing that fixing defect rose exponentially with time).

Architects: look for and execute large scale refactorings, write system-level tests that stres the achitecture, and implement stories.
Architects sign up for programming tasks just like any programmer. However, they are also on the lookup for big changes that have big payoffs.

In ten years the pendulum has swung from 'design everything' to 'design nothing'.
McConnell

Scale software development:
- number of people
- investment
- size of the entire organization
- time
- problem complexity
- solution complexity
- consequence of failure

When faced with a big problem:
- turn the problem into smalled problems
- apply simple solutions
- apply complex solutions if any problem is left

Write Rosetta document before shutting down the project. A brief guide to future maintainers tells how to run the build and test process, ...


You can learn them from someone who has made all the mistakes or you can make the mistakes yourself.

It is worse to fail with XP team that to succeed with a pure waterfall team.


There is no improvement without first improving myself.

Apply some of the practices:
- Testing early, often and aumated.
- Incremental design - invest in the design every day, and keep the API stable at the same time.
- Daily deployment - deploy daily and develop on top of the deployed code to catch problems early.
- Customer involvement - continuous feedback
- Continuous integration - night builds, validates integration.
- Short development cycles.

Making a change in a building later - cost much higher than at the planning phase.
Building higher quolity building cost more. Building higher quolity software cost less.

Inclusivity and divercity.


"It is about minimalism and incrementalism, which are especially usefu principles when tackling complex problems that require a balance of creativity and discipline."
Michael A. Cusumano

"My only beef is that our profession has gotten to a point where such common-sense ideas are labeled extreme."
Lou Mazzuccelli

Develop better software in less time and less money.


Practices that seemed impossible extreme five years ago, when the first edition of this book was published, are now common. Five years from now the practices in this book will probably seem conservative.

Being humble and respect others and learn from others.

XP is a style of software development focusing on excelent application of programming techniques, clear communication, and teamwork which allows us to accomplish things we previously could not even imagine.

XP is also productive, produces high-quality software, and it is a lot of fun to execute.

## Links

[Lecture 24: eXtreme Programming - Richard Buckland](https://www.youtube.com/watch?v=XP4o0ArkP4s) at UNSW eLearning
[Extreme Programming 20 years later by Kent Beck](https://www.youtube.com/watch?v=cGuTmOUdFbo) at InstitutLeanFrance
[Extreme Programming Explained](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change-ebook/dp/B00N1ZN6C0/) by Kent Beckm, Cynthia Andres
