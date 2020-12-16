library("tm")
library("SnowballC")
library("wordcloud2")

print("Parsing words...")

test <- readLines("scrolled_text.txt")

docs1 <- VCorpus(VectorSource(test))

# inspect(docs1)

removings <- read.csv("removings.csv",header=FALSE)
container <- c()

for i in 1:nrow(removings) {
    container <- append(container,removings[i,2])
}



toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))

docs1 <- tm_map(docs1, content_transformer(tolower))
docs1 <- tm_map(docs1, removeNumbers)
docs1 <- tm_map(docs1, removeWords, stopwords("english"))
docs1 <- tm_map(docs1, removeWords, c("s","d","ve","t","m","re")) #remainder
docs1 <- tm_map(docs1, removeWords, container) #removings
# docs1 <- tm_map(docs1, removePunctuation)
docs1 <- tm_map(docs1, stripWhitespace)
# docs1 <- tm_map(docs1, stemDocument)

dtm <- TermDocumentMatrix(docs1)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d1 <- data.frame(word = names(v),freq=v)

print("Making a wordcloud")

# install.packages("webshot")
# webshot::install_phantomjs()
hw <- wordcloud2(d1, size = 1, minRotation = -pi/2, maxRotation = -pi/2)
saveWidget(hw,"wordcloud.html",selfcontained = F)

print("Wordcloud successfully created!")


# barplot(d1[1:20,]$freq, las = 2, names.arg = d1[1:20,]$word,
#         col ="lightblue", main ="Most frequent words",
#         ylab = "Word frequencies")
