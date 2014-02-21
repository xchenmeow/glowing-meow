w = windmatlab;

%%
befyesdate = '2014-02-07';
yesdate = '2014-02-10';
todaysdate = '2014-02-11';
%%
% SH510050, using previous one day data
etf50 =  loadwinddata(1, '510050.SH', yesdate, yesdate);
load 'net.mat'
% etfopen = w.wsd('510050.SH','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
etfforcast =  net(raw2inf(etf50, 1.477));

%%
% SZ159915, using previous two days data
% load 'sz159915net.mat' % for one day
load cat2_sz159915net.mat % for two days
GEM = loadwinddata(1, '159915.SZ', befyesdate, yesdate);
% gemopen = w.wsd('159915.SZ','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
gemforcast = net(raw2inf(GEM, 1.505));

%%
% SH601318, using previous one day data
load 'sh601318net.mat'
pingan = loadwinddata(1, '601318.SH', yesdate, yesdate);
% pinganopen = w.wsd('601318.SH','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
pinganforcast = net(raw2inf(pingan, 38.33));

%%
% SZ159915, using previous one day data
load 'sz159901net.mat'
etf100 = loadwinddata(1, '159901.SZ', yesdate, yesdate);
% etf100open = w.wsd('159901.SZ','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
etf100forcast = net(raw2inf(etf100, 0.542));