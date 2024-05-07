import React, { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  DropDownDefault,
  keyValueSetSymbolApi,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "../../channelConfig/ChannelConfigurationTable";
type Props = {
  symbolId: string;
};
const TriggerSourceComponent = ({ symbolId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [checkbox, setCheckbox] = useState(false);
  const triggerSource = useKeyValueSetSymbol({componentId,symbolId})
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
  return <div style={{textAlign:'center'}}>{checkbox &&  triggerSource.selectedOption}</div>;
};

export default TriggerSourceComponent;
