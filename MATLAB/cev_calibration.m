function [x,error] = cev_calibration(price, N)
% cev_calibration calibrate the local vol CEV model.
% dSt = mu*St*dt + sigma*St^gamma*dWt
% price time series should be passed as arguments.
% the first element in the time series is the last.
% N is the times of monte carlo.
% the function returns the calibrated parameters, and the backtest errors.


%% calibrating...
ave = mean(price2ret(price));
vol = std(price2ret(price));
dt = 1/252;
x0 = [ave, vol, 0.5];
% x(1) = mu, x(2) = sigma, x(3) = gamma
y = @(x) (price(1:end-1)-price(2:end) - x(1)*price(2:end)*dt)/x(2)./(price(2:end).^x(3))/sqrt(dt);
loglikelihood = @(x) sum(y(x).^2)+sum(log(x(2)*price(2:end).^x(3)*sqrt(dt)));
[x, fval, exitflag] = fminsearch(loglikelihood, x0);

%% backtesting...
dwt = randn(length(price)-1,N);
St = repmat(price(2:end) + x(1)*price(2:end)*dt,1,N) + x(2)*repmat(price(2:end),1,N).^x(3).*dwt*sqrt(dt);
Sthat = mean(St,2);
error = (price(1:end-1) - Sthat)./price(1:end-1);
end
