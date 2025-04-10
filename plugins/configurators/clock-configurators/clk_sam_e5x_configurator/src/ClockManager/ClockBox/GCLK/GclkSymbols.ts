export const getGclockSymbols = (index: string) => {
  let symbols = [
    "GCLK_INST_NUMX",
    "GCLK_X_RUNSTDBY",
    "GCLK_IO_X_FREQ",
    "GCLK_X_SRC",
    "GCLK_X_OUTPUTENABLE",
    "GCLK_X_OUTPUTOFFVALUE",
    "GCLK_IN_X_FREQ",
    "GCLK_X_DIVSEL",
    "GCLK_X_DIV",
    "GCLK_X_IMPROVE_DUTYCYCLE",
    "GCLK_X_FREQ",
  ];

  if (index === "8" || index === "9" || index === "10" || index === "11") {
    symbols = [
      "GCLK_INST_NUMX",
      "GCLK_X_RUNSTDBY",
      "GCLK_X_SRC",
      "GCLK_X_DIVSEL",
      "GCLK_X_DIV",
      "GCLK_X_IMPROVE_DUTYCYCLE",
      "GCLK_X_FREQ",
    ];
  }

  for (let i = 0; i < symbols.length; i++) {
    symbols[i] = symbols[i].replace("X", index);
  }

  return symbols;
};
