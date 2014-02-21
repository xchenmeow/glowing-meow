function data_Reg = Reg(data)

data_Reg = (data - mean(data)) / std(data);
