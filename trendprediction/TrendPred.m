clear
clc
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
% cretiria is mean plus or minus 1/2, 1, 3/2, 2 sigma 
ret = log(close) - log(open);
ret(isnan(ret)) = 0;
trainingsample = ret(1:50,:);
[trainingsize,~] = size(trainingsample);
forcastingsample = ret(51:end,:);
[M,N] = size(forcastingsample);
trainingmean = zeros(M-trainingsize,N);
trainingstd = zeros(M-trainingsize,N);
for i = 1:M
    trainingmean(i,:) = mean(ret(i:i+trainingsize,:));
    trainingstd(i,:) = std(ret(i:i+trainingsize,:));
end
SR = (forcastingsample-trainingmean)./trainingstd;
flag = floor(SR*2)+1;
flag(flag<-4 & flag ~= -inf) = -4;
flag(flag>5) = 5;
flag(flag==-inf) = -5;
flag(isnan(flag)) = -5;

%%
% calculating...

% strategy 1
% select first 5 stocks which had highest returns from last week
% this strategy sucks...
% not any stop loss strategy has been considered.
[orderedret,ind] = sort(forcastingsample,2,'descend');
ind = ind(:,1:5);
deltaret = zeros(M-1,1);
for i = 1:M-1
    deltaret(i) = sum(forcastingsample(i+1,ind(i,:)));
end
totalret = sum(deltaret);

% strategy 2
% P/L for -4-5 classes.
% buy one share of each asset at time t 
% not any stop loss strategy has been considered.
position = zeros(M,N);
position(2:end,:) = flag(1:end-1,:);
classvalue = NaN(M,10);
for i = -4:5
    temp = forcastingsample;
    temp(position == i) = 0;
    tempmat = forcastingsample - temp;
    classvalue(:,i+5) = sum(tempmat,2);
    classvalue(1,:) = zeros(1,10);
end


%%
% analysing...
% find the best class by the result of stretagy 2 above

% subplot(2,1,1), plot(classvalue(:,5))
% subplot(2,1,2), plot(classvalue(:,6))
% qqplot(classvalue(:,2))
sharpratio = mean(classvalue)./std(classvalue);
maxloss = min(classvalue);
orderedvalue = sort(classvalue,1,'ascend');
VaR = orderedvalue(7,:);
RAROC = mean(classvalue)./VaR;




