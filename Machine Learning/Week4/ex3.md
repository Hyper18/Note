### ex3.m 

#### Part 1: Loading and Visualizing Data

- Load Training Data

```matlab
load('ex3data1.mat'); % training data stored in arrays X, y
```

- Visualization

![image-20210910203101080](C:\Users\Vincent\AppData\Roaming\Typora\typora-user-images\image-20210910203101080.png)

#### Part 2a: Vectorize Logistic Regression

- Compute the cost of a particular choice of theta. You should set J to the cost.
  Compute the partial derivatives and set grad to the partial derivatives of the cost w.r.t. each parameter in theta

```matlab
J = (1 / m) * sum(-y .* log(sigmoid(X * theta)) - (1 - y) .* log(1 - sigmoid(X * theta))) + (lambda / (2 * m)) * sum(theta(2:size(theta)) .^2);

temp = theta;
temp(1) = 0;
grad = (1 / m) * (X' * (sigmoid(X * theta) - y)) + (lambda / m) * temp;
```

#### Part 2b: One-vs-All Training

- You should complete the following code to train num_labels logistic regression classifiers with regularization parameter lambda.

```matlab
% Set Initial theta
initial_theta = zeros(n + 1, 1);
% Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 50);
for c = 1: num_labels
      all_theta(c, :) = fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)), initial_theta, options);
```

#### Part 3: Predict for One-Vs-All

- Complete the following code to make predictions using your learned logistic regression parameters (one-vs-all).

```matlab
predict = sigmoid(X * all_theta');
[~,p] = max(predict, [], 2); % ~ means ignore this 1st parameter output
```

### ex3_nn.m

- Complete the following code to make predictions using your learned neural network.

```matlab
X = [ones(m, 1) X];
z1 = sigmoid(X * Theta1');
z1 = [ones(m, 1) z1];
z2 = sigmoid(z1 * Theta2');

[~, p] = max(z2, [], 2);
```