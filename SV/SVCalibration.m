function mlikelihood = SVCalibration(ret, theta)
% reference: Nonlinear Filtering for Stochastic Volatiliy Models with Heavy
%   Tails and Leverage by AE Clements, SI White.
% Calibrate log-AR(1) model. 
% input: return time series(last is the latest), parameters to calibrate
% output: minus likelihood function

%%
delta = 0.005;
sigma = 0.1:delta:0.5;
x = log(sigma.^2);
alpha = theta(1);
beta = theta(2);
sigmav = theta(3);
rho = theta(4);
x0 = log(0.2^2);
xi = repmat(x',1,length(x));
xj = repmat(x,length(x),1);
sigmai = repmat(sigma',1,length(x));
sigmaj = repmat(sigma,length(x),1);
%%
yt = ret(1);
u0 = exp(-(xi-alpha-beta*x0).^2/2/sigmav^2) / sqrt(2*pi*sigmav^2);
q = exp(-(xi-alpha-beta*xj).^2/2/sigmav^2) / sqrt(2*pi*sigmav^2);
mu = exp(xi/2) .* rho .* (xi-alpha-beta*xj)/sigmav;
pt = q .* u0;
rt = exp(-(yt - mu).^2./(2*exp(xi)*(1-rho^2))) ./ sqrt(2*pi*exp(xi)*(1-rho^2));
for i = 2:length(ret)
    yt = ret(i);
    pt = q .* repmat(sum(rt.*pt./sigmaj,2),1,length(x))*delta / sum(sum(rt.*pt./sigmai./sigmaj))/2/delta^2;
    rt = exp(-(yt - mu).^2./(2*exp(xi)*(1-rho^2))) ./ sqrt(2*pi*exp(xi)*(1-rho^2));
end


mlikelihood = -sum(sum(rt.*pt./sigmai./sigmaj))*4*delta^2;

