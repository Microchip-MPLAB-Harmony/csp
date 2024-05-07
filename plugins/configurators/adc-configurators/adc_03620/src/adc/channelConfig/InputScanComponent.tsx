import React, { useContext } from "react";
import { PluginConfigContext,CheckBox, useBooleanSymbol } from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const InputScanComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const inputScan = useBooleanSymbol({
    componentId,
    symbolId: symbolId.channelInScan,
  });
  return (
    <>
     <CheckBox
        booleanSymbolHook={inputScan}
        hidden={false}
        disabled={false}
      ></CheckBox>
    </>
  );
};

export default InputScanComponent;
