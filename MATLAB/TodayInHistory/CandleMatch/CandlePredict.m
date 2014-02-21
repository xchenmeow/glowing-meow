
%% 
% drawing candlestick chart
clear; clc

Data = csvread('510050SS.csv',1,0);
datenumber = Data(:,1);

candleopen = Data(1:end-1,2);
candleclose = Data(1:end-1,5);
candlehigh = Data(1:end-1,3);
candlelow = Data(1:end-1,4);

candlestick = SetCandle(candleopen, candlehigh, candlelow, candleclose);


%%
% finding the alike candle
samplelen = 1000;
k = 3; % window size
testsample = candlestick(samplelen+1:end,:);
weight = [1/6, 1/3, 1/2];
idx = zeros(size(testsample,1)-k+1,1);
for i = 1:size(testsample,1)-k+1
    [candledistance, idx(i)] = candledist(testsample(i:i+k-1,:), ...
        candlestick(1:samplelen+i-1,:), weight);
end



%%
% testing...
errdist = zeros(length(idx)-2,1);
for i = 1:length(idx)-2
    errdist(i) = candledist(testsample(i+k,:), candlestick(idx(i)+k,:),1);
end

%%
% uncomment the following codes to see the backtest candlestick chart
% press Ctrl C to stop showing the candelstick charts.

% for testind = 1:length(errdist)
%     
% subplot(2,1,1);
% sample = (idx(testind):idx(testind)+k);
% candle(candlehigh(sample), candlelow(sample),...
%     candleclose(sample), candleopen(sample));
% xlabel(datestr(date(idx(testind))+datenum([1900,1,1])));
% 
% subplot(2,1,2);
% predicted = (samplelen+testind:samplelen+testind+k);
% candle(candlehigh(predicted), ...
%     candlelow(predicted), ...
%     candleclose(predicted), ...
%     candleopen(predicted));
% xlabel(datestr(date(samplelen+testind)+datenum([1900,1,1])));
% 
% % pause
% fprintf('press Enter to continue. \n');
% pause;
% 
% fprintf('the predicted distance is %d. \n', errdist(testind));
% end
% 

%%
% predicting...
todayopen = Data(end-k+1:end,2);
todayhigh = Data(end-k+1:end,3);
todaylow = Data(end-k+1:end,4);
todayclose = Data(end-k+1:end,5);
todaycandle = SetCandle(todayopen, todayhigh, todaylow, todayclose);
[todaydistance, todayidx] = candledist(todaycandle, ...
        candlestick, weight);

flagtoday = candlestick(todayidx+k,1);
bodylentoday = candlestick(todayidx+k,2);
predictcandleopen = todayopen(end) + candlestick(todayidx+k,5);
predictcandleclose = predictcandleopen + (flagtoday-(~flagtoday))*bodylentoday;
predictcandlehigh = max(predictcandleclose, predictcandleopen) + candlestick(todayidx+k,3); 
predictcandlelow = min(predictcandleclose, predictcandleopen) - candlestick(todayidx+k,4);
    
subplot(2,1,1);
todaysample = todayidx:todayidx+k;
candle(candlehigh(todaysample), candlelow(todaysample),...
    candleclose(todaysample), candleopen(todaysample));
xlabel(datestr(datenumber(todayidx)+datenum([1900,1,1])));

subplot(2,1,2);
candle([todayhigh;predictcandlehigh], ...
    [todaylow;predictcandlelow], ...
    [todayclose;predictcandleclose], ...
    [todayopen;predictcandleopen]);
xlabel(date);


