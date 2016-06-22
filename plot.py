from numpy import linspace, pi, exp, sin, cos, loadtxt, savetxt, mean, zeros, size, log, sum, sqrt, arctan, diag, array, std, genfromtxt
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Ausgabe von 5 Trajektorien für jede Antriebskraft

zeit,x1, y1 = loadtxt('data1/data_0_1.txt', unpack=True);
zeit,x2, y2 = loadtxt('data1/data_0_2.txt', unpack=True);
zeit,x3, y3 = loadtxt('data1/data_0_3.txt', unpack=True);
zeit,x4, y4 = loadtxt('data1/data_0_4.txt', unpack=True);
zeit,x5, y5 = loadtxt('data1/data_0_5.txt', unpack=True);

plt.plot(x1,y1, 'b-', label='Messung 1')
plt.plot(x2,y2, 'g-', label='Messung 2')
plt.plot(x3,y3, 'r-', label='Messung 3')
plt.plot(x4,y4, 'c-', label='Messung 4')
plt.plot(x5,y5, 'm-', label='Messung 5')
plt.grid()
plt.legend(loc="best")
plt.xlabel('x-Komponente')
plt.ylabel('y-Komponente')
plt.tight_layout()
#plt.show()
plt.savefig('trajektorie_0.pdf')
plt.clf()

zeit,x1, y1 = loadtxt('data1/data_25_1.txt', unpack=True);
zeit,x2, y2 = loadtxt('data1/data_25_2.txt', unpack=True);
zeit,x3, y3 = loadtxt('data1/data_25_3.txt', unpack=True);
zeit,x4, y4 = loadtxt('data1/data_25_4.txt', unpack=True);
zeit,x5, y5 = loadtxt('data1/data_25_5.txt', unpack=True);

plt.plot(x1,y1, 'b-', label='Messung 1')
plt.plot(x2,y2, 'g-', label='Messung 2')
plt.plot(x3,y3, 'r-', label='Messung 3')
plt.plot(x4,y4, 'c-', label='Messung 4')
plt.plot(x5,y5, 'm-', label='Messung 5')
plt.grid()
plt.legend(loc="best")
plt.xlabel('x-Komponente')
plt.ylabel('y-Komponente')
plt.tight_layout()
#plt.show()
plt.savefig('trajektorie_25.pdf')
plt.clf()

zeit,x1, y1 = loadtxt('data1/data_50_1.txt', unpack=True);
zeit,x2, y2 = loadtxt('data1/data_50_2.txt', unpack=True);
zeit,x3, y3 = loadtxt('data1/data_50_3.txt', unpack=True);
zeit,x4, y4 = loadtxt('data1/data_50_4.txt', unpack=True);
zeit,x5, y5 = loadtxt('data1/data_50_5.txt', unpack=True);

plt.plot(x1,y1, 'b-', label='Messung 1')
plt.plot(x2,y2, 'g-', label='Messung 2')
plt.plot(x3,y3, 'r-', label='Messung 3')
plt.plot(x4,y4, 'c-', label='Messung 4')
plt.plot(x5,y5, 'm-', label='Messung 5')
plt.grid()
plt.legend(loc="best")
plt.xlabel('x-Komponente')
plt.ylabel('y-Komponente')
plt.tight_layout()
#plt.show()
plt.savefig('trajektorie_50.pdf')
plt.clf()

zeit,x1, y1 = loadtxt('data1/data_75_1.txt', unpack=True);
zeit,x2, y2 = loadtxt('data1/data_75_2.txt', unpack=True);
zeit,x3, y3 = loadtxt('data1/data_75_3.txt', unpack=True);
zeit,x4, y4 = loadtxt('data1/data_75_4.txt', unpack=True);
zeit,x5, y5 = loadtxt('data1/data_75_5.txt', unpack=True);

plt.plot(x1,y1, 'b-', label='Messung 1')
plt.plot(x2,y2, 'g-', label='Messung 2')
plt.plot(x3,y3, 'r-', label='Messung 3')
plt.plot(x4,y4, 'c-', label='Messung 4')
plt.plot(x5,y5, 'm-', label='Messung 5')
plt.grid()
plt.legend(loc="best")
plt.xlabel('x-Komponente')
plt.ylabel('y-Komponente')
plt.tight_layout()
#plt.show()
plt.savefig('trajektorie_75.pdf')
plt.clf()

zeit,x1, y1 = loadtxt('data1/data_100_1.txt', unpack=True);
zeit,x2, y2 = loadtxt('data1/data_100_2.txt', unpack=True);
zeit,x3, y3 = loadtxt('data1/data_100_3.txt', unpack=True);
zeit,x4, y4 = loadtxt('data1/data_100_4.txt', unpack=True);
zeit,x5, y5 = loadtxt('data1/data_100_5.txt', unpack=True);

