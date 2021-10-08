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

#### Part 5: Learning Curve for Linear Regression

- Fill in this function to return training errors in error_train and the cross validation errors in error_val.

```matlab
for i = 1: m
   subset_x = X(1: i, :);
   subset_y = y(1: i);
   theta = trainLinearReg(subset_x, subset_y, lambda);
   
   % for training set error, compute on the training subset
   error_train(i) = linearRegCostFunction(subset_x, subset_y, theta, 0); % set λ to 0
   % for cross validation error, compute over the entire cross validation set
   error_val(i) = linearRegCostFunction(Xval, yval, theta, 0);
end
```

#### Part 6: Feature Mapping for Polynomial Regression

- Given a vector X, return a matrix X_poly where the p-th column of X contains the values of X to the p-th power.

```matlab
m = size(X, 1);

for i = 1: m
    for j = 1:p
        X_poly(i, j) = X(i) .^j;
    end
end
```

#### Part 8: Validation for Selecting Lambda

- Fill in this function to return training errors in error_train and the validation errors in error_val.

```matlab
for i = 1: length(lambda_vec)
    % take each lambda and test
    lambda = lambda_vec(i);
    theta = trainLinearReg(X, y, lambda);
    
    error_train(i) = linearRegCostFunction(X, y, theta, 0); % set λ to 0
    error_val(i) = linearRegCostFunction(Xval, yval, theta, 0);
```

