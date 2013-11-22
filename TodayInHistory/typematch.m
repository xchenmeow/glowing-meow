
% this script predicts the afternoon trend by finding the most similar 
% morning trend in the history 


%%
% set 20 points to present the whole day trend
clear; clc;

load('highfreqdata.mat');
price = Data(:,2);
date = Data(:,1);
price = price(692:end);
date = date(692:end);
date(273) = [];
price(273) = [];
[n,~] = size(price);
price = reshape(price, 1, n);
m = 239;
for i = 1:n
    price{i} = price{i}(1:m,4);
end
close = cell2mat(price);
close = close';

k = 10; % divided by k sections
l = floor(m/k) + 1;
trendopen = close(:,1:l:end);
trendclose = [close(:,l+1:l:end), close(:,end)];
trendhigh = zeros(size(trendopen));
trendlow = zeros(size(trendopen));
Ih = zeros(size(trendopen));
Il = zeros(size(trendopen));
for i = 1:k-1
    [trendhigh(:,i), Ih(:,i)] = max(close(:,l*(i-1)+1:l*(i-1)+l+1),[],2);
    [trendlow(:,i), Il(:,i)] = min(close(:,l*(i-1)+1:l*(i-1)+l+1),[],2);
end
[trendhigh(:,k), Ih(:,k)] = max(close(:,l*(k-1)+1:end),[],2);
[trendlow(:,k), Il(:,k)] = min(close(:,l*(k-1)+1:end),[],2);

flag = Ih < Il;
trendfirst = zeros(size(trendopen));
trendlast = zeros(size(trendopen));
trendfirst(flag == 1) = trendhigh(flag == 1);
trendfirst(flag == 0) = trendlow(flag == 0);
trendlast(flag == 1) = trendlow(flag == 1);
trendlast(flag == 0) = trendhigh(flag == 0);

trend = zeros(size(trendopen,1), k*2);
trend(:,1:2:end) = trendfirst;
trend(:,2:2:end) = trendlast;

%%
% finding the most similar trend
samplesize = 1000;
trainingsample = trend(:,1:k);
minsample = repmat(min(trainingsample,[],2),1,k);
maxsample = repmat(max(trainingsample,[],2),1,k);
regsample = (trainingsample - minsample)./(maxsample-minsample);

trenddist = zeros(size(trainingsample,1) - samplesize,1);
idx = zeros(size(trainingsample,1) - samplesize,1);
for i = 1:size(trainingsample,1) - samplesize
    [trenddist(i), idx(i)] = min(pdist2(regsample(1:samplesize+i-1,:),...
        regsample(samplesize+i,:)));
end



%%
% backtesting...
testingsample = trend(:,k+1:end);
error = zeros(length(idx),1);
for i = 1:length(idx)
    error(i) = pdist2(testingsample(idx(i),:), testingsample(samplesize+i,:));
end

%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% uncomment the following codes to see the accuracy of this model
% press Ctrl C to stop this program.

for testind = 100:length(error)
    clf
    subplot(2,1,1);
    hold on
    plot(1:10,trainingsample(idx(testind),:),'r');
    plot(11:20,testingsample(idx(testind),:),'b');
    xlabel(date(idx(testind)));
    hold off
    subplot(2,1,2);
    hold on
    plot(1:10,trainingsample(samplesize+testind,:),'r');
    plot(11:20,testingsample(samplesize+testind,:),'b');
    xlabel(date(samplesize+testind));
    hold off
    
    % Pause
    fprintf('Program paused. Press enter to continue.\n');
    pause;
    
    fprintf('the predicting distance is %d. \n', error(testind));    

end

%%
% strategy...

