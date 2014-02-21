function regsample = Reg(sample)
% regularize the sample by min-max 
    k = size(sample,2);
    minsample = repmat(min(sample,[],2),1,k);
    maxsample = repmat(max(sample,[],2),1,k);
    regsample = (sample - minsample)./(maxsample-minsample);
end