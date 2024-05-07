import { useContext } from "react";
import { PluginConfigContext, useIntegerSymbol } from "@mplab_harmony/harmony-plugin-client-lib";
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
const useADCModuleConfig = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const ADC_NUM_SAR_CORES = useIntegerSymbol({
    componentId,
    symbolId: "ADC_NUM_SAR_CORES",
  }); //adc core list
  const adcModules: ADCModule[] = new Array(ADC_NUM_SAR_CORES.value)
    .fill(0)
    .map((val, index) => {
      let adcModule = `ADC CORE ${index}`;
      return { name: adcModule, moduleId: index };
    });

  const ADC_MAX_CHANNELS = useIntegerSymbol({
    componentId,
    symbolId: "ADC_MAX_CHANNELS",
  }); //adc core list

  return {
    adcModules,
    ADC_MAX_CHANNELS,
  };
};

export default useADCModuleConfig;
