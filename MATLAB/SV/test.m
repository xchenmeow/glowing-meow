
price = xlsread('SSE.xlsx',2);
ret = price2ret(flipud(price(:,6)));
ret = ret(end-100:end);
lb = [-10, 0.2, 0.01, -0.99];
ub = [10, 0.99, 1, 0.99];
theta0 = [-0.01, 0.95, 0.2, 0.1];
[theta, fval, exitflag] = fminsearch(@(theta) SVCalibration(ret, theta), theta0);