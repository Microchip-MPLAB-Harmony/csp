import { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  symbolUtilApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
export type ADCModule = {
  name: string;
  moduleId: number;
};

export type SymbolId = {
  channelEnable: string;
  inputSelect: string;
  clockDivider: string;
  tad: string;
  resolution: string;
  sampleCount: string;
  conversionRate: string;
  triggerSource: string;
  inputScan: string;
  signMode: string;
  diffMode: string;
  interrupt: string;
};
const sharedModuleId = 7
const useADCModuleConfig = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [adcModules, setAdcModules] = useState<ADCModule[]>([]);

  useEffect(() => {
    symbolUtilApi
      .getChildren(componentId, "ADCHS_DEDICATED_ADC_CONF")
      .then((module: string[]) => {
        let adcModuleLis = module.map((value, index) => {
          let adcModule = value.split("_").join(" ");
          return { name: adcModule, moduleId: index };
        });
        setAdcModules([
          ...adcModuleLis,
          { name: "ADCHS 7 ENABLE", moduleId: sharedModuleId },
        ]);
      });
  }, [componentId]);
  const getDedicatedSymbolIds = (value: number) => {
    return {
      channelEnable: `ADCHS_${value}_ENABLE`,
      inputSelect: `ADCTRGMODE__SH${value}ALT`,
      clockDivider: `ADC${value}TIME__ADCDIV`,
      tad: `ADCHS_TADC${value}`,
      resolution: `ADC${value}TIME__SELRES`,
      sampleCount: `ADC${value}TIME__SAMC`,
      conversionRate: `ADCHS_CONV_RATE${value}`,
      triggerSource: `ADCTRG1__TRGSRC${value}`,
      inputScan: `ADCCSS1__CSS${value}`,
      signMode: `ADCIMCON1__SIGN${value}`,
      diffMode: `ADCIMCON1__DIFF${value}`,
      interrupt: `ADCGIRQEN1__AGIEN${value}`,
    };
  };
  const getSharedSymbolIds = (value:number) => {
    return {
        channelEnable: `ADCHS_${value}_ENABLE`,
        inputSelect: `ADCTRGMODE__SH${value}ALT`,
        clockDivider: `ADCCON2__ADCDIV`,
        tad: `ADCHS_TADC${value}`,
        resolution: `ADCCON1__SELRES`,
        sampleCount: `ADCCON2__SAMC`,
        conversionRate: `ADCHS_CONV_RATE${value}`,
        triggerSource: `ADCCON1__STRGSRC`,
        inputScan: `ADCCSS1__CSS${value}`,
        signMode: `ADCIMCON1__SIGN${value}`,
        diffMode: `ADCIMCON1__DIFF${value}`,
        interrupt: `ADCGIRQEN1__AGIEN${value}`,
      };
  };
  return {
    adcModules,
    getDedicatedSymbolIds,
    getSharedSymbolIds,
    sharedModuleId
  };
};

export default useADCModuleConfig;
