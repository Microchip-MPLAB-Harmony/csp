export const getFDPLLSettingsSymbol = (instanceNumber: string) => {
  let symbols = [
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_ENABLE',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_ONDEMAND',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_RUNSTDY',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_LDR_INTEGER',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_LDRFRAC_FRACTION',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_LOCK_BYPASS',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_DCOEN',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_DCOFILTER',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_WAKEUP_FAST',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_FILTER',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_REF_CLOCK',
    'CONFIG_CLOCK_DPLL' + instanceNumber + '_DIVIDER'
  ];
  return symbols;
};
