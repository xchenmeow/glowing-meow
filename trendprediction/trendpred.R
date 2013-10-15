
# loading...
### CHANGE PATH HERE ###
inputfile=read.csv(file = "C:/Users/cr/Documents/SSE300Data.csv", head = FALSE)

# this function returns the total return and std of nth stock
# the returns have been divided into 10 groups
# this strategy is to find out which group yield more return and less risk

trendpred <- function(n)
{
# assigning...
open <- inputfile[,2+(i-1)*9]
open <- as.numeric(as.character(open))
open <- open[4:length(open)]
close <- inputfile[,5+(i-1)*9]
close <- as.numeric(as.character(close))
close <- close[4:length(close)]

# --------------------
# calculating...
ret <- log(close) - log(open)
ret <- ret[!is.na(ret)]
average <- mean(ret[1:50,])
# flag classify all the returns to 10 class
flag <- floor(ret*50)
flag[flag < -4] <- -4
# buy one share when the stock rise at time t-1
position <- c(0, flag[1:length(flag)-1])
# position[position < 0] <- 0
deltavalue <- close - open
# classvalue is the total return in a specific class
classvalue <- rep(0,each = 10)
classrisk <- rep(0,each = 10)
for (i in -4:5)
{
	classvalue[i+5] <- sum(deltavalue[position == i])
	classrisk[i+5] <- sd(deltavalue[position == i])
}
temp = c(classvalue, classrisk)
return (matrix(temp,nrow = 10, ncol = 2))
}

#----------------------
# looping...
value <- matrix(rep(0, each = 300*10), nrow = 300, ncol = 10)
risk <- matrix(rep(0, each = 300*10), nrow = 300, ncol = 10)
for (i in 1:300)
{
value[i,] <- trendpred(i)[,1]
risk[i,] <- trendpred(i)[,2]
}
