function winddata = windhighfreqdata(ticker, barsize, startdate, enddate)


w = windmatlab;
winddata = [];
times = datenum(enddate)+1;
while times(1) > datenum(startdate)
    enddate = datestr(times(1)-1, 'yyyy-mm-dd');
    [data, ~, ~, times, error,~] = w.wsi(ticker,'open,high,low,close,volume,amt',strcat(startdate, ' 09:00:00'),strcat(enddate,' 15:30:00'),strcat('BarSize=', num2str(barsize)));
    if error ~= 0
        break
    end
    winddata = [[times, data]; winddata];
end