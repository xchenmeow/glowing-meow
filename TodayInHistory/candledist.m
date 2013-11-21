
function [candleliketoday,idx] = candledist(Y,X,weight)
% Y is a n*(m+1) matrix
% X is a samplesize*(m+1) matrix
% weight is a 1*n matrix

% if samplesize < k, k is the window size
% just calculate the distance between X and Y, idx returns 0

% the first colume of X and Y are flags indicate the color of the...
% candlestick body
% this function finds the closest candlesticks which is like today's most
% the window is 3 days, which means the previow 3 days candle should...
% match each other respectively.
% the flag should be matched strictly
% find the candle have shortest distance(euclidean) to today's candle.

k = 3;  % window size
samplesize = size(X,1);
candleliketoday = 1;
flag = Y(:,1);

if samplesize > k
    
for i = 1:samplesize-k+1
    flagx = X(i:i+k-1,1);
    if flagx == flag
        temp = (Y(:,2:end)-X(i:i+k-1,2:end)).^2;
        tempdist = weight * temp;
        if candleliketoday > sum(tempdist)
            candleliketoday = sum(tempdist);
            idx = i;
        end
    end
end

else 
    flagx = X(:,1);
    if flagx == flag
        temp = (Y(:,2:end)-X(:,2:end)).^2;
        tempdist = weight * temp;
        if candleliketoday > sum(tempdist)
            candleliketoday = sum(tempdist);
            idx = 0;
        end
    end
end

end