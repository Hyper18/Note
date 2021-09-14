####  Part 2: Regularized Linear Regression Cost 

- Compute the cost and gradient of regularized linear regression for a particular choice of theta.

```matlab
% cost function
J = 1 / (2 * m) * (X * theta - y)' * (X * theta - y);
J = J + lambda / (2 * m) * (theta(2:end)' * (theta(2:end)));

% for j = 0
theta_temp = theta;
theta_temp(1) = 0;
% for j = 1
grad = (1 / m) * (X * theta - y)' * X + (lambda / m) * theta_temp';
```

#### Part 4: Train Linear Regression

- In this part, we set regularization parameter λ to zero. 
  - Because our current implementation of linear regression is trying to fit a 2-dimensional θ, regularization will not be incredibly helpful for a θ of such low dimension.

```matlab
% Initialize Theta
initial_theta = zeros(size(X, 2), 1); 

% Create "short hand" for the cost function to be minimized
costFunction = @(t) linearRegCostFunction(X, y, t, lambda);

% Now, costFunction is a function that takes in only one argument
options = optimset('MaxIter', 200, 'GradObj', 'on');

% Minimize using fmincg
theta = fmincg(costFunction, initial_theta, options);
```