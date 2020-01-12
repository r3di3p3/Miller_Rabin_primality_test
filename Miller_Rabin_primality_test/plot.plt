set terminal png large size 800,600
set output "plot1001_withpoints.png"
set title "Nombre des temoins par rapport un entier"
set colorbox user size .03, .6 noborder
set xlabel 'les enties'
set ylabel 'temoins[%]'
set yrange[0:100]
set style fill solid
plot 'outfile0.csv' with points