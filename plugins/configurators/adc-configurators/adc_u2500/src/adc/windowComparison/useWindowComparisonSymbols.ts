import { useContext } from "react";
import {
  useKeyValueSetSymbol,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useWindowComparisonSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const comparisonMode = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_CTRLB_WINMODE",
  });
  const vhi = useIntegerSymbol({
    componentId,
    symbolId: "ADC_WINUT",
  });
  const vlo = useIntegerSymbol({
    componentId,
    symbolId: "ADC_WINLT",
  });
  const winmonInterrupt = useBooleanSymbol({
    componentId,
    symbolId: "ADC_INTENSET_WINMON",
  });
  const win = useBooleanSymbol({
    componentId,
    symbolId: "ADC_WINDOW_OUTPUT_EVENT",
  });
  return {
    comparisonMode,
    win,
    winmonInterrupt,
    vlo,
    vhi,
  };
};

export default useWindowComparisonSymbols;
