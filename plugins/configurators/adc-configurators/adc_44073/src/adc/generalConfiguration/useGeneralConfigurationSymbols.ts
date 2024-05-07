import { useContext } from "react";
import {
  useKeyValueSetSymbol,
  PluginConfigContext,
  useIntegerSymbol,
  useBooleanSymbol,
  useComboSymbol,
  useCommentSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useGenerealConfigurationSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const clockFrequency = useIntegerSymbol({
    componentId,
    symbolId: "ADC_CLK",
  });
  const clockFrequencyWarning = useCommentSymbol({
    componentId,
    symbolId: "ADC_PRESCAL_WARNING",
  });
  const sleepMode = useBooleanSymbol({
    componentId,
    symbolId: "ADC_MR_SLEEP",
  });
  const fastWakeUp = useComboSymbol({
    componentId,
    symbolId: "ADC_MR_FWUP",
  });
  const prescaler = useIntegerSymbol({
    componentId,
    symbolId: "ADC_MR_PRESCAL",
  });
  const resultSign = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_EMR_SIGNMODE_VALUE",
  });
  return {
    resultSign,
    prescaler,
    clockFrequency,
    clockFrequencyWarning,
    sleepMode,
    fastWakeUp,
  };
};

export default useGenerealConfigurationSymbols;
