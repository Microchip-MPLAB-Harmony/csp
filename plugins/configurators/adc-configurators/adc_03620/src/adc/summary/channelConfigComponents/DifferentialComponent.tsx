import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  comboSymbolApi,
  useComboSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
type Props = {
  symbolId: string;
};
const DifferentialComponent = ({ symbolId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const diffMode = useComboSymbol({ componentId, symbolId });
  const [checkbox, setCheckbox] = useState(false);
  useEffect(() => {
    comboSymbolApi
      .getValue(componentId, symbolId)
      .then((e) => setCheckbox(true))
      .catch((e) => {
        setCheckbox(false);
      });
  }, [symbolId]);
  return (
    <div style={{ textAlign: "center" }}>
      <label>{checkbox && diffMode.value}</label>
    </div>
  );
};

export default DifferentialComponent;
