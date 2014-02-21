function hurst = Hurst(price)
    % this function calculates the hurst exponent
    % http://en.wikipedia.org/wiki/Hurst_exponent
    
    % transform the original time series to column vector(if not)
    if size(price,2) > 1
        price = price';
    end
    % ret = price2ret(price);
    diffprice = diff(price);
    N = length(diffprice);
    n = zeros(floor(log2(N))-3,1);
    ros = zeros(floor(log2(N))-3,1);
    for i = 1:floor(log2(N)) - 3
        k = 1;
        n(i) = 2^(i + 3);
        j = 0;
        r = zeros(floor(N/n(i)),1);
        s = zeros(floor(N/n(i)),1);
        while k <= N-n(i)+1
            j = j + 1;
            sample = diffprice(k:k+n(i)-1); 
            ave = mean(sample);
            z = cumsum(sample - repmat(ave,length(sample),1));
            r(j) = max(z)-min(z);
            s(j) = std(sample,1);
            k = k + n(i);
        end
        ros(i) = mean(r./s);
    end
    beta = regress(log(ros), [ones(length(n),1), log(n)]);
    hurst = beta(2);
    
    
%     hold on
%     plot((0:1:length(n)), (0:1:length(n))*beta(2) + beta(1));
%     plot(log(n), log(ros),'ro');
%     hold off
    
end
