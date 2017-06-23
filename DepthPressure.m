


function DepthPressure();
  display('pressures are differential from sea level')
  depth_meters = input("input the depth in meters: ");
  pressure_atm = depth_meters/10;
  pressure_psi = depth_meters/10*14.7;
  pressure_kPa = depth_meters/10*101.3;
  display(['pressure (atm):', num2str(pressure_atm)])
  display(['pressure (psi):', num2str(pressure_psi)])
  display(['pressure (kPa):', num2str(pressure_kPa)])
return 