#include "Eigen/Dense"
#include<fstream>
#include<iostream>
#include<vector>
#include<cmath>
#include <tr1/random>
#include <string>

using namespace std;
using namespace Eigen;

//Diese Datei macht:
//-Random Walk für N Teilchen, Trajektorien-Ausgabe in data/
//-tmax Zeitschritte
//-unterschiedliche Antriebskräfte (0.00, 0.25, 0.50, 0.75, 1.00)
//-Berechnung des Abstandsquadrats, Ausgabe in data2/

//Liste von physikalischen Größen
const double reibung_trans = 0.6; // \sigma
const double staerkebrown_trans = 0.6; // \lambda
const double reibung_rot = 0.2; // \sigma_theta
const double staerkebrown_rot = 1.0; // \lambda_theta

//Numerische Größen
const double h = 0.01; //Zeitschrittweite
const double t0 = 0; //Startzeitpunkt
const double tmax = 100; //Endzeitpunkt
const int N=1000; //Anzahl der simulierten Teilchen

//Random Number generator aus C++11
default_random_engine generator;

//stochastische Krafte, Dimension 1:
//Gibt einen Vektor der Dimension 1 mit gaußverteilten Elementen zurück
//Die Gaußverteilung hat Mittelwert 0 und Varianz staerke/h
//Notwendig für stochastisches Rauschen
Vector2d zufallskraft2(double staerke)
{
	Vector2d kraft;
	normal_distribution<double> distribution(0.0,sqrt(staerke/h));
	kraft << (double)distribution(generator), (double)distribution(generator);
	return 	kraft;
}

//stochastische Krafte, Dimension 1:
//Gibt einen Vektor der Dimension 1 mit gaußverteilten Elementen zurück
//Die Gaußverteilung hat Mittelwert 0 und Varianz staerke/h
//Notwendig für Rotationsdiffusion
double zufallskraft1(double staerke)
{	
	//default_random_engine generator;
	//generator.seed(rdtsc());
	double kraft;
	normal_distribution<double> distribution(0.0,sqrt(staerke/h));
	kraft = (double)distribution(generator);
	return 	kraft;
}

//Orientierung des Teilchens
//Problemdimension 2, Tangentialvektor in Polarkoordinaten-Darstellung
Vector2d richtung(double theta)
{
	Vector2d richtungsvektor;
	richtungsvektor << cos(theta), sin(theta);
	return richtungsvektor;
}

int main()
{
	//Setzen des seeds
	generator.seed(time(NULL));
	
	//Schleife über Antriebskraft
	for (double antriebskraft=0.0; antriebskraft<=1.0; antriebskraft+=0.25)
	{
		//Vektor zur Speicherung des Abstandquadrats
		vector<double> abstandsquadrat;
	
		//füllen mit Nullen, um anschließend Werte aufaddieren zu können
		for(int i=0; i<=tmax/h; i++)
		{
			abstandsquadrat.push_back(0);
		}
	
		//for-Schleife über N Teilchen
		for(int m=1; m<=N; m++)
		{
			//Startvektor
			Vector2d r_0;
			double theta_0;
		
			//Startvektor füllen, Startpunkt im Ursprung, Ausgangsrichtung gleichverteilt
			r_0 << 0, 0;
			uniform_real_distribution<double> gleich(0, 2*M_PI);
			theta_0 = gleich(generator);
		
			//Vektor mit allen Lösungen im jeweiligen Zeitschritt
			vector<Vector2d> r;
			vector<double> theta;
		
			//Startvektor einfügen
			r.push_back(r_0);
			theta.push_back(theta_0);
		
			//Zeitschleife
			for(double t=t0; t<tmax; t+=h)
			{
				//Setzen von r_n und theta_n
				Vector2d r_n = r.back();
				double theta_n = theta.back();
				
				//Erzeugung der stochastischen brownschen Kraft
				Vector2d stochkraft = zufallskraft2(staerkebrown_trans);
				
				//Euler-Verfahren, einfügen von r_n+1 und theta_n+1
				r.push_back(r_n+h/reibung_trans*(stochkraft+antriebskraft*richtung(theta_n)));
				
				theta.push_back(theta_n+h/reibung_rot*zufallskraft1(staerkebrown_rot));
				
				//Addieren des Abstandsquadrats für das Teilchen m zum Zeitpunkt t 
				abstandsquadrat[t/h+1]+=r.back().dot(r.back())/N;
			}	
		
			//Dateiausgabe
			ofstream data1;
			data1.open("data1/data_"+to_string((int) (antriebskraft*100))+"_"+to_string((int)m)+".txt");
			for (int i = 0; i<r.size(); i++)
			{
				data1 << i*h << "\t" << r[i].transpose() << endl;
			}	
			data1.close();
			//Speichern sämtlicher Koordinaten zu jedem Zeitpunkt!
		}
	
		//Dateiausgabe des Abstandsquadrats
		ofstream data2;
		data2.open("data2/abstandsquadrat_"+to_string((int) (antriebskraft*100))+".txt");
		for(int i = 0; i<abstandsquadrat.size(); i++)
		{
			data2 << i*h << "\t" << abstandsquadrat[i] << endl;
		}	
		data2.close();
	}
	return 0;	
}
