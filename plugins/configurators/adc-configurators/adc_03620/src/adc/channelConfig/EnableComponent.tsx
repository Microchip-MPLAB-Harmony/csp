import React, { useContext } from "react";
import { PluginConfigContext,CheckBox, useBooleanSymbol } from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const EnableComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const channelInterrupt = useBooleanSymbol({
    componentId,
    symbolId: symbolId.enable,
  });
  return (
    <>
     <CheckBox
        booleanSymbolHook={channelInterrupt}
        hidden={false}
        disabled={false}
      ></CheckBox>
    </>
  );
};

export default EnableComponent;
