export const getMckClkSettingsSymbol = (tabTitle: string) => {
  let symbols = ['CLK_MCR_MCK' + tabTitle + '_CSS', 'CLK_MCR_MCK' + tabTitle + '_DIV'];

  return symbols;
};
