import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  CheckBoxDefault,
  booleanSymbolApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const DifferentialComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [checkbox, setCheckbox] = useState(false);
  useEffect(() => {
    booleanSymbolApi
      .getValue(componentId, symbolId.diffMode)
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
          symbolId={symbolId.diffMode}
          hidden={false}
        ></CheckBoxDefault>
      )}
    </>
  );
};

export default DifferentialComponent;
