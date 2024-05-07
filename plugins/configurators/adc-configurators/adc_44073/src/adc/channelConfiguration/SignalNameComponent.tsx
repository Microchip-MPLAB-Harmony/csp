import React, { useContext } from "react";
import CustomTooltip from "./CustomTooltip";
import { PluginConfigContext, InputTextDefault } from "@mplab_harmony/harmony-plugin-client-lib";
import { ChannelIds } from "./ChannelConfigurationTable";
import useSymbolControl from "./useSymbolControl";

const SignalNameComponent = (channelId: ChannelIds,MAX_CH_COUNT:number) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { disabled, toolTipValue } = useSymbolControl({channelId,MAX_CH_COUNT});
  return (
    <>
      {disabled === true && <CustomTooltip value={channelId.signalName} />}
      <div className={channelId.signalName} data-pr-tooltip={toolTipValue}>
        <InputTextDefault
          componentId={componentId}
          symbolId={channelId.signalName}
          disabled={disabled}
          hidden={false}
        ></InputTextDefault>
      </div>
    </>
  );
};

export default SignalNameComponent;
