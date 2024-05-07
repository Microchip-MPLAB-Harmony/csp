import { useContext } from "react";
import { PluginConfigContext, useIntegerSymbol } from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const useSymbolControl = (moduleId: number) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);

  const numChannels = useIntegerSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_NUM_CHANNELS`,
  });

  const symbolIds: SymbolIds[] = new Array(numChannels.value)
    .fill(0)
    .map((val, index) => {
      return {
        index: index,
        enable: `ADC_CORE_${moduleId}_CH_${index}_ENABLE`,
        enableSigneData: `ADC_CORE_${moduleId}_CH_${index}_CHNCFG3_SIGN`,
        channelInScan: `ADC_CORE_${moduleId}_CH_${index}_CHNCFG2_CSS`,
        mode: `ADC_CORE_${moduleId}_CH_${index}_CHNCFG3_DIFF`,
        triggerSource: `ADC_CORE_${moduleId}_CH_${index}_CHNCFG4_5_TRGSRC`,
        enableInterrupt: `ADC_CORE_${moduleId}_CH_${index}_INTENSET_CHRDY`,
      };
    });

  return {
    symbolIds,
  };
};

export default useSymbolControl;
