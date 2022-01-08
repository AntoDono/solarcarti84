J=float
G='Press enter to continue...'
D=str
B=input
A=print
import batttype as H
try:import ti_system as F
except:pass
try:import os
except:pass
def C():
	try:F.disp_clr()
	except:os.system('cls')
def K():C='. ';B=1;A(D(B)+C+'Calculate solar array area');B+=1;A(D(B)+C+'Calculate Array Voltage');B+=1;A(D(B)+C+'Calculate Amp Hour');B+=1;A(D(B)+C+'Calculate Parallel Batteries');B+=1;A(D(B)+C+'Calculate Power');B+=1;A(D(B)+C+'Calculates Supercharged Voltage');B+=1;A(D(B)+C+'Returns velocity');B+=1;A(D(B)+C+'Brute force best combination for series and parallel')
def L():
	C();A('Battery types: ');G=1;I={}
	for F in H.batteries.keys():A('%d. %s | V: %s AH: %s'%(G,F,D(H.batteries[F]['nominal-voltage']),D(H.batteries[F]['Ah'])));I[G]=F;G+=1
	J=E(B('Select a battery > '));return I[J]
def M():
	C();A('Verbose on?');A('1. Yes');A('2. No');D=E(B('Your response > '))
	if D==1:return True
	return False
def N():
	C();A('Please choose your priority: ');A('1. Get Maximum Voltage');A('2. Get Maximum Amp Hours');A('3. Get Maximum Power');D=E(B('Select your priority > '))
	if D==1:return'voltage'
	elif D==2:return'amp'
	elif D==3:return'power'
def E(response):
	D=response
	try:J(D);return J(D)
	except:C();A('Not an number, press enter to try again.');B(G);I()
def I():
	h='Batteries in series | %f';g='Please input the number of cells: ';C();A('Staten Island SolarCar\n');K();F=E(B('\nSelect an option > '))
	if F==1:import getArea as O;C();H=E(B(g));P=E(B('Please input the area of one cell: '));D=O.getArea(H,P);A('The total area of the solar array is: %f'%D);B(G);C()
	elif F==2:import getArray as Q;C();H=E(B(g));J=E(B('Please input the voltage of one cell: '));D=Q.getArray(H,J);A('The total voltage of the solar array is: %f'%D);B(G);C()
	elif F==3:import getPAB as R;C();S=E(B('Please input the battery voltage: '));D=R.getPAB(S);A('The resulted amp hour is: %f'%D);B(G);C()
	elif F==4:import getPara as T;C();U=E(B('Please input the battery amp hour: '));V=E(B('Please input the cell amp hour: '));D=T.getPara(U,V);A('The resulted number of batteries needed are: %f'%D);B(G);C()
	elif F==5:import getPow as W;C();X=E(B('Voltage of the whole array: '));Y=E(B('Please input the current: '));D=W.getPow(X,Y);B(G);A('The power is: {result}');C()
	elif F==6:import SCharge as Z;C();J=E(B('Desire voltage: '));D=Z.getSCharge(J);A('The supercharged voltage is: %f'%D);B(G);C()
	elif F==7:import Velocity as a;C();b=E(B('Distance traveled (m): '));c=E(B('Elapsed time (s): '));D=a.getVelocity(b,c);A('The velocity is: %f m/s'%D);B(G);C()
	elif F==8:import brute;C();d=E(B('Please provide the nominal (desired) voltage: '));F=L();e=N();f=M();D=brute.bruteForce(d,F,priority=e,verbose=f);A('Best result found:');A(D);A('===================RESULT=====================');A('Batteries in parallel | %f'%D[0]);A(h%D[1]);A('Total Voltage | %f'%D[-1]);A(h%D[-2]);A('Total power | %f'%D[2]);A('==============================================');B(G)
	I()
I()