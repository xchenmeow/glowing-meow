library(rugarch)
library(xts)

args <- commandArgs(trailingOnly = TRUE)
# args <- c("C:\\Users\\benqing.shen\\Desktop\\Data", "symbols_short.csv")
# args <- c("C:\\bshen\\glowing-meow\\DataUpdater\\return_temp", "symbols_short.csv")

data_dir <- args[1]
data_names <- read.csv(args[2], header=FALSE)

symbol = '^GSPC'

for(i in 1:nrow(data_names)) {
  symbol <- toString(data_names[i, ])

  # load fit
  fit_name <- paste(symbol, 'fit', sep='_')
  fit_file <- paste(fit_name, 'RData', sep='.')
  load(file=fit_file)
  
  # load data
  data_file <- paste(data_dir, "\\", symbol, "_returns.csv", sep="")
  df <- read.csv(data_file, header=TRUE, skip=1)
  df[, 1] = as.Date(x=df[, 1], format="%Y-%m-%d")
  df <- xts(df[,2], order.by=df[,1])
  
  fcst <- ugarchforecast(fitORspec=fit)
  
  sink(file=paste(symbol, "fcst.txt", sep='_'), split=FALSE)
  rugarch::show(fcst)
  sink()
}
