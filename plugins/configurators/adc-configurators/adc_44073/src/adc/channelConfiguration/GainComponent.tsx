import React, { useContext } from "react";
import CustomTooltip from "./CustomTooltip";
import { PluginConfigContext, ComboBoxDefault,createClassResolver, DropDownDefault } from "@mplab_harmony/harmony-plugin-client-lib";
import { ChannelIds } from "./ChannelConfigurationTable";
import useSymbolControl from "./useSymbolControl";
import style from "./channelCofiguration.module.css";
const cx = createClassResolver(style);
const GainComponent = (channelId: ChannelIds,MAX_CH_COUNT:number) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { disabled, toolTipValue} = useSymbolControl({channelId,MAX_CH_COUNT});
    return (
      <>
        {disabled === true && (
          <CustomTooltip value={channelId.gain} />
        )}
        <div
          className={channelId.gain}
          data-pr-tooltip={toolTipValue}
        >
          <DropDownDefault
            componentId={componentId}
            symbolId={channelId.gain}
            disabled={disabled}
            hidden={false}
            className={cx("channelWidth")}
          ></DropDownDefault>
        </div>
      </>
    );
};

export default GainComponent;
