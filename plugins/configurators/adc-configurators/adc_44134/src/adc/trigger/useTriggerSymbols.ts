import { useContext } from "react";
import {
  useKeyValueSetSymbol,
  PluginConfigContext,
  useIntegerSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useTriggerSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const triggerMode = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_TRGR_MODE",
  });
  const triggerSelection = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_MR_TRGSEL_VALUE",
  });
  const triggerPeriod = useIntegerSymbol({
    componentId,
    symbolId: "ADC_TRIGGER_TIME",
  });
  return {
    triggerMode,
    triggerSelection,
    triggerPeriod,
  };
};

export default useTriggerSymbols;
