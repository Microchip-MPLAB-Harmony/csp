import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  booleanSymbolApi,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
type Props = {
  symbolId: string;
};
const InputScanComponent = ({ symbolId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const inputSCan = useBooleanSymbol({ componentId, symbolId });
  const [checkbox, setCheckbox] = useState(false);
  useEffect(() => {
    booleanSymbolApi
      .getValue(componentId, symbolId)
      .then((e) => setCheckbox(true))
      .catch((e) => {
        setCheckbox(false);
      });
  }, [symbolId]);
  return (
    <div style={{ textAlign: "center" }}>
      {checkbox &&
        (inputSCan.value ? (
          <i
            className="pi pi-check"
            style={{ color: "green", fontSize: "1.25rem" }}
          ></i>
        ) : (
          <i
            className="pi pi-ban"
            style={{ color :"orange", fontSize: "1.25rem" }}
          ></i>
        ))}
    </div>
  );
};

export default InputScanComponent;
