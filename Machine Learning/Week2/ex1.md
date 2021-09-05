#### Part 1: Basic Function

- Modify warmUpExercise.m to return a 5 x 5 identity matrix

```matlab
A = eye(5);
```



#### Part 2: Plotting

- Plot the training data into a figure in plotData.m

```matlab
data = load('ex1data1.txt')
x = data(:, 1);y = data(:,2)
m = length(y)

plot(x, y, 'rx', 'MarkerSize', 10);
ylabel('Profit in $10,000s')
xlabel('Population of City in 10,000s')
```



#### Part 3: Cost and Gradient descent

- complete the code in the file computeCost.m, which is a function that computes J(θ)

```matlab
J = sum(((X * theta) - y).^2) / (2 * m);
```

-  Perform a single gradient step on the parameter vector theta in gradientDescent.m

```matlab
for iter = 1:num_iters
    theta = theta - alpha * (1 / m) * (X'* ((X * theta) - y) );
```

