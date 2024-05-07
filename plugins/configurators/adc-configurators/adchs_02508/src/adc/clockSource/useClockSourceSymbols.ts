import { useContext } from "react";
import {
  useKeyValueSetSymbol,
  PluginConfigContext,
  useIntegerSymbol,
  useFloatSymbol,
  useLongSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useClockSourceSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  
  const controlClockDivider = useLongSymbol({
    componentId,
    symbolId: "ADCCON3__CONCLKDIV",
  });
  const clockSource = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADCCON3__ADCSEL",
  });
  const labelTCLK = useFloatSymbol({
    componentId,
    symbolId: "ADCHS_TCLK",
  });
  const labelTQ = useFloatSymbol({
    componentId,
    symbolId: "ADCHS_TQ",
  });
  const frequency = useIntegerSymbol({
    componentId:'core',
    symbolId: "ADCHS_CLOCK_FREQUENCY",
  });
  const clkFreq = (frequency.value === 0)?0:((1.0/frequency.value) * 1000000000)

  return {
    controlClockDivider,
    clockSource,
    labelTQ,
    labelTCLK,
    clkFreq,frequency
  };
};

export default useClockSourceSymbols;
