labels: Draft
        ML
created: 2017-04-02T23:32
modified: 2018-07-23T15:39
place: Phuket, Thailand
comments: true

# Machine learning

[TOC]

Machine learning is valuable because it lets us use computers to automate decision-making processes.

The basics of most machine learning:

- Start with a set of data that you know the answer to
- Train your machine learning algorithm on that data set, often known as the training set
- Get a set of data that you want to know the answer to, often known as the test set
- Pass that data through your trained algorithm and find the result

## Decision tree

## Random forest

A Swiss Army Knife of machine learning algorithms.

[sklearn RandomForestClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

### n_estimators

Default: 10

Number of trees in the forest.

Random forest does not overfit, and you can use as much trees as you want.

Number of trees between 64-128 trees. Min - 10.

### criterion

Default: 'gini'

Options:

- gini: gini impurity
- entropy: information gain

Gini impurity and Information Gain Entropy are pretty much the same.
Entropy might be a little slower to compute.

### max_depth

Default: None

The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.

Max depth is usually only a technical parameter to avoid recursion overflows while min sample in leaf is mainly for smoothing votes for regression.

The default values for the parameters controlling the size of the trees (e.g. max_depth, min_samples_leaf, etc.) lead to fully grown and unpruned trees which can potentially be very large on some data sets. To reduce memory consumption, the complexity and size of the trees should be controlled by setting those parameter values.

### max_features

Default: 'auto' (`sqrt(n_features)`)

The number of features to consider when looking for the best split.

### min_samples_split

Default: 2 (accepts float values for percentage)

When we require all of the samples at each node, the model cannot learn enough about the data. This is an underfitting case.

### min_samples_leaf

Default: 1

Increasing this value can cause underfitting.

### min_weight_fraction_leaf

Default: 0.0

### max_leaf_nodes

Default: None (unlimited number of leaf nodes)

### min_impurity_decrease

Default: 0.0

A node will be split if this split induces a decrease of the impurity greater than or equal to this value.

### bootstrap

Default: True

Whether bootstrap samples are used when building trees.

### oob_score

Default: False

Whether to use out-of-bag samples to estimate the generalization accuracy.

Out-of-bag (OOB) error, also called out-of-bag estimate, is a method of measuring the prediction error of random forests, boosted decision trees, and other machine learning models utilizing bootstrap aggregating (bagging) to sub-sample data samples used for training.

### n_jobs

Default: 1

The number of jobs to run in parallel for both fit and predict. If -1, then the number of jobs is set to the number of cores.

### random_state

Default: None (the random number generator is the RandomState instance used by `np.random`)

### warm_start

Default: False

When set to True, reuse the solution of the previous call to fit and add more estimators to the ensemble, otherwise, just fit a whole new forest.

### class_weight

Default: None (balanced_subsample)

## Reinforcement learning

Goal: Building systems that can adapt to their environments and learn from their experience.

Reinforcement learning is learning how to map situations to actions so that maximize reward signal.

Is not supervised learning, learns only by it's own interraction.

Has to both exploit and explore. Exploit - use what it knows in order to obtain reward. Explore - find and use better actions in future.

Subelements of a reinforcement learning system: a policy, a reward function, a value function, a model of the environment (optionally).

### Definitions

Works with late gratification.

Mouse in a maze:

- Agent - mouse
- Environment - maze
- State - current position (observations -> state)
- Action - left/right (changes state)
- Reward - cheese

Techniques:

- Deep Q learning

#### Q Learning

`Q(State[t], Action) = Reward[t] + DiscountFactor * Q(State[t + 1], OptimalAction)`

## Links

[Machine Learning With Random Forests and Decision Trees](https://www.amazon.com/Machine-Learning-Random-Forests-Decision-ebook/dp/B01JBL8YVK) by Scott Hartshorn
[In Depth: Parameter tuning for Random Forest](https://medium.com/@mohtedibf/in-depth-parameter-tuning-for-random-forest-d67bb7e920d)
Reinforcement Learning by Richard S. Sutton and Andrew G. Barto

### Courses

- [Machine Learning: Beginner Reinforcement Learning in Python](https://www.udemy.com/course/machine-learning-beginner-reinforcement-learning-in-python/)
