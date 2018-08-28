for file in $(echo *.txt); do
	gnuplot << EOF
	set terminal pngcairo
	set output "${file}-panel.png"
	set datafile separator "\t"
	load "Dark2.plt"
	set decimalsign locale
	set key off
	set multiplot layout 1, 2 ;
	set xrange [-5:50]
	set yrange [-10:55]
	set xlabel "Time (s)"
	set ylabel "Response (RU)"
		
	plot for[n=2:12:2] "${file}" u 1:n w lines ls n+1%8 lw 3 
	set xrange[*:*]
	set yrange [-10:55]
	set xtics 0.0006
	set xlabel "Concentration (M)"
	set ylabel "Response (RU)"
	set format x "%4.1E"
	plot "${file}.ssa" using 1:2 pt 7 ps 3, "" using 3:4 with lines ls 1 lw 3
	unset multiplot
EOF
done
