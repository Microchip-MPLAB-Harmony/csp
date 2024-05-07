import { useContext } from "react";
import {
  PluginConfigContext,
  useBooleanSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import useADCModuleConfig from "../useADCModuleConfig";

const usePinConfigSymbols = (code: number) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const {adcModules} = useADCModuleConfig()
  const pinConfigPositive = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADCTRGMODE__SH${code}ALT`,
  });

  const pinConfigNegative = useBooleanSymbol({
    componentId,
    symbolId: `ADCIMCON1__DIFF${code}`,
  });

  const negativePinLable = ['VREFL',`AN${(code+adcModules.length-1)}`]

  return {
    pinConfigPositive,
    pinConfigNegative,
    negativePinLable,

  };
};

export default usePinConfigSymbols;
