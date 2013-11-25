
% this script predicts the afternoon trend by finding the most similar 
% morning trend in the history 


%%
% set 20 points to present the whole day trend
clear; clc;

% should change the way of loading data
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

k = 10;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% trend = SetTrend(k, close); 
% set trend without the previous close
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
trend = SetTrendwithClose(k, close, close(:,end)); 
% set trend with the previous close

%%
% finding the most similar trend
samplesize = 1000;
trainingsample = trend(:,1:k+1);
regsample = Reg(trainingsample);

trenddist = zeros(size(trainingsample,1) - samplesize,1);
idx = zeros(size(trainingsample,1) - samplesize,1);
for i = 1:size(trainingsample,1) - samplesize
    [trenddist(i), idx(i)] = min(pdist2(regsample(1:samplesize+i-1,:),...
        regsample(samplesize+i,:)));
end



%%
% backtesting...
testingsample = trend(:,k+2:end);
error = zeros(length(idx),1);
for i = 1:length(idx)
    error(i) = pdist2(testingsample(idx(i),:), testingsample(samplesize+i,:));
end

%%

% uncomment the following codes to see the accuracy of this model
% press Ctrl C to stop this program.

% for testind = 100:length(error)
%     clf
%     subplot(2,1,1);
%     hold on
%     plot(1:k+1,trainingsample(idx(testind),:),'r');
%     plot(k+2:2*k+2,testingsample(idx(testind),:),'b');
%     xlabel(datenum(idx(testind)));
%     hold off
%     subplot(2,1,2);
%     hold on
%     plot(1:k+1,trainingsample(samplesize+testind,:),'r');
%     plot(k+2:2*k+2,testingsample(samplesize+testind,:),'b');
%     xlabel(datenum(samplesize+testind));
%     hold off
%     
%     % Pause
%     fprintf('Program paused. Press enter to continue.\n');
%     pause;
%     
%     fprintf('the predicting distance is %d. \n', error(testind));    
% 
% end

%%
% predicting...

% load today's morning data
% should change the way of loading data
todaydata = xlsread('nov1113highfreq.xlsx');
previousclose = 1.64;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% datatoday = SetTrend(k/2, todaydata(:,4)'); 
% set trend without previous close
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
datatoday = SetTrendwithClose(k/2, todaydata(:,4)', previousclose);
% set trend with previous close
regtoday = Reg(datatoday);
[trenddisttoday, idxtoday] = min(pdist2(regsample(1:end-1,:),regtoday));
regtestsample = Reg(testingsample(idxtoday,:));
predictingtrend = regtestsample * (max(datatoday)-min(datatoday)) ...
    + min(datatoday);

% plot the prediction
subplot(2,1,1);
hold on
plot(1:k+1,trainingsample(idxtoday,:),'r');
plot(k+2:2*k+2,testingsample(idxtoday,:),'b');
xlabel(datenum(idxtoday));
hold off

subplot(2,1,2);
hold on
plot(1:k+1,datatoday,'r');
plot(k+2:2*k+2,predictingtrend, 'b--');
xlabel(date);
hold off


