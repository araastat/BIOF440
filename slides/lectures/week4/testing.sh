infile=$1
outfile=$2
if [ -z $3]
then
	scale='50%'
else
	scale=$3
fi
echo $scale
jupyter nbconvert --to markdown $infile
sed -e 's/^# /---@class:middle,center,inverse@@# /' ${infile/ipynb/md} | \
	sed -e 's/^## /---@@## /' | \
 	sed -e "s/\[png\]/[:scale ${scale}]/" | \
 	tr '@' '\n' > $outfile
#Rscript -e "pacman::p_load('xaringan'); rmarkdown::render('${outfile}')"
#open ${outfile/Rmd/html}

