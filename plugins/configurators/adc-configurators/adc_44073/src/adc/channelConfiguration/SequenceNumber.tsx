import CustomTooltip from "./CustomTooltip";
import { ChannelIds } from "./ChannelConfigurationTable";
import useSymbolControl from "./useSymbolControl";

const SequenceNumber = (channelId: ChannelIds, MAX_CH_COUNT: number) => {
  const { disabled, toolTipValue } = useSymbolControl({
    channelId,
    MAX_CH_COUNT,
  });
  return (
    <>
      {disabled === true && <CustomTooltip value={channelId.channel} />}
      <div className={channelId.channel} data-pr-tooltip={toolTipValue}>
        {channelId.channel}
      </div>
    </>
  );
};

export default SequenceNumber;
