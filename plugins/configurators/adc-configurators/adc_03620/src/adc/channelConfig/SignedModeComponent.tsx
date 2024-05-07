import React, { useContext } from "react";
import { PluginConfigContext, useBooleanSymbol, CheckBox } from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const SignedModeComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const enableSigneData = useBooleanSymbol({
    componentId,
    symbolId: symbolId.enableSigneData,
  });
  return (
    <>
      <CheckBox
        booleanSymbolHook={enableSigneData}
        hidden={false}
        disabled={false}
      ></CheckBox>
    </>
  );
};

export default SignedModeComponent;
