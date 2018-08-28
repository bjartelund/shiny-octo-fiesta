args=("$@")
python stderr-calc.py ${args[0]}.csv > ${args[0]}.csv.stderrs
gnuplot << EOF
set terminal pngcairo mono
load 'Greys.plt'
set output "${args[0]}.png"
set datafile separator ","
set decimalsign "."
set key off
set yrange [0:129]
set xlabel "Concentration (log M)"
set ylabel "Activity (%)"
plot 100/(1+10**(x-${args[1]})) ls 7 lw 3, "${args[0]}.csv.stderrs" using 1:2:3 with yerrorbars ls 8 lw 3
EOF
