export const getRefClkSettingsSymbol = (instanceNumber: string) => {
  let symbols = [
    'CONFIG_SYS_CLK_CONFIG_REFCLKI_PIN',
    'CONFIG_SYS_CLK_ROTRIM' + instanceNumber,
    'CONFIG_SYS_CLK_RODIV' + instanceNumber,
    'CONFIG_SYS_CLK_REFCLK' + instanceNumber + '_ENABLE',
    'CONFIG_SYS_CLK_REFCLK_SIDL' + instanceNumber,
    'CONFIG_SYS_CLK_REFCLK_RSLP' + instanceNumber,
    'CONFIG_SYS_CLK_REFCLK' + instanceNumber + '_OE'
  ];
  return symbols;
};
