import React, { useContext } from "react";
import CustomTooltip from "./CustomTooltip";
import { PluginConfigContext, ComboBoxDefault,createClassResolver } from "@mplab_harmony/harmony-plugin-client-lib";
import { ChannelIds } from "./ChannelConfigurationTable";
import useSymbolControl from "./useSymbolControl";
import style from "./channelCofiguration.module.css";
const cx = createClassResolver(style);
const NegativeInputComponent = (channelId: ChannelIds,MAX_CH_COUNT:number) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { disabled, toolTipValue} = useSymbolControl({channelId,MAX_CH_COUNT});
  if (channelId?.index < MAX_CH_COUNT)
    return (
      <>
        {disabled === true && (
          <CustomTooltip value={channelId.negativeInput} />
        )}
        <div
          className={channelId.negativeInput}
          data-pr-tooltip={toolTipValue}
        >
          <ComboBoxDefault
            componentId={componentId}
            symbolId={channelId.negativeInput}
            disabled={disabled}
            hidden={false}
            className={cx("channelWidth")}
          ></ComboBoxDefault>
        </div>
      </>
    );
};

export default NegativeInputComponent;
