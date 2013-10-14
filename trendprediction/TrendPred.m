
%%
% loading data...
data = xlsread('»¦Éî300Êý¾Ý');
open = NaN(192,300);
close = NaN(192,300);
volume = NaN(192,300);
for i = 1:300
    open(:,i) = data(:,1+(i-1)*9);
    close(:,i) = data(:,4+(i-1)*9);
    volume(:,i) = data(:,6+(i-1)*9);
end
%%
% classifying...
% all the stock returns have been divided into 11 groups. -5 <= flag <= 5.
% -5 means the stock did not trade in that week. 
% ret < -0.08       -4;    -0.08<ret<-0.06 -3;
% -0.06<ret<-0.04	-2;    -0.04<ret<-0.02 -1; 
% -0.02 < ret < 0    0;    0 < ret < 0.02   1;
% 0.02<ret<0.04      2;    0.04<ret<0.06    3;
% 0.06<ret<0.08      4;    0.08 < ret       5;
ret = log(close) - log(open);
ret(isnan(ret)) = 0;
flag = floor(ret*50)+1;
flag(flag<-4 & flag ~= -inf) = -4;
flag(flag>5) = 5;
flag(flag==-inf) = -5;

%%
% calculating...
% flag (1-5 at time t-1) shares will be bought at time t.
% not any stop loss strategy has been considered.
position = zeros(192,300);
position(2:end,:) = flag(1:end-1,:);
position(position <= 0) = 0;
deltavalue = position.*(close-open);
totalvalue = cumsum(deltavalue);

% P/L for 1-5 classes.
% buy one share of each asset at time t, if its flag's in (1,5) at time t-1 
% not any stop loss strategy has been considered.
classvalue = NaN(192,5);
for i = 1:5
    temp = deltavalue;
    temp(position == i) = 0;
    tempmat = deltavalue - temp;
    classvalue(:,i) = sum(tempmat,2)/i;
end




