import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  CheckBoxDefault,
  booleanSymbolApi,
  useKeyValueSetSymbol,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "../../channelConfig/ChannelConfigurationTable";
type Props = {
  symbolId: string;
};
const DifferentialComponent = ({ symbolId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const diffMode = useBooleanSymbol({ componentId, symbolId });
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
    <div style={{textAlign:'center'}}>
      {checkbox &&
        (diffMode.value ? (
          <i className="pi pi-check" style={{ color: "green", fontSize: '1.25rem' }}></i>
        ) : (
          <i className="pi pi-ban" style={{ color: "orange", fontSize: '1.25rem' }}></i>
        ))}
    </div>
  );
};

export default DifferentialComponent;
