args <- commandArgs(trailingOnly = TRUE)

# args <- c("C:\\bshen\\glowing-meow\\DataUpdater\\return_temp", "symbols_short.csv")

data_dir <- args[1]

# data_file: assumes Yahoo return time series.
# assumes also date range is processed
data_names <- read.csv(args[2], header=FALSE)

library(rugarch)
library(xts)

for(i in 1:nrow(data_names)) {
  data_name <- toString(data_names[i, ])

  data_file <- paste(data_dir, "\\", data_name, "_returns.csv", sep="")

  # load spec
  if(length(args) == 3) {
    load(args[3])
  } else {
    load("ModelSpec.RData")
  }
  
  df <- read.csv(data_file, header=TRUE, skip=1)
  df[, 1] = as.Date(x=df[, 1], format="%Y-%m-%d")
  df <- xts(df[,2], order.by=df[,1])
  # read.table()
  # rownames(df) <- df$Date
  
  # spec <- ugarchspec(mean.model=list(armaOrder=c(0,0), include.mean=FALSE))
  fit <- ugarchfit(spec=spec, data=df)
  save(fit, file=paste(data_name, "fit.RData", sep='_'))
  sink(file=paste(data_name, "fit.txt", sep='_'), split=FALSE)
  rugarch::show(fit)
}

sink()

# rugarch::show(fit)
# ugarchforecast(fitORspec=fit, data=df[,2], n.ahead=1)


# library(fGarch)
# spec.f <- garchSpec()
# fit.f <- garchFit(data=df[,2], include.mean=TRUE)
