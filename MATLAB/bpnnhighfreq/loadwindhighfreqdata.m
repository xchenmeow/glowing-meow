w = windmatlab;
data601318 = [];
times = 735623;
while times(1) > 734524
    enddate = datestr(times(1)-1, 'yyyy-mm-dd');
    try
    [data, ~, ~, times, error,~] = w.wsi('601318.SH','open,high,low,close,volume,amt','2011-01-03 09:00:00',strcat(enddate,' 15:30:00'),'BarSize=60');
    catch error
        disp(error)
    end
    data601318 = [[times, data]; data601318];
end