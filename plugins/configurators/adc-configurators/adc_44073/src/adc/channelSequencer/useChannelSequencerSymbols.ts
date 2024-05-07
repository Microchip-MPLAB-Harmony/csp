import { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  integerSymbolApi,
  useBooleanSymbol,
  useIntegerSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
const useChannelSequencerSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [totalPins, setTotalPins] = useState(0);
  const [symbolIds, setSymbolId] = useState<string[]>([]);
  const isChannelSequencer = useBooleanSymbol({
    componentId,
    symbolId: "ADC_MR_USEQ",
  });
  useEffect(() => {
    integerSymbolApi
      .getValue(componentId, "ADC_CHANNEL_SEQ_NUM")
      .then((e) => setTotalPins(e));
  }, []);
  
  useEffect(() => {
    const symbolId: string[] = Array.apply(null, Array(totalPins)).map(
      (e, i) => "ADC_SEQR1_USCH" + (i + 1)
    );
    setSymbolId(symbolId);
  }, [totalPins]);

  const userChannelCount = useIntegerSymbol({
    componentId,
    symbolId: "ADC_CHANNEL_SEQ_NUM",
  });

  return {
    symbolIds,
    userChannelCount,
    isChannelSequencer,
  };
};

export default useChannelSequencerSymbols;
