### ex8.m

#### Part 2: Estimate the dataset statistics

- Compute the mean of the data and the variances

```matlab
mu = sum(X) / m;
sigma2 = sum((X - repmat(mu, m, 1)).^2) / m; % X - 307 * 1 matrix
```

####  Part 3: Find Outliers

- Compute the F1 score of choosing epsilon as the threshold and place the value in F1

```matlab
% define the anomolous condition
    condition = pval < epsilon;
    % sum up to get each parameter
    fp = sum((condition == 1) & (yval == 0));
    fn = sum((condition == 0) & (yval == 1));
    tp = sum((condition == 1) & (yval == 1));
    % define precision and recall
    prec = tp / (tp + fp);
    rec = tp / (tp + fn);
    % use F1 score to estimate its performance
    F1 = (2 * prec * rec) / (prec + rec);
```

### ex8_cofi.m

```matlab
% compute cost function
J = sum(sum((((X * Theta' - Y) .* R) .^ 2))) / 2;
% compute gradient
X_grad = ((X * Theta' - Y) .* R) * Theta;
Theta_grad = ((X * Theta' - Y) .* R)' * X;
% compute cost function with regularization
J = J + lambda / 2 * ((sum(sum(Theta .^ 2)) + sum(sum(X .^ 2))));
% compute gradient with regularization
X_grad = X_grad + lambda * X;
Theta_grad = Theta_grad + lambda * Theta;
```

