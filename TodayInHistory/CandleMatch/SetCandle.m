function candlestick = SetCandle(open, high, low, close)
    flag = close > open; % black or white
    bodylength = abs(close - open); 
    uppershadowlen = high - max(open, close);
    lowershadowlen = min(open, close) - low; 
    pos = [0; diff(open)];
    candlestick = [flag, bodylength, uppershadowlen, lowershadowlen, pos];
end