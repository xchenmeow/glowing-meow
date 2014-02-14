args <- commandArgs(trailingOnly = TRUE)

# args <- c("C:\\Users\\benqing.shen\\Desktop\\Data", "HYG_returns")

data_dir <- args[1]

# data_file: assumes Yahoo return time series.
# assumes also date range is processed
data_name <- args[2]

data_file <- paste(data_dir, "\\", data_name, ".csv", sep="")

# load spec
if(length(args) == 3) {
  load(args[3])
} else {
  load("ModelSpec.RData")
}

df <- read.csv(data_file)
# rownames(df) <- df$Date

library(rugarch)
# spec <- ugarchspec(mean.model=list(armaOrder=c(0,0), include.mean=FALSE))
fit <- ugarchfit(spec=spec, data=df[,2])
save(fit, file=paste(data_name, "fit.RData", sep='_'))
# rugarch::show(fit)
# ugarchforecast(fitORspec=fit, data=df[,2], n.ahead=1)


# library(fGarch)
# spec.f <- garchSpec()
# fit.f <- garchFit(data=df[,2], include.mean=TRUE)
