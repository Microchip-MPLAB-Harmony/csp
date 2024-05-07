import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  CheckBoxDefault,
  booleanSymbolApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const InterruptComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [checkbox, setCheckbox] = useState(false);
  useEffect(() => {
    booleanSymbolApi
      .getValue(componentId, symbolId.interrupt)
      .then((e) => setCheckbox(true))
      .catch((e) => {
        setCheckbox(false);
      });
  }, []);
  return (
    <>
      {checkbox && (
        <CheckBoxDefault
          componentId={componentId}
          symbolId={symbolId.interrupt}
          hidden={false}
        ></CheckBoxDefault>
      )}
    </>
  );
};

export default InterruptComponent;
