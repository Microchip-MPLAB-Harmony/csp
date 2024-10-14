export const getPeripheralBusClockSymbols = (index: string) => {
  let symbols = ['CONFIG_SYS_CLK_PBCLK' + index + '_ENABLE', 'CONFIG_SYS_CLK_PBDIV' + index];
  return symbols;
};
