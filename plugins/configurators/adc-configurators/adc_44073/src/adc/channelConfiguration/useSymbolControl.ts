import { useContext } from "react";
import {
  PluginConfigContext,
  useStringSymbol,
  useComboSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { ChannelIds } from "./ChannelConfigurationTable";
export type UseSymbolCntrolProps = {
  channelId: ChannelIds;
  MAX_CH_COUNT: number;
};
const useSymbolControl = ({
  channelId,
  MAX_CH_COUNT,
}: UseSymbolCntrolProps) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);

  const positiveInputSymbols = useStringSymbol({
    componentId,
    symbolId:
      channelId?.index < MAX_CH_COUNT
        ? channelId?.positiveInput
        : "ADC_0_POS_INP",
  });
  const negativeSymbol =
    channelId?.index - 1 < 0 || channelId?.index >= MAX_CH_COUNT
      ? 0
      : channelId?.index - 1;

  const negativeInputSymbols = useComboSymbol({
    componentId,
    symbolId: `ADC_${negativeSymbol}_NEG_INP`,
  });

  let disabled =
    channelId?.index < MAX_CH_COUNT
      ? negativeInputSymbols?.value === positiveInputSymbols?.value
      : false;
  const toolTipValue = `${
    negativeInputSymbols?.value
  } is used as negative input of channel ${channelId?.index - 1}`;

  return {
    disabled,
    toolTipValue,
    positiveInputSymbols,
  };
};

export default useSymbolControl;
