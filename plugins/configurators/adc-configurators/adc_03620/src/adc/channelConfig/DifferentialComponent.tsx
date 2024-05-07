import React, { useContext } from "react";
import {
  PluginConfigContext,
  useComboSymbol,
  ComboBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const DifferentialComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const mode = useComboSymbol({
    componentId,
    symbolId: symbolId.mode,
  });
  return (
    <>
      <ComboBox
        comboSymbolHook={mode}
        hidden={false}
      ></ComboBox>
    </>
  );
};

export default DifferentialComponent;
