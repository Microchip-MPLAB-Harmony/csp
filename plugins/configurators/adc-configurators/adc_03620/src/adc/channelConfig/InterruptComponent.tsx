import React, { useContext } from "react";
import {
  PluginConfigContext,
  useBooleanSymbol,
  CheckBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const InterruptComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const enableInterrupt = useBooleanSymbol({
    componentId,
    symbolId: symbolId.enableInterrupt,
  });
  return (
    <>
     <CheckBox
        booleanSymbolHook={enableInterrupt}
        hidden={false}
        disabled={false}
      ></CheckBox>
    </>
  );
};

export default InterruptComponent;
