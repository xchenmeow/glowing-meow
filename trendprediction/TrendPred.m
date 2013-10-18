clear
clc
%%
% loading data...
data = xlsread('SHSZ300.xlsx',2);
[m,~] = size(data);
open = NaN(m,300);
close = NaN(m,300);
% volume = NaN(192,300);
for i = 1:300
    open(:,i) = data(:,1+(i-1)*3);
    close(:,i) = data(:,2+(i-1)*3);
    % volume(:,i) = data(:,6+(i-1)*9);
end
ret = log(close) - log(open);


%%
% classifying...
% strategy 1
% all the stock returns have been divided into 11 groups. -5 <= flag <= 5.
% -5 means the stock did not trade in that week. 
% cretiria is mean plus or minus 0.2533, 0.5244, 0.8416, 1.2816 sigma 
trainingsample = ret(1:50,:);
[trainingsize,~] = size(trainingsample);
forcastingsample = ret(51:end,:);
forcastingsample(forcastingsample == 0) = NaN;
[M,N] = size(forcastingsample);
trainingmean = zeros(M-trainingsize,N);
trainingstd = zeros(M-trainingsize,N);
for i = 1:M
    trainingmean(i,:) = mean(ret(i:i+trainingsize,:));
    trainingstd(i,:) = std(ret(i:i+trainingsize,:));
end
SR = (forcastingsample-trainingmean)./trainingstd;
flag = floor(normcdf(SR)*10)+1;
flag = flag - 5;
flag(flag<-4 & flag ~= -inf) = -4;
flag(flag>5) = 5;
flag(flag==-inf) = -5;
flag(isnan(flag)) = -5;

%%
% classifying...
% strategy 2
% select 30 stocks per group by the ordered returns from last week
% not any stop loss strategy has been considered.
quantileret = quantile(forcastingsample,0.1:0.1:0.9,2);
quantileret = [ones(M,1)*(-10), quantileret, ones(M,1)*10];
flag1 = zeros(M,N);
for i = 1:10 
    flag1(forcastingsample<repmat(quantileret(:,i+1),1,N)...
        & forcastingsample>=repmat(quantileret(:,i),1,N)) = i;
end
flag1 = flag1 - 5;
flag1(isnan(flag1)) = -5;

%%
% calculating...
% P/L for -4-5 classes.
% principle is one dollar
% equal weighted each asset at time t in a specific class
% not any stop loss strategy has been considered.
position = NaN(M,N);
position(1,:) = -5*ones(1,N);
% flag from strategy 1
% flag1 from strategy 2
position(2:end,:) = flag(1:end-1,:);
classvalue = NaN(M,10);
num = zeros(M,10);
for i = -4:5
    temp = forcastingsample;
    temp(position == i) = 0;
    tempmat = forcastingsample - temp;
    num(:,i+5) = sum(~isnan(tempmat) & tempmat~=0,2);
    classvalue(:,i+5) = nansum(tempmat,2)./num(:,i+5);
    classvalue(isnan(classvalue)) = 0;
    classvalue(1,i+5) = 0;
end


%%
% analysing...
% find the best class by the result of stretagy above

cumreturn = cumprod(classvalue+1);
sharpratio = mean(classvalue)./std(classvalue);
maxloss = min(classvalue);
orderedvalue = sort(classvalue,1,'ascend');
VaR = orderedvalue(floor(M*0.05),:); % alpha = 5%
RAROC = mean(classvalue)./VaR;
figure
for i = 1:10
   subplot(2,5,i), qqplot(classvalue(:,i))
end

% class 5 performs best...
% [row col] stores the indeces of the stocks in class 5 
[row, col] = find(position == 5);

%%
% selecting...

numtd = sum(~isnan(forcastingsample));
selectingsample = forcastingsample(:,numtd>100);
correlation = corrcoef(selectingsample, 'rows', 'pairwise');
% for i = 1:N
i = 1;
    tempcorr = correlation(row(col == i),row(col == i));
    tempcorr = triu(tempcorr);
    tempcorr(tempcorr == 0) = 2;
    sortedcorr = sort(reshape(tempcorr,size(tempcorr,2)^2,1));
    [tempr,tempc] = find(tempcorr < sortedcorr(6));
    indr = row(tempr);
    indc = row(tempc);
% end


