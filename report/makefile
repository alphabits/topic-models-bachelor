report.pdf: report.tex ../bibliography.bib

	pdflatex report.tex
	bibtex report.aux
	pdflatex report.tex
	pdflatex report.tex
	gnome-open report.pdf &
