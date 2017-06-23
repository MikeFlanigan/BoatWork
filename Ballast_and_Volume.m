% ballast and volume

Volume_Tot = 34; # controllable liters is only 31
Volume_Fillable = 31; 

Air_Volume = linspace(Volume_Tot,Volume_Fillable*.2,20);

Flood_Percent = Volume_Tot./Air_Volume;

Initial_Pressure = 331; # psi

Pump_Pressure = Initial_Pressure*Volume_Tot./Air_Volume;

figure(1)
plot(Air_Volume,Pump_Pressure,'b')

hold on 

Volume_Tot = 50; # controllable liters is only 31
Volume_Fillable = 45; 

Air_Volume = linspace(Volume_Tot,Volume_Fillable*.2,20);

Flood_Percent = Volume_Tot./Air_Volume;

Initial_Pressure = 331; # psi

Pump_Pressure = Initial_Pressure*Volume_Tot./Air_Volume;

plot(Air_Volume,Pump_Pressure,'r')



axis "square"
set(gca,'xtick',[0:5:Volume_Tot+5])
set(gca,'ytick',[0:100:1250])
grid on
axis([0,Volume_Tot+5,0,1250])
xlabel("tank liters flooded")
ylabel("internal pressure")