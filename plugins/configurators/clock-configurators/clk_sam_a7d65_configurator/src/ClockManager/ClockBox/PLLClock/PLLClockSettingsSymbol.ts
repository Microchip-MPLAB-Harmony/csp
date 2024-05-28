export const getPLLClkSettingsSymbol = (tabTitle: string) => {
  let symbols = [
    'CLK_' + tabTitle + '_MUL',
    'CLK_' + tabTitle + '_FRACR',
    'CLK_' + tabTitle + '_DIVPMC',
    'CLK_' + tabTitle + '_EN',
    'CLK_' + tabTitle + '_SS',
    'CLK_' + tabTitle + '_SS_STEP',
    'CLK_' + tabTitle + '_SS_NSTEP'
  ];
  if (tabTitle === 'AUDIOPLL') {
    symbols = symbols.concat(['CLK_AUDIOPLL_DIVIO', 'CLK_AUDIOPLL_ENIOPLLCK']);
  }
  return symbols;
};
