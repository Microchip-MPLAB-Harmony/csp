import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  DropDownDefault,
  keyValueSetSymbolApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";

const TriggerSourceComponent = (symbolId: SymbolIds) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [checkbox, setCheckbox] = useState(false);
  useEffect(() => {
    keyValueSetSymbolApi
      .getValue(componentId, symbolId?.triggerSource)
      .then((e) => setCheckbox(true))
      .catch((e) => {
        setCheckbox(false);
      });
  }, []);
  return (
    <>
      {checkbox && (
        <DropDownDefault
          componentId={componentId}
          symbolId={symbolId.triggerSource}
          hidden={false}
        ></DropDownDefault>
      )}
    </>
  );
};

export default TriggerSourceComponent;
