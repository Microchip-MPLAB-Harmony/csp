import React, { useContext } from "react";
import CustomTooltip from "./CustomTooltip";
import { PluginConfigContext, CheckBoxDefault } from "@mplab_harmony/harmony-plugin-client-lib";
import { ChannelIds } from "./ChannelConfigurationTable";
import useSymbolControl from "./useSymbolControl";

const EnableComponent = (channelId: ChannelIds,MAX_CH_COUNT:number) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { disabled, toolTipValue } = useSymbolControl({channelId,MAX_CH_COUNT});
  return (
    <>
      {disabled === true && <CustomTooltip value={channelId.enable} />}
      <div className={channelId.enable} data-pr-tooltip={toolTipValue}>
        <CheckBoxDefault
          componentId={componentId}
          symbolId={channelId.enable}
          disabled={disabled}
          hidden={false}
        ></CheckBoxDefault>
      </div>
    </>
  );
};

export default EnableComponent;
