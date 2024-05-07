import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  CheckBoxDefault,
  useSymbol,
  symbolUtilApi,
  booleanSymbolApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const SignedModeComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [checkbox, setCheckbox] = useState(false);
  useEffect(() => {
    booleanSymbolApi
      .getValue(componentId, symbolId.signedMode)
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
          symbolId={symbolId.signedMode}
          hidden={false}
        ></CheckBoxDefault>
      )}
    </>
  );
};

export default SignedModeComponent;
