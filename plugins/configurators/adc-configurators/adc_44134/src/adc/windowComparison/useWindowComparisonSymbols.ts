import { useContext } from "react";
import {
  useKeyValueSetSymbol,
  PluginConfigContext,
  useBooleanSymbol,
  useComboSymbol,
  useIntegerSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useWindowComparisonSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const comparisonType = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_EMR_CMPTYPE",
  });
  const comparisonMode = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_EMR_CMPMODE",
  });
  const windowComparisonBoolean = useBooleanSymbol({
    componentId,
    symbolId: "ADC_COMP_WINDOW",
  });
  const interrupt = useBooleanSymbol({
    componentId,
    symbolId: "ADC_IER_COMPE",
  });
  const channelCombo = useComboSymbol({
    componentId,
    symbolId: "ADC_EMR_CMPSEL",
  });
  const vlo = useIntegerSymbol({
    componentId,
    symbolId: "ADC_CWR_LOWTHRES_VALUE",
  });
  const vhi = useIntegerSymbol({
    componentId,
    symbolId: "ADC_CWR_HIGHTHRES_VALUE",
  });
  return {
    comparisonMode,
    comparisonType,
    windowComparisonBoolean,
    interrupt,
    channelCombo,
    vlo,
    vhi,
  };
};

export default useWindowComparisonSymbols;
