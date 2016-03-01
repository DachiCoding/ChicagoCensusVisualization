library(rgdal)
library(ggplot2)
library(maptools)
library(rgeos)
path <- '~/Dropbox/5_Career/Projects/d3_project/data/'
setwd(path)
ogrInfo("chicagogeo.geojson","OGRGeoJSON")
chicago <- readOGR("chicagogeo.geojson","OGRGeoJSON")
census <- read.csv('datause1.csv',header = TRUE, sep = ',')
census$Change_Population <- as.numeric(census$Change_Population)
ggplot() + geom_polygon(data=chicago,aes(x=long,y=lat,group=group),color='green')

