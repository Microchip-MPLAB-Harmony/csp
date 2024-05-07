import { useContext } from "react";
import {
  useKeyValueSetSymbol,
  PluginConfigContext,
  useIntegerSymbol,
  useCommentSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useAnalogConfigurationSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const resultResolution = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_CTRLB_RESSEL",
  });
  const channelConfigPositve = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_INPUTCTRL_MUXPOS",
  });
  const channelConfigNegative = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_INPUTCTRL_MUXNEG",
  });

  const conversionTime = useCommentSymbol({
    componentId,
    symbolId: "ADC_SAMPCTRL_SAMPLEN_TIME",
  });

  const gain = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_INPUTCTRL_GAIN",
  });

  const reference = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_REFCTRL_REFSEL",
  });
  const sampleLenght = useIntegerSymbol({
    componentId,
    symbolId: "ADC_SAMPCTRL_SAMPLEN",
  });
  return {
    sampleLenght,
    reference,
    gain,
    conversionTime,
    channelConfigNegative,
    channelConfigPositve,
    resultResolution,
  };
};

export default useAnalogConfigurationSymbols;
