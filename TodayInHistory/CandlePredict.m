
%% 
% drawing candlestick chart
price = Data(:,2);
price = price(692:end);
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

% uncomment the following codes to see the in sample test candlestick chart

% istind = 1;
% subplot(1,2,1);
% candle(candlehigh(idx(istind):idx(istind)+2), candlelow(idx(istind):idx(istind)+2),...
%     candleclose(idx(istind):idx(istind)+2), candleopen(idx(istind):idx(istind)+2));
% subplot(1,2,2);
% candle(candlehigh(samplelen+istind:samplelen+istind+k-1), ...
%     candlelow(samplelen+istind:samplelen+istind+k-1), ...
%     candleclose(samplelen+istind:samplelen+istind+k-1), ...
%     candleopen(samplelen+istind:samplelen+istind+k-1));

%%
% testing...
errdist = zeros(length(idx)-2,1);
for i = 1:length(idx)-2
    errdist(i) = candledist(testsample(i+k+1,:), candlestick(idx(i)+k+1,:),1);
end

% uncomment the following codes to see the backtest candlestick chart

% testind = 1;
% subplot(1,2,1);
% candle(candlehigh(idx(testind)+4), candlelow(idx(testind)+4), ...
%     candleclose(idx(testind)+4), candleopen(idx(testind)+4));
% subplot(1,2,2);
% candle(candlehigh(samplelen+k+1+testind), candlelow(samplelen+k+1+testind), ...
%     candleclose(samplelen+k+1+testind), candleopen(samplelen+k+1+testind));

%%
% strategy...




