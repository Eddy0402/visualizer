clear
reset

bin(x)=0.000005*floor(x/0.000005)

plot 'context_switch_time.txt' using (bin($1)):(1) smooth frequency with boxes
