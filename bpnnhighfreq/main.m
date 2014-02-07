w = windmatlab;

yesdate = '2014-01-30';
% todaysdate = '2014-02-07';
etf50 =  loadwinddata(1, '510050.SH', yesdate);
load 'net.mat'
% etfopen = w.wsd('510050.SH','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
etfforcast =  net(raw2inf(etf50, 1.465));

load 'sz159915net.mat'
GEM = loadwinddata(1, '159915.SZ', yesdate);
% gemopen = w.wsd('159915.SZ','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
gemforcast = net(raw2inf(GEM, 1.451));
% ???

load 'sh601318net.mat'
pingan = loadwinddata(1, '601318.SH', yesdate);
% pinganopen = w.wsd('601318.SH','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
pinganforcast = net(raw2inf(pingan, 38.61));

load 'sz159901net.mat'
etf100 = loadwinddata(1, '159901.SZ', yesdate);
% etf100open = w.wsd('159901.SZ','open',todaysdate,todaysdate,'Days=Alldays','Fill=Previous');
etf100forcast = net(raw2inf(etf100, 0.531));