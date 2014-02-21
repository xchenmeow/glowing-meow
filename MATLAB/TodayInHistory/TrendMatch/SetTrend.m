function trend = SetTrend(k, close)
% close is a m*n matirx which contains data in m days, 
% and n period in each day
% close is the close price in every minutes
% divided close by k sections
% find the high and low in the k sections
% trend first returns the high or low which comes first

m = size(close,2);
l = floor(m/k) + 1;
% trendopen = close(:,1:l:end);
% trendclose = [close(:,l+1:l:end), close(:,end)];
trendhigh = zeros(size(close,1),k);
trendlow = zeros(size(close,1),k);
Ih = zeros(size(close,1),k);
Il = zeros(size(close,1),k);
for i = 1:k-1
    [trendhigh(:,i), Ih(:,i)] = max(close(:,l*(i-1)+1:l*(i-1)+l+1),[],2);
    [trendlow(:,i), Il(:,i)] = min(close(:,l*(i-1)+1:l*(i-1)+l+1),[],2);
end
[trendhigh(:,k), Ih(:,k)] = max(close(:,l*(k-1)+1:end),[],2);
[trendlow(:,k), Il(:,k)] = min(close(:,l*(k-1)+1:end),[],2);

flag = Ih < Il;
trendfirst = zeros(size(close,1),k);
trendlast = zeros(size(close,1),k);
trendfirst(flag == 1) = trendhigh(flag == 1);
trendfirst(flag == 0) = trendlow(flag == 0);
trendlast(flag == 1) = trendlow(flag == 1);
trendlast(flag == 0) = trendhigh(flag == 0);

trend = zeros(size(close,1), k*2);
trend(:,1:2:end) = trendfirst;
trend(:,2:2:end) = trendlast;

end