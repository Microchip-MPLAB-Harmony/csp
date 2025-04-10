export const getCrstalSettingsSymbol = (instanceNumber: string) => {
  let symbols = [
    'CONFIG_CLOCK_XOSC' + instanceNumber + '_ENABLE',
    'XOSC' + instanceNumber + '_ENALC',
    'XOSC' + instanceNumber + '_LOWBUFGAIN',
    'XOSC' + instanceNumber + '_SWBEN',
    'XOSC' + instanceNumber + '_OSCILLATOR_MODE',
    'CONFIG_CLOCK_XOSC' + instanceNumber + '_FREQUENCY',
    'CONFIG_CLOCK_XOSC' + instanceNumber + '_ONDEMAND',
    'CONFIG_CLOCK_XOSC' + instanceNumber + '_STARTUP',
    'CONFIG_CLOCK_XOSC' + instanceNumber + '_RUNSTDBY',
    'CONFIG_CLOCK_XOSC' + instanceNumber + '_CFDEN',
    'CONFIG_CLOCK_XOSC' + instanceNumber + '_CFDPRESC'
  ];
  return symbols;
};
