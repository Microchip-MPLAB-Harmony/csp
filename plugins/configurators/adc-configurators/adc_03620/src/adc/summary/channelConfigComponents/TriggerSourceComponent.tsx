import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  keyValueSetSymbolApi,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
type Props = {
  symbolId: string;
};
const TriggerSourceComponent = ({ symbolId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [checkbox, setCheckbox] = useState(false);
  const triggerSource = useKeyValueSetSymbol({ componentId, symbolId });
  useEffect(() => {
    keyValueSetSymbolApi
      .getValue(componentId, symbolId)
      .then(() => {
        setCheckbox(true);
      })
      .catch((e) => {
        setCheckbox(false);
      });
  }, [symbolId]);
  return (
    <div style={{textAlign:'center'}}>
      <label>
        {checkbox && triggerSource.selectedOption}
      </label>
    </div>
  );
};

export default TriggerSourceComponent;
