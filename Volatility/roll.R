args <- commandArgs(trailingOnly = TRUE)

# args <- c("C:\\bshen\\glowing-meow\\DataUpdater\\return_temp", "symbols_short.csv", 500)
# args <- c("C:\\bshen\\glowing-meow\\DataUpdater\\return_temp", "symbols_one.csv", 2500)
# args <- c("C:\\bshen\\glowing-meow\\DataUpdater\\return_temp", "symbols_one.csv", 4000)

data_dir <- args[1]

# data_file: assumes Yahoo return time series.
# assumes also date range is processed
data_names <- read.csv(args[2], header=FALSE)

fcst_length <- as.numeric(args[3])

library(rugarch)
library(xts)

for(i in 1:nrow(data_names)) {
  data_name <- toString(data_names[i, ])
  
  data_file <- paste(data_dir, "\\", data_name, "_returns.csv", sep="")
  
  # load spec
  if(length(args) == 4) {
    load(args[4])
  } else {
    load("ModelSpec.RData")
  }
  
  df <- read.csv(data_file, header=TRUE, skip=1)
  df[, 1] = as.Date(x=df[, 1], format="%Y-%m-%d")
  df <- xts(df[,2], order.by=df[,1])
  # read.table()
  # rownames(df) <- df$Date
  
  # spec <- ugarchspec(mean.model=list(armaOrder=c(0,0), include.mean=FALSE))
  ugroll <- ugarchroll(spec=spec, data=df, forecast.length=fcst_length)
  out_file_name <- paste(data_name, 'roll.csv', sep='_')
  write.table(x=ugroll@forecast$density, file=out_file_name, quote=FALSE, sep=',')
}