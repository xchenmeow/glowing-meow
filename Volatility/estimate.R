args <- commandArgs(trailingOnly = TRUE)

# data_file <- 'C:\\Users\\benqing.shen\\Desktop\\Data\\HYG_returns.csv'
data_file <- args[1]

df <- read.csv(data_file)
# rownames(df) <- df$Date

library(rugarch)
spec <- ugarchspec(mean.model=list(armaOrder=c(0,0), include.mean=FALSE))
fit <- ugarchfit(spec=spec, data=df[,2])
rugarch::show(fit)
# ugarchforecast(fitORspec=fit, data=df[,2], n.ahead=1)


# library(fGarch)
# spec.f <- garchSpec()
# fit.f <- garchFit(data=df[,2], include.mean=TRUE)
