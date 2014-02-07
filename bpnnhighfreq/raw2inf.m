function [inputsmooth, target_mat] = raw2inf(rawdata, open)

% convert the rawdata to the form of [input, target]
% we need to train the neural network

l = 5;
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
    if ~isempty(r)
    for j = 1:length(r)
        if r(j) == 1
            price(r(j),c(j)) = price(r(j)+1,c(j));
        else
            price(r(j),c(j)) = price(r(j)-1,c(j));
        end
    end
    end
    high = max(price(:,3));
    temp = price(:,4);
    low = min(temp(temp>0));
    close_Reg = Reg(price([1,2:l:end],5))';
    volumn_Reg = Reg(price([1,2:l:end],6))';
    input{i} = [close_Reg, volumn_Reg];
    target{i} = [high, low];
end

input_mat = cell2mat(input)';
target_mat = cell2mat(target)';
% open = 1.479;
% inputmat = input_mat(:,1:end-1);
% targetmat = target_mat(:,2:end);

inputmatv2 = 0.25*input_mat(1:50,:)+0.25*input_mat(51:100,:)+0.5*repmat(open,50,1);
inputsmooth = zeros(size(inputmatv2));
for i = 1:size(inputmatv2,2)
    inputsmooth(:,i) = smooth(inputmatv2(:,i));
end

end