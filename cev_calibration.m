
data = xlsread('SSE.xlsx',2);
price = data(:,6);
% ave = mean(price2ret(price));
% vol = std(price2ret(price));
dt = 1/252;
x0 = [0.1, 0.2, 0.5];
lb = [-1,0,0];
ub = [1,0.6,2];
y = @(x) (price(1:end-1)-price(2:end) - x(1)*price(2:end)*dt)/x(2)./(price(2:end).^x(3))/sqrt(dt);
[x, resnorm, residals, exitflag] = lsqnonlin(y, x0, lb, ub);
dwt = randn(100,1);
St = price(end) + x(1)*price(end)*dt + x(2)*price(end)^x(3).*dwt*sqrt(dt);
temp = x(2)*price(end)^x(3)*sqrt(dt);
