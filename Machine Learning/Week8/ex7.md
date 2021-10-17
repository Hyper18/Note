### ex7.m

#### Part 1: Find Closest Centroids

- Go over every example, find its closest centroid, and store the index inside idx at the appropriate location

```matlab
for i = 1: size(X,1) % query from 1 to 300
    d = zeros(1, K); % distance: 1*3 matrix
    for j = 1: K
        d(1, j) = sqrt(sum(power(X(i, :) - centroids(j, :), 2))); % use Euclidean Distance, centroids: 3*2 matrix
    end
    [~, idx(i)] = min(d); % get the 2nd parameter from distance matrix only
end
```

#### Part 2: Compute Means

- Go over every centroid and compute mean of all points that belong to it

```matlab
for i = 1 : K
    % find all the points that is nearest to No.i centroid, then count their
    % mean
    points = X(idx==i, :);
    centroids(i, :) = mean(points);
end
```

### ex7 pca.m

#### Part 2: Principal Component Analysis

- You should first compute the covariance matrix. Then, you should use the "svd" function to compute the eigenvectors and eigenvalues of the covariance matrix

```matlab
% compute sigma
sigma = (X' * X) / m;
% use SVD to compute the eigenvectors and eigenvalues of the covariance matrix
[U, S, V] = svd(sigma);
```

#### Part 3: Dimension Reduction

- Compute the projection of the data using only the top K  eigenvectors in U (first K columns)

```matlab
% using only the top K eigenvectors in U
U_reduce = U(:, 1:K);
% implementing PCA
for i = 1: size(X, 1)
    x = X(i, :)';
    for k = 1: K
        projection_k = x' * U_reduce;
        Z(i, :) = projection_k;
    end
end
```

- Compute the approximation of the data by projecting back onto the original space using the top K eigenvectors in U

```matlab
% implementing PCA
for i = 1: size(Z, 1)
    v = Z(i, :)';
    for j = 1: size(U, 1)
        recovered_j = v' * U(:, 1:K)';
        % 2D -> 1D
        X_rec(i, :) = recovered_j;
    end
end
```

