function mlikelihood = SVCalibration(ret, theta)
%%
delta = 0.01;
x = delta:delta:0.5;
% theta = [-0.3, 0.95, 0.2, 0.1];
alpha = theta(1);
beta = theta(2);
sigmav = theta(3);
rho = theta(4);
x0 = 0.2;
xi = repmat(x',1,length(x));
xj = repmat(x,length(x),1);

%%
yt = ret(1);
u0 = exp(-(xi-alpha-beta*x0)^2/2/sigmav^2) / sqrt(2*pi*sigmav^2);
q = delta * exp(-(xi-alpha-beta*xj)^2/2/sigmav^2) / sqrt(2*pi*sigmav^2);
mu = exp(xi/2) .* rho .* (xi-alpha-beta*xj)/sigmav;
pt = q * u0;
rt = exp(-(yt - mu).^2./(2*exp(xi)*(1-rho^2))) ./ sqrt(2*pi*exp(xi)*(1-rho^2));
for i = 2:length(ret)
    yt = ret(i);
    pt = q .* repmat(sum(rt.*pt),length(x),1) / sum(sum(rt.*pt));
    rt = exp(-(yt - mu).^2./(2*exp(xi)*(1-rho^2))) ./ sqrt(2*pi*exp(xi)*(1-rho^2));
end


mlikelihood = -sum(sum(rt*pt));

