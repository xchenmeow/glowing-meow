


l = 5; % k min data
%%
% rawdata = csvread('etf502013highfreq.csv',2,0);
load sz159915.mat
rawdata = sz159915;
N = floor(rawdata(end,1)) - floor(rawdata(1,1));
data = cell(N, 1);
for t = floor(rawdata(1,1)):floor(rawdata(end,1))
    j = t - floor(rawdata(1,1)) + 1;
    data{j} =  rawdata(floor(rawdata(:,1)) == t,:);
end

emptyCells = cellfun(@isempty,data);
data(emptyCells) = [];
N = length(data);
input = cell(N, 1);
target = cell(N, 1);
for i = 1:N
    price = data{i};
    if size(price,1) < 242
        price(length(price)+1:242,:) = repmat(price(length(price),:),242-length(price),1);
    end
    [r,c] = find(price == 0);
    for j = 1:length(r)
        if r(j) == 1
            price(r(j),c(j)) = price(r(j)+1,c(j));
        else
            price(r(j),c(j)) = price(r(j)-1,c(j));
        end
    end
    high = max(price(:,3));
    temp = price(:,4);
    low = min(temp(temp>0));
    open = price(1,2);
    close_Reg = Reg(price([1,2:l:end],5))';
    volumn_Reg = Reg(price([1,2:l:end],6))';
    input{i} = [close_Reg, volumn_Reg, open];
    target{i} = [high, low];
end

%%

input_mat = cell2mat(input)';
target_mat = cell2mat(target)';
inputmat = input_mat(1:end-1,1:end-1);
open = input_mat(end,2:end);
targetmat = target_mat(:,2:end);

% ind = [min(inputmat); max(inputmat)];
% L = abs(ind([sum(ind,1) >= 0,sum(ind,1) < 0]')); % time slot to transform
% n = size(inputmat,1);
% inputinf = zeros(size(inputmat));
% for i = 1:length(L)
%     t2=linspace(0,L(i),n+1); t=t2(1:n);
%     k=(2*pi/L(i))*[0:n/2-1 -n/2:-1]; ks=fftshift(k);
%     filter=exp(-0.1*ks.^2); % Gaussian filter
%     inputnf = filter'.*fftshift(fft(inputmat(:,i)));
%     inputinf(:,i) = ifft(ifftshift(inputnf));
%     if i == 1
%     	subplot(2,1,1); plot(1:100, inputmat(:,1),'k', 1:100, abs(inputinf(:,1)),'g');
%         subplot(2,1,2); plot(ks, abs(inputnf)/max(abs(inputnf)),'k');
%         pause(0.1)
%     end
% end
inputmatv2 = 0.3*inputmat(1:50,:)+0.2*inputmat(51:100,:)+0.5*repmat(open,50,1);
inputsmooth = zeros(size(inputmatv2));
for i = 1:size(inputmatv2,2)
    inputsmooth(:,i) = smooth(inputmatv2(:,i)); 
end

m = size(inputmatv2,2);
[trainInd,valInd,testInd] = divideind(m,1:floor(m*0.6),floor(m*0.6)+1:floor(m*0.8),floor(m*0.8)+1:m);
net = feedforwardnet(2,'trainbr');
net.divideFcn;
net = train(net,inputsmooth,targetmat);
a = net(inputsmooth(:,end));


%%
