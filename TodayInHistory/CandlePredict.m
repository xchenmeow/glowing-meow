
%% 
% drawing candlestick chart
clear; clc
load('highfreqdata.mat');
date = Data(:,1);
price = Data(:,2);
date = date(692:end);
price = price(692:end);
date(273) = [];
price(273) = [];
[n,~] = size(price);
price = reshape(price, 1, n);
m = 239;
for i = 1:n
    price{i} = price{i}(1:m,4);
end
close = cell2mat(price);
close = close';
close(1138,1) = close(1138,2);

candleopen = close(:,1);
candleclose = close(:,end);
candlehigh = max(close,[],2);
candlelow = min(close,[],2);

flag = candleclose > candleopen; % black or white
bodylength = abs(candleclose - candleopen); 
uppershadowlen = candlehigh - max(candleopen, candleclose);
lowershadowlen = min(candleopen, candleclose) - candlelow; 
pos = [0; diff(candleopen)];
candlestick = [flag, bodylength, uppershadowlen, lowershadowlen, pos];

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

for testind = 1:length(errdist)
    
subplot(2,1,1);
sample = (idx(testind):idx(testind)+3);
candle(candlehigh(sample), candlelow(sample),...
    candleclose(sample), candleopen(sample));
xlabel(date(idx(testind)));

subplot(2,1,2);
predicted = (samplelen+testind:samplelen+testind+k);
candle(candlehigh(predicted), ...
    candlelow(predicted), ...
    candleclose(predicted), ...
    candleopen(predicted));
xlabel(date(samplelen+testind));

% pause
fprintf('press Enter to continue. \n');
pause;

fprintf('the predicted distance is %d. \n', errdist(testind));
end


%%
% strategy...




