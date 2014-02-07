function [data,c,f,t,e,r] = loadwinddata(k,ticker, todaydate)

w = windmatlab;
% todaydate = '2014-01-21';
% today = datestr(datenum('2014-01-20', 'yyyy-mm-dd'));
[w_wsi_data,c,f,t,e,r]=w.wsi(ticker,'open,high,low,close,volume,amt',strcat(todaydate,'09:00:00'),strcat(todaydate,'15:00:00'),strcat('BarSize=',num2str(k)));
n = size(w_wsi_data,1);
data = [repmat(datenum(todaydate),n,1), w_wsi_data];
end