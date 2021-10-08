### ex6.m

#### Part 2: Training Linear SVM

- Try different value of C, sp. changing the  value of C from 1 to 100 in ex6.m makes the classification work out correctly

#### Part 3: Implementing Gaussian Kernel

- Fill in this function to return the similarity between x1 and x2 computed using a Gaussian kernel with bandwidth sigma

```matlab
sim = exp(-sum((x1-x2).^2) / (2*(sigma^2)))
```

#### Part 7: Training SVM with RBF Kernel (Dataset 3)

- Fill in this function to return the optimal C and sigma learning parameters found using the cross validation set

```matlab
val = [0.01 0.03 0.1 0.3 1 3 10 30];
min = 1;

for i = 1:8
    for j = 1:8
        C_test = val(i);
        sigma_test = val(j);
        model = svmTrain(X, y, C_test, @(x1, x2) gaussianKernel(x1, x2, sigma_test));
        predictions = svmPredict(model, Xval);
        % compute the prediction error
        err = mean(double(predictions ~= yval));
        if err < min
           C = C_test;
           sigma = sigma_test;
           min = err;
        end
    end
end
```

### ex6_spam.m

#### Part 1: Email Preprocessing

- Fill in this function to add the index of str to word_indices if it is in the vocabulary

```matlab
for i = 1 : length(vocabList)
    % compare two strings (str1 and str2)
    if(strcmp(vocabList{i}, str) == 1)
        word_indices = [word_indices;i];
        break;
    end
end
```

#### Part 2: Feature Extraction

- Fill in this function to return a feature vector for the  given email (word_indices)

```matlab
for i = 1 : length(word_indices)
   x(word_indices(i)) = 1; 
end
```

​	or a better and simpler approach

```matlab
x(word_indices(i)) = 1;
```

