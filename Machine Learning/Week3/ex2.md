### ex2.m 

#### Part 1: Plotting

- Plot the positive and negative examples on a 2D plot, using the option 'k+' for the positive examples and 'ko' for the negative examples

```matlab
positive = find(y == 1); negative = find(y == 0);
plot(X(positive, 1), X(positive, 2), 'k+','LineWidth', 1.2, 'MarkerSize', 8);
plot(X(negative, 1), X(negative, 2), 'ko','MarkerFaceColor', 'g', 'MarkerSize', 8);
```

#### Part 2: Compute Cost and Gradient

- Compute the sigmoid of each value of z (z can be a matrix, vector or scalar)

```matlab
% Y = exp(X) 为数组 X 中的每个元素返回指数 e^x
g = 1 ./ (1 + exp(1) .^ (-z));
```

- Compute the cost of a particular choice of theta. You should set J to the cost

```matlab
J = (1 / m) * sum(
	-y .* log(sigmoid(X * theta)) - (1 - y) .* log(1 - sigmoid(X * theta
)));
```

- Compute the partial derivatives and set grad to the partial derivatives of the cost w.r.t. each parameter in theta

```matlab
for j = 1:size(theta)
    grad(j) = (1 / m) * sum((sigmoid(X * theta) - y) .* X(:, j));
```

#### Part 3: Optimizing using fminunc

![image-20210905193014755](C:\Users\Vincent\AppData\Roaming\Typora\typora-user-images\image-20210905193014755.png)

#### Part 4: Predict and Accuracies

-  Complete the following code to make predictions using your learned logistic regression parameters. You should set p to a vector of 0's and 1's

```matlab
p = sigmoid(X * theta) >= 0.5;
```



### ex2_reg.m

#### Part 1: Regularized Logistic Regression

- Compute the cost of a particular choice of theta. You should set J to the cost
  - tip: In Octave/MATLAB, recall that indexing **starts from 1**, hence, you should not be regularizing the theta(1) parameter (which corresponds to θ0) in the code

```matlab
J = (1 / m) * sum(-y .* log(sigmoid(X * theta)) - (1 - y) .* log(1 - sigmoid(X * theta))) + (lambda / (2 * m)) * sum(theta(2:size(theta)) .^2);
```

- Compute the partial derivatives and set grad to the partial derivatives of the cost w.r.t. each parameter in theta

```matlab
grad(1) = sum((sigmoid(X * theta) - y) .* X(:, 1)) / m;
for j = 2 : size(theta)
    grad(j) = sum((sigmoid(X * theta) - y) .* X(:, j)) / m + (lambda / m) * theta(j);
```
