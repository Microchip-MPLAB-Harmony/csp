import { useContext } from "react";
import { useKeyValueSetSymbol, PluginConfigContext, useBooleanSymbol } from "@mplab_harmony/harmony-plugin-client-lib";
const useReferenceVoltageSymbols = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);

  const voltageReference = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADCCON3__VREFSEL",
    
  });
  const endOfScan=useBooleanSymbol({
    componentId,
    symbolId: 'ADCCON2__EOSIEN',
  });
  return {
    voltageReference,
    endOfScan
  };
};

export default useReferenceVoltageSymbols;
