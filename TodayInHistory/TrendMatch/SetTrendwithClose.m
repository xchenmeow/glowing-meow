function trend = SetTrendwithClose(k, data, close)
% data is a m*n matrix which contains data in m days, 
% and n period in each day
% close is a m*1 vector for dividing all day data
% or close can be 1*1 vector for predicting
% data is the close price in every minutes
% close is the daily close price
% divided data by k sections
% find the high and low in the k sections
% trend first returns the high or low which comes first

m = size(data,2);
l = floor(m/k) + 1;
% trendopen = close(:,1:l:end);
% trendclose = [close(:,l+1:l:end), close(:,end)];
trendhigh = zeros(size(data,1),k);
trendlow = zeros(size(data,1),k);
Ih = zeros(size(data,1),k);
Il = zeros(size(data,1),k);
for i = 1:k-1
    [trendhigh(:,i), Ih(:,i)] = max(data(:,l*(i-1)+1:l*(i-1)+l+1),[],2);
    [trendlow(:,i), Il(:,i)] = min(data(:,l*(i-1)+1:l*(i-1)+l+1),[],2);
end
[trendhigh(:,k), Ih(:,k)] = max(data(:,l*(k-1)+1:end),[],2);
[trendlow(:,k), Il(:,k)] = min(data(:,l*(k-1)+1:end),[],2);

flag = Ih < Il;
trendfirst = zeros(size(data,1),k);
trendlast = zeros(size(data,1),k);
trendfirst(flag == 1) = trendhigh(flag == 1);
trendfirst(flag == 0) = trendlow(flag == 0);
trendlast(flag == 1) = trendlow(flag == 1);
trendlast(flag == 0) = trendhigh(flag == 0);

if length(close) > 1
    trend = zeros(size(data,1)-1, k*2+2);
    trend(:,2:2:end-2) = trendfirst(2:end,:);
    trend(:,3:2:end) = trendlast(2:end,:);
    trend(:,1) = close(1:end-1,end);
    trend(:,end) = close(2:end,end);
else
    trend = zeros(1, k*2+1);
    trend(:,2:2:end) = trendfirst;
    trend(:,3:2:end) = trendlast;
    trend(:,1) = close;
end
    
end

