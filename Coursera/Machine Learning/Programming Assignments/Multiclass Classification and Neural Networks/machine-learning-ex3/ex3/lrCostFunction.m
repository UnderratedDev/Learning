function [J, grad] = lrCostFunction(theta, X, y, lambda)
%LRCOSTFUNCTION Compute cost and gradient for logistic regression with 
%regularization
%   J = LRCOSTFUNCTION(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Hint: The computation of the cost function and gradients can be
%       efficiently vectorized. For example, consider the computation
%
%           sigmoid(X * theta)
%
%       Each row of the resulting matrix will contain the value of the
%       prediction for that example. You can make use of this to vectorize
%       the cost function and gradient computations. 
%
% Hint: When computing the gradient of the regularized cost function, 
%       there're many possible vectorized solutions, but one solution
%       looks like:
%           grad = (unregularized gradient for logistic regression)
%           temp = theta; 
%           temp(1) = 0;   % because we don't add anything for j = 0  
%           grad = grad + YOUR_CODE_HERE (using the temp variable)
%

predictions = sigmoid (X * theta); % calculate predictions matrix
left        = -y' * log (predictions); % calculate left hand side of cost
right       = (1 - y') * log (1 - predictions); % calculate right hand side of cost
thetaZero   = theta; % use previous theta
thetaZero(1) = 0; % must be zero as when j = 0, calculations with j = 0 should not affect output
regularizedCost   = (lambda / (2 * m)) * sum(thetaZero .^ 2); % regularized cost part
regularizedGrad  = lambda / m * thetaZero; % regularized gradient part

J = (1 / m) * (left - right) + regularizedCost; % calculate regularized cost

grad = ((1 / m) * (X' * (predictions - y))); % calculate unregularized gradient

grad = grad + regularizedGrad; % add regularized gradient



% =============================================================

grad = grad(:);

end
