export const getPckClkSettingsSymbol = (tabTitle: string) => {
  let symbols = [
    'CLK_PCK' + tabTitle + '_EN',
    'CLK_PCK' + tabTitle + '_CSS',
    'CLK_PCK' + tabTitle + '_PRES'
  ];

  return symbols;
};
