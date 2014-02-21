function [data,c,f,t,e,r] = loadwinddata(k,ticker, startdate, enddate)

w = windmatlab;
% todaydate = '2014-01-21';
% today = datestr(datenum('2014-01-20', 'yyyy-mm-dd'));
[w_wsi_data,c,f,t,e,r]=w.wsi(ticker,'open,high,low,close,volume,amt',strcat(startdate,'09:00:00'),strcat(enddate,'15:00:00'),strcat('BarSize=',num2str(k)));
n = size(w_wsi_data,1);
data = [t, w_wsi_data];
end