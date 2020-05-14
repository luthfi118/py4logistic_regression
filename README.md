# py4logistic-regression

Logistic Regression Python Library

## Getting Started

This project is simply implementation of logistic regression algorithm in python programming language.

### Prerequisites

Numpy


### Installing

The easiest way to install py4logistic-regression is using pip

```
pip install py4logistic-regression
```

### Usage
There is 2 public method of Logistic Regression class. It is learn and predict method, learn method takes 5 argument namely x_train, t_train, alpha, and epoch. It is the training data, it's label, learning rate, and number of iteration respectively. predict method takes 1 argument namely x_test. It is the data to be predicted
```
from py4logistic_regression.regression import logistic_regression
x_train = [[0,0],[0,1],[1,0],[1,1]]
t_train = [0,0,0,1]
classifier = logistic_regression()
classifier.learn(x_train,t_train,0.1,50)
x_test = [[0.02,0.25],[0.97,0.89]]
y = classifier.predict(x_test)
```
