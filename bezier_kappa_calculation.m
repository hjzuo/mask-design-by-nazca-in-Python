
P0=[0,5000];%width
P1=[2000,5000];
P2=[2000,0];%length
P3=[0,0];



% for i=1:length(t)
%     t1=t(i);
% x(i)=P0(1)*(1-t1)^3+3*P1(1)*t1*(1-t1)^2+3*P2(1)*t1*t1*(1-t1)+P3(1)*t1^3;
% y(i)=P0(2)*(1-t1)^3+3*P1(2)*t1*(1-t1)^2+3*P2(2)*t1*t1*(1-t1)+P3(2)*t1^3;
% end
% 
% plot(x,y)

% derivative                   radius of curvature

syms x;
fx(x)=P0(1)*(1-x)^3+3*P1(1)*x*(1-x)^2+3*P2(1)*x*x*(1-x)+P3(1)*x^3;%horizontal
fy(x)=P0(2)*(1-x)^3+3*P1(2)*x*(1-x)^2+3*P2(2)*x*x*(1-x)+P3(2)*x^3;%vertical

fx1d=diff(fx,x);fx2d=diff(fx,x,2);
fy1d=diff(fy,x);fy2d=diff(fy,x,2);

t=0:0.001:1;
bezier_x=subs(fx,x,t);
bezier_y=subs(fy,x,t);
plot(bezier_x,bezier_y);
hold on; scatter(P0(1),P0(2),'filled');
hold on; scatter(P1(1),P1(2),'filled');
hold on; scatter(P2(1),P2(2),'filled');
hold on; scatter(P3(1),P3(2),'filled');%set(gca,'DataAspectRatio',[1 1 1])
% figure ;plot(t,bezier_x,"-");

%Kappa
p=0.5;
x1=subs(fx1d,x,p);x11=subs(fx2d,x,p);
y1=subs(fy1d,x,p);y11=subs(fy2d,x,p);
k=abs(x1*y11-x11*y1)/(x1^2+y1^2)^1.5;
r=1/k;
vpa(r)


