
# loading...
### CHANGE PATH HERE ###
inputfile=read.csv(file = "C:/Users/cr/Documents/SSE300Data.csv", head = FALSE)

# this function returns the total return and std of nth stock
# the returns have been divided into 10 groups
# this strategy is to find out which group yield more return and less risk


ret <- NULL
position <- NULL
for (i in 1:300)
{

	# assigning...
	open <- inputfile[,2+(i-1)*3]
	open <- as.numeric(as.character(open))
	open <- open[4:length(open)]
	close <- inputfile[,3+(i-1)*3]
	close <- as.numeric(as.character(close))
	close <- close[4:length(close)]

	# --------------------
	# calculating...
	tempret <- log(close) - log(open)
	ret <- matrix(c(ret, tempret), nrow = 192, ncol = i)
	average <- NULL
	std <- NULL
	for (j in 1:142)
	{
		average <- c(average, mean(tempret[j:(j+50)],na.rm = T))
		std <- c(std, sd(tempret[j:(j+50)], na.rm = T))
	}
	SR <- (tempret[51:length(tempret)] - average)/std
	# flag classify all the returns to 10 class
	flag <- floor(pnorm(SR)*10)-4
	flag[flag < -4] <- -4
	# buy one share at time t-1
	tempposition <- c(0, flag[1:length(flag)-1])
	position <- matrix(c(position, tempposition), nrow =142, ncol =i)
}


forcastingret <- ret[51:dim(ret)[1],]
classvalue <- NULL
totalreturn <- NULL
# classvalue is the return in a specific class
for (k in -4:5)
{
	tempclassvalue <- NULL
	num <- 0
	for (l in 1:142)
	{
		y <- forcastingret[l,]
		z <- y[position[l,] == k & !is.na(position[l,])]
		num <- length(z)
		if (num > 0){
			tempclassvalue <- c(tempclassvalue, sum(z,na.rm = TRUE)/num)
		}else{ 
			tempclassvalue <- c(tempclassvalue, 0)
		}
	}
	tempclassvalue[1] <- 0
	classvalue <- matrix(c(classvalue, tempclassvalue), nrow = 142, ncol = k+5)
	totalreturn <- matrix(c(totalreturn, cumprod(1+tempclassvalue)), nrow = 142, ncol = k+5)
}


#----------------------
write.csv(classvalue, "classreturn.csv")
write.csv(totalreturn,"totalreturn.csv")
