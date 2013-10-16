
# loading...
### CHANGE PATH HERE ###
inputfile=read.csv(file = "C:/Users/cr/Documents/SSE300Data.csv", head = FALSE)

# this function returns the total return and std of nth stock
# the returns have been divided into 10 groups
# this strategy is to find out which group yield more return and less risk


findposition <- function(n)
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
tempret <- log(close) - log(open)
tempret <- tempret[!is.na(ret)]
# ret <- matrix(c(ret, tempret), nrow = 192, ncol = i)
average <- NULL
std <- NULL
for (j in 1:142)
{
	average <- c(average, mean(tempret[j:j+50]))
	std <- c(std, sd(tempret[j:j+50]))
}
SR <- (ret[51:length(tempret)] - average)/std
# flag classify all the returns to 10 class
flag <- floor(SR*2)
flag[flag < -4] <- -4
# buy one share at time t-1
position <- c(0, flag[1:length(flag)-1])
return (position)
}


# e...
# the problem is... ret is not a matrix...
# so cannot calculate the returns in each class...
# the loop structure should change...

classvalue <- NULL
# looping...
for (i in 1:300)
{
	position <- matrix(c(position, findposition(i)), nrow =142, ncol =i)
# classvalue is the return in a specific class
for (k in -4:5)
{
	classvalue <- matrix(c(classvalue, sum(ret[position == k],na.rm = TRUE)), nrow = 142, ncol = i)
}

}



#----------------------
totalreturn <- prod(1+value)
