import CustomTooltip from "./CustomTooltip";
import { ChannelIds } from "./ChannelConfigurationTable";
import useSymbolControl from "./useSymbolControl";

const PositiveInputComponent = (channelId: ChannelIds,MAX_CH_COUNT:number) => {
  const { disabled, toolTipValue, positiveInputSymbols } = useSymbolControl({channelId,MAX_CH_COUNT});
  if (channelId?.index < MAX_CH_COUNT)
    return (
      <>
        {disabled === true && (
          <CustomTooltip value={channelId.positiveInput} />
        )}
        <div
          className={channelId.positiveInput}
          data-pr-tooltip={toolTipValue}
        >
          {positiveInputSymbols.value}
        </div>
      </>
    );
};

export default PositiveInputComponent;
