import { useContext } from "react";
import {
  useKeyValueSetSymbol,
  PluginConfigContext,
  useBooleanSymbol,
  useComboSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useGenerealConfigurationSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const startEvent = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_EVCTRL_START",
  });

  const flushEvent = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_EVCTRL_FLUSH",
  });

  const preScaler = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_CTRLA_PRESCALER",
  });

  const resultInterrupt = useBooleanSymbol({
    componentId,
    symbolId: "ADC_INTENSET_RESRDY",
  });
  const leftAlignResult = useBooleanSymbol({
    componentId,
    symbolId: "ADC_CTRLB_LEFTADJ",
  });
  const runStandby = useBooleanSymbol({
    componentId,
    symbolId: "ADC_CTRLA_RUNSTDBY",
  });
  const resultEvent = useBooleanSymbol({
    componentId,
    symbolId: "ADC_EVCTRL_RESRDYEO",
  });
  const conversionTrigger = useComboSymbol({
    componentId,
    symbolId: "ADC_CONV_TRIGGER",
  });
  const onDemandctrl = useBooleanSymbol({
    componentId,
    symbolId: "ADC_CTRLA_ONDEMAND",
  });
  return {
    conversionTrigger,
    onDemandctrl,
    resultEvent,
    runStandby,
    leftAlignResult,
    resultInterrupt,
    preScaler,
    flushEvent,
    startEvent,
  };
};

export default useGenerealConfigurationSymbols;
