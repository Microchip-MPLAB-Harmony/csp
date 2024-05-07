import React, { useContext } from "react";
import {
  PluginConfigContext,
  useKeyValueSetSymbol,
  DropDown,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const TriggerSourceComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const triggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId: symbolId.triggerSource,
  });
  return (
    <>
      <DropDown
        keyValueSetSymbolHook={triggerSource}
        hidden={false}
      ></DropDown>
    </>
  );
};

export default TriggerSourceComponent;
