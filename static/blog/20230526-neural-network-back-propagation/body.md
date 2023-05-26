A feed-forward neural network of $n$ layers is a type of non-linear model
where the model parameters are matrices
$$
A^{(0)}, A^{(1)}, \ldots, A^{(n-1)}
$$
which iteratively relate the model inputs $\mathbf{x}$ to the model 
predictions $\mathbf{\hat{y}}$ by
$$
\mathbf{\hat{y}}^{(k)} = \sigma^{(k-1)}
\left( \mathbf{\hat{y}}^{(k-1)} A^{(k-1)} \right)
$$
where 
$$
\begin{aligned}
\mathbf{\hat{y}}^{(0)} &= \mathbf{x} \\
\mathbf{\hat{y}}^{(n)} &= \mathbf{\hat{y}} \\
\end{aligned}
$$
and the _activation_ $\sigma^{(k)}$ is a specified (typically
non-linear) scalar function that acts elementwise on the matrix product  
$\mathbf{\hat{y}}^{(k-1)} A^{(k-1)}$. We call the $\mathbf{\hat{y}}^{(k)}$
the model outputs at layer $k$; the feed-forward neural net thereby
defines model outputs at layer $k$ in terms of model outputs at layer $k-1$.

Regarding the activation functions $\sigma^{(k)}$ at layer $k$, 
a typical feed-forward neural net might use the non-linear function 
$$
\sigma^{(k)}(z) = \tanh(z)
$$
for all $k = 0,1,\ldots (n-2)$, and
$$
\sigma^{(n-1)}(z) = z
$$
for the final layer. (If the final activation were also $\tanh$,
the net output would be bounded by the range of $\tanh$ to $(-1,1)$.)

_Model training_ is the process of optimising the $A^{(k)}$ so that
for a given set of model inputs $\mathbf{x}_i$ and model targets 
$\mathbf{y}_i$ with $i = 1,2,\ldots,N$, the model predictions 
$\mathbf{\hat{y}}_i$ minimise the _loss_
$$
S = \frac{1}{2} \sum_i \left( \mathbf{y}_i - \mathbf{\hat{y}}_i \right)^2 .
$$
Typically, some form of the gradient descent method is used to
iteratively improve the model parameters $A^{(k)}$ towards an optimum
of $S$. This requires the gradient of $S$ with respect to each of the 
$A^{(k)}$. We start with $A^{(n-1)}$ and evaluate
$$
\begin{aligned}
-\frac{\partial S}{\partial A^{(n-1)}} 
&= \left( \mathbf{y} - \mathbf{\hat{y}}^{(n)} \right) 
\frac{\partial \mathbf{\hat{y}}^{(n)}}{\partial A^{(n-1)}} \\
&= \left( \mathbf{y} - \mathbf{\hat{y}}^{(n)} \right) 
\sigma^{(n-1) \prime} \left( \mathbf{\hat{y}}^{(n-1)} A^{(n-1)} \right)
\mathbf{\hat{y}}^{(n-1)},
\end{aligned}
$$
making indices and summation over $i$ implicit. For the deeper levels 
of the network, we take advantage of the iterative definition of the network
to write the derivative as a chain-rule product
$$
-\frac{\partial S}{\partial A^{(n-k-1)}} 
= \left( \mathbf{y} - \mathbf{\hat{y}}^{(n)} \right) 
\frac{\partial \mathbf{\hat{y}}^{(n)}}{\partial \mathbf{\hat{y}}^{(n-1)}}
\frac{\partial \mathbf{\hat{y}}^{(n-1)}}{\partial \mathbf{\hat{y}}^{(n-2)}}
\ldots
\frac{\partial \mathbf{\hat{y}}^{(n-k+1)}}{\partial \mathbf{\hat{y}}^{(n-k)}}
\frac{\partial \mathbf{\hat{y}}^{(n-k)}}{\partial A^{(n-k-1)}} .
$$
Evaluating each factor in the product,
$$
\begin{aligned}
-\frac{\partial S}{\partial A^{(n-k-1)}} 
= \left( \mathbf{y} - \mathbf{\hat{y}}^{(n)} \right)
&\sigma^{(n-1) \prime}
\left( \mathbf{\hat{y}}^{(n-1)} A^{(n-1)} \right) A^{(n-1)} \\
&\sigma^{(n-2) \prime}
\left( \mathbf{\hat{y}}^{(n-2)} A^{(n-2)} \right) A^{(n-2)} \\
&\qquad \ldots \\
&\sigma^{(n-k) \prime}
\left( \mathbf{\hat{y}}^{(n-k)} A^{(n-k)} \right) A^{(n-k)} \\
&\sigma^{(n-k-1) \prime}
\left( \mathbf{\hat{y}}^{(n-k-1)} A^{(n-k-1)} \right) \mathbf{\hat{y}}^{(n-k-1)} .
\end{aligned}
$$
This expression suggests that the gradients be computed in reverse
order, iteratively constructing the intermediate quantities
$$
\begin{aligned}
P^{(n-1)} &= \left( \mathbf{y} - \mathbf{\hat{y}}^{(n)} \right)
\sigma^{(n-1) \prime} \left( \mathbf{\hat{y}}^{(n-1)} A^{(n-1)} \right) \\
P^{(n-k-1)} &= P^{(n-k)} A^{(n-k)}
\sigma^{(n-k-1) \prime} \left( \mathbf{\hat{y}}^{(n-k-1)} A^{(n-k-1)} \right)
\end{aligned}
$$
and putting
$$
-\frac{\partial S}{\partial A^{(n-k)}} 
= P^{(n-k)} \mathbf{\hat{y}}^{(n-k)} .
$$

