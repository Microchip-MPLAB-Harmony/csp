export const getGclockSymbols = (index: string) => {
  let symbols = [
    'GCLK_INST_NUM' + index,
    'GCLK_' + index + '_RUNSTDBY',
    'GCLK_IO_' + index + '_FREQ',
    'GCLK_' + index + '_SRC',
    'GCLK_' + index + '_OUTPUTOFFVALUE',
    'GCLK_IN_' + index + '_FREQ',
    'GCLK_' + index + '_DIVSEL',
    'GCLK_' + index + '_DIV',
    'GCLK_' + index + '_IMPROVE_DUTYCYCLE',
    'GCLK_' + index + '_OUTPUTENABLE',
    'GCLK_' + index + '_FREQ'
  ];

  if (parseInt(index) >= 8 && parseInt(index) <= 15) {
    symbols = [
      'GCLK_INST_NUM' + index,
      'GCLK_' + index + '_RUNSTDBY',
      'GCLK_' + index + '_SRC',
      'GCLK_' + index + '_DIVSEL',
      'GCLK_' + index + '_DIV',
      'GCLK_' + index + '_IMPROVE_DUTYCYCLE',
      'GCLK_' + index + '_FREQ'
    ];
  }

  return symbols;
};