plt.plot(x1,y1, 'b-', label='Messung 1')
plt.plot(x2,y2, 'g-', label='Messung 2')
plt.plot(x3,y3, 'r-', label='Messung 3')
plt.plot(x4,y4, 'c-', label='Messung 4')
plt.plot(x5,y5, 'm-', label='Messung 5')
plt.grid()
plt.legend(loc="best")
plt.xlabel('x-Komponente')
plt.ylabel('y-Komponente')
plt.tight_layout()
#plt.show()
plt.savefig('trajektorie_100.pdf')
plt.clf()


##########################################################################################
#Ausgabe des Abstandsquadrats und linearer Fit für jede Antriebskraft

def func(x,a,b):
	return a*x+b
l=linspace(0, 100);


zeit,abstandsquadrat = loadtxt('data2/abstandsquadrat_0.txt', unpack=True);

params, covariance = curve_fit(func, zeit, abstandsquadrat)
errors = sqrt(diag(covariance))	
print(' a0=', params[0], '+-', errors[0])
#print(' b0=', params[1], '+-', errors[1])
plt.plot(l, func(l, *params), 'b-', label='Lineare Regression')
plt.plot(zeit,abstandsquadrat, 'r.', label='Messung')
plt.grid()
plt.legend(loc="best")
plt.xlabel('Zeit')
plt.ylabel('$<(\\vec{r}(\\Delta t)-\\vec{r}(0))^2>$')
plt.tight_layout()
#plt.show()
plt.savefig('abstandsquadrat_0.pdf')
plt.clf()
	
zeit,abstandsquadrat = loadtxt('data2/abstandsquadrat_25.txt', unpack=True);

params, covariance = curve_fit(func, zeit, abstandsquadrat)
errors = sqrt(diag(covariance))	
print(' a25=', params[0], '+-', errors[0])
#print(' b25=', params[1], '+-', errors[1])
plt.plot(l, func(l, *params), 'b-', label='Lineare Regression')
plt.plot(zeit,abstandsquadrat, 'r.', label='Messung')
plt.grid()
plt.legend(loc="best")
plt.xlabel('Zeit')
plt.ylabel('$<(\\vec{r}(\\Delta t)-\\vec{r}(0))^2>$')
plt.tight_layout()
#plt.show()
plt.savefig('abstandsquadrat_25.pdf')
plt.clf()
	
zeit,abstandsquadrat = loadtxt('data2/abstandsquadrat_50.txt', unpack=True);

params, covariance = curve_fit(func, zeit, abstandsquadrat)
errors = sqrt(diag(covariance))	
print(' a50=', params[0], '+-', errors[0])
#print(' b50=', params[1], '+-', errors[1])
plt.plot(l, func(l, *params), 'b-', label='Lineare Regression')
plt.plot(zeit,abstandsquadrat, 'r.', label='Messung')
plt.grid()
plt.legend(loc="best")
plt.xlabel('Zeit')
plt.ylabel('$<(\\vec{r}(\\Delta t)-\\vec{r}(0))^2>$')
plt.tight_layout()
#plt.show()
plt.savefig('abstandsquadrat_050.pdf')
plt.clf()
	
zeit,abstandsquadrat = loadtxt('data2/abstandsquadrat_75.txt', unpack=True);

params, covariance = curve_fit(func, zeit, abstandsquadrat)
errors = sqrt(diag(covariance))	
print(' a75=', params[0], '+-', errors[0])
#print(' b75=', params[1], '+-', errors[1])
plt.plot(l, func(l, *params), 'b-', label='Lineare Regression')
plt.plot(zeit,abstandsquadrat, 'r.', label='Messung')
plt.grid()
plt.legend(loc="best")
plt.xlabel('Zeit')
plt.ylabel('$<(\\vec{r}(\\Delta t)-\\vec{r}(0))^2>$')
plt.tight_layout()
#plt.show()
plt.savefig('abstandsquadrat_75.pdf')
plt.clf()
	
zeit,abstandsquadrat = loadtxt('data2/abstandsquadrat_100.txt', unpack=True);

params, covariance = curve_fit(func, zeit, abstandsquadrat)
errors = sqrt(diag(covariance))	
print(' a100=', params[0], '+-', errors[0])
#print(' b100=', params[1], '+-', errors[1])
plt.plot(l, func(l, *params), 'b-', label='Lineare Regression')
plt.plot(zeit,abstandsquadrat, 'r.', label='Messung')
plt.grid()
plt.legend(loc="best")
plt.xlabel('Zeit')
plt.ylabel('$<(\\vec{r}(\\Delta t)-\\vec{r}(0))^2>$')
plt.tight_layout()
#plt.show()
plt.savefig('abstandsquadrat_100.pdf')
plt.clf()
	
