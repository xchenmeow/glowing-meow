function [minafternoon, maxafternoon] = TrendMatchFunc(todayfilename, k, numofmatch, closeflag, previousclose)
% this function predicts the afternoon trend by finding the most similar 
% morning trend in the history 
% todayfilename contains today's morning data
% k is the number of sections this function divide the data(whole day) into
% closeflag is a flag indicates using previous close data of not
% 0 set trend without the previous close
% 1 set trend with the previous close
% previousclose is the close price from yesterday
% numofmatch is number this function find the most similar trend


%%
% set 20 points to present the whole day trend

load('highfreqdata.mat');
price = Data(:,2);
datenum = Data(:,1);
price = price(692:end);
datenum = datenum(692:end);
m = 239;
[n,~] = size(price);
for i = 1:n
    try
        price{i} = price{i}(1:m,4);
    catch exceptions
        price{i} = [];
        datenum{i} = [];
    end
end
close = cell2mat(price');
close = close';


if closeflag == 0
    trend = SetTrend(k, close); 
elseif closeflag == 1
    trend = SetTrendwithClose(k, close, close(:,end)); 
else
    fprintf('closeflag can only take 0 or 1');
end

%%
% finding the most similar trend
samplesize = 1000;
trainingsample = trend(:,1:k+closeflag);
regsample = Reg(trainingsample);

trenddist = zeros(size(trainingsample,1) - samplesize,1);
idx = zeros(size(trainingsample,1) - samplesize,1);
for i = 1:size(trainingsample,1) - samplesize
    [trenddist(i), idx(i)] = min(pdist2(regsample(1:samplesize+i-1,:),...
        regsample(samplesize+i,:)));
end



%%
% backtesting...
testingsample = trend(:,k+1+closeflag:end);
error = zeros(length(idx),1);
for i = 1:length(idx)
    error(i) = pdist2(testingsample(idx(i),:), testingsample(samplesize+i,:));
end



%%
% predicting...

% load today's morning data

todaydata = xlsread(todayfilename);

if closeflag == 0
    datatoday = SetTrend(k/2, todaydata(:,4)'); 
elseif closeflag == 1
    datatoday = SetTrendwithClose(k/2, todaydata(:,4)', previousclose);
end
regtoday = Reg(datatoday);

trenddisttoday = zeros(numofmatch,1);
idxtoday = zeros(numofmatch,1);
predictingtrend = zeros(numofmatch,k+closeflag);
minafternoon = zeros(numofmatch,1);
maxafternoon = zeros(numofmatch,1);
[tempdist, tempidx] = sort(pdist2(regsample(1:end-1,:),regtoday));
for i = 1:numofmatch   
    trenddisttoday(i) = tempdist(i);
    idxtoday(i) = tempidx(i);
    minsample = min(trainingsample(idxtoday(i),:));
    maxsample = max(trainingsample(idxtoday(i),:));
    regtestsample = (testingsample(idxtoday(i),:)-minsample)/(maxsample-minsample);
    predictingtrend(i,:) = regtestsample * (max(datatoday)-min(datatoday)) ...
        + min(datatoday);
    minafternoon(i) = min(predictingtrend(i,:));
    maxafternoon(i) = max(predictingtrend(i,:));

    % plot the prediction
    clf
    subplot(2,1,1);
    hold on
    plot(1:k+closeflag,trainingsample(idxtoday(i),:),'r');
    plot(k+closeflag:2*k+2*closeflag,[trainingsample(idxtoday(i),end),testingsample(idxtoday(i),:)],'b');
    xlabel(datenum(idxtoday(i)));
    hold off

    subplot(2,1,2);
    hold on
    plot(1:k+closeflag,datatoday,'r');
    plot(k+closeflag:2*k+2*closeflag,[datatoday(end), predictingtrend(i,:)], 'b--');
    xlabel(date);
    hold off
    
    fprintf('program pause, press Enter to continue.\n');
    pause;


end
