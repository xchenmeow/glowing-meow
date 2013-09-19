# library('quantmod')
# library('rugarch')

spec <- ugarchspec(
  variance.model = list(model = "csGARCH"),
  mean.model=list(armaOrder = c(0,0), include.mean = FALSE)
  )

getSymbols('SPX', from='1985-01-01')
spx.level <- SPX[,6]

head(spx.level)
plot(spx.level)

spx.return = dailyReturn(x=spx.level, type='log')

plot(spx.return)

hist(x=spx.return, breaks=100, freq=FALSE)

window.size <- 2520
coef.df <- data.frame()
likelihoods <- list()
for (i in 2 : (length(spx.return)-window.size+1))
{
  data = spx.return[i : (i+window.size-1), ]
  fit = ugarchfit(spec=spec, data=data, solver="gosolnp")
  coef.df <- rbind(coef.df, coef(fit))
  likelihoods <- c(likelihoods, likelihood(fit))
}