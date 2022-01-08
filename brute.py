b=False
Q=range
M=print
from getPAB import getPAB as Z
import getPres as a
from math import floor as P
def J(batteries,volt_or_ah):return batteries*volt_or_ah
def bruteForce(nominal_voltage,battery_type,priority='power',verbose=b):
	Y=True;X='nominal-voltage';W='Ah';S=verbose;R=priority;N=nominal_voltage;C=a.getPres(battery_type)
	if not C:return'Invalid Battery Type'
	T=Z(N);G=P(T/C[W]);H=P(N/C[X]);A=[G,H,J(G,C[W])*J(H,C[X]),T,N];O=round(min(G,H)/2+1)
	for E in Q(0,5):
		if E==0:F=1;D=1
		elif E==1:F=1;D=-1
		elif E==2:F=-1;D=1
		elif E==3:F=0;D=1
		elif E==4:F=1;D=0
		I=G;B=H
		if S:M('Current scenario: %f | PC: %f | SC: %f'%(E,F,D))
		for c in Q(0,O):
			I+=F
			for d in Q(0,O):
				B+=D;U=J(B,C[X]);V=J(I,C[W]);K=U*V
				if S:M('Series: %f | Parallel: %f | Power: %f'%(B,I,K))
				if K<=5000:
					L=b
					if A[2]<K:
						if R=='amp'and A[1]<B:L=Y
						elif R=='voltage'and A[1]<B:L=Y
						else:L=Y
					if L:A[0]=I;A[1]=B;A[2]=K;A[3]=V;A[4]=U;M('Found new maximum combination: ');M(A)
			B-=O*D
		I=G;B=H
	return A
def B():return'Brute force best combination for series and parallel'