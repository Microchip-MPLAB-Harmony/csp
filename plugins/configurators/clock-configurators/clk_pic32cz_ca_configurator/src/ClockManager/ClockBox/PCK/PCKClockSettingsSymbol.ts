export const getPckClkSettingsSymbol = (tabTitle: string) => {
  let symbols = [
    "CONFIG_CLOCK_" + tabTitle + "_ENABLE",
    "CONFIG_CLOCK_" + tabTitle + "_ONDEMAND",
    "CONFIG_CLOCK_" + tabTitle + "_BWSEL",
    "CONFIG_CLOCK_" + tabTitle + "_REF_CLOCK",
    "CONFIG_CLOCK_" + tabTitle + "_PLLFBDIV_FBDIV",
    "CONFIG_CLOCK_" + tabTitle + "_PLLREFDIV_REFDIV",
    "CONFIG_CLOCK_" + tabTitle + "_FRACDIV_INTDIV",
    "CONFIG_CLOCK_" + tabTitle + "_FRACDIV_REMDIV",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_POSTDIV0",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_OUTEN0",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_POSTDIV1",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_OUTEN1",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_POSTDIV2",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_OUTEN2",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_POSTDIV3",
    "CONFIG_CLOCK_" + tabTitle + "_PLLPOSTDIVA_OUTEN3" 
  ];

  return symbols;
};