To see this in action, consider a two-layer model with tanh activation on
both layers.

    class nn_model:
        def __init__( self, m0, m1, m2  ):
            self.m0 = m0
            self.m1 = m1
            self.m2 = m2
    
            self.a0 = np.random.normal( size = ( self.m0, self.m1 ) )
            self.a1 = np.random.normal( size = ( self.m1, self.m2 ) )
    
        def predict( self, x ):
            ## Forward pass only
            z0 = x
            z1 = np.tanh( z0 @ self.a0 )
            z2 = np.tanh( z1 @ self.a1 )
            return z2
    
        def loss( self, x, y ):
            yhat = self.predict( x )
            return np.sum( ( y - yhat ) ** 2 ) / y.size
    
        def grad( self, x, y ):
            ## Forward pass
            z0 = x
            z1 = np.tanh( z0 @ self.a0 )
            z2 = np.tanh( z1 @ self.a1 )
        
            ## Backward pass
            p1 = ( y - z2 ) / np.cosh( z1 @ self.a1 ) ** 2
            p0 = p1 @ np.transpose( self.a1 ) / np.cosh( z0 @ self.a0 ) ** 2
        
            g1 = -np.transpose( z1 ) @ p1
            g0 = -np.transpose( z0 ) @ p0
            return g0, g1
    
        def iterate( self, x, y, step ):
            ( g0, g1 ) = self.grad( x, y )
            self.a0 -= step * g0
            self.a1 -= step * g1
            return

We can set up some toy data using a random normal design matrix `x`, choosing
a random neural network model and using it to create some targets `y`.

    n = 100000
    m0 = 4
    m1 = 3
    m2 = 2

    x = np.random.normal( size = ( n, m0 ) )
    true_nn = nn_model( m0, m1, m2 )
    y = true_nn.predict( x ) + np.random.normal( size = ( n, m2 ) )

By construction, the loss on `true_nn` on the data sample `(x, y)`
is the sample variance of 200k independent draws from a random normal
distribution, and is therefore very close to 1.0:

    true_nn.loss( x, y )
    0.9984112413952128

We now choose another random neural net as a starting point for
back-propagation over 200 iterations.

    nn = nn_model( m0, m1, m2 )
    loss = np.zeros( shape = 200 )
    step = 1.0e-5

    for j in range( len( loss ) ):
        loss[j] = nn.loss( x, y )
        nn.iterate( x, y, step )

We also construct the zero model and an OLS model for comparison.

    zero_loss = np.sum( y ** 2 ) / y.size

    ols = sm.OLS( y, x ).fit()
    yhat = ols.predict( x )
    ols_loss = np.sum( ( y - yhat ) **2 ) / y.size


We can then plot the loss for the neural net over each iteration,
together with the loss for the zero, OLS and true model. It can
be seen from the chart that back propagation has been successful
and the neural net has been trained so that its output is almost
equivalent to the true model. The neural net strongly outperforms
the zero model and OLS model on this toy dataset.

![Back-propagation in action.](/static/blog/20230526-neural-network-back-propagation/backprop-loss.png)
