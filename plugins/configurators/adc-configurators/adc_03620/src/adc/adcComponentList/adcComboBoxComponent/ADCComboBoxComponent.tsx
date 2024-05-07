import React, { useContext } from "react";
import {
  createClassResolver,
  PluginConfigContext,
  DropDown,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";
type Props = {
  moduleId: number;
};

const cx = createClassResolver(positions);
const ADCComboBoxComponent = ({ moduleId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const resolution = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_CORCTRL_SELRES`,
  });
  const triggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_CORCTRL_STRGSRC`,
  });
  const globalTriggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_PFFCTRL_PFFRDYDMA`,
  });
  
  return (
    <div>
      <DropDown
        keyValueSetSymbolHook={resolution}
        className={cx("resolution")}
        hidden={false}
      ></DropDown>
      <DropDown
        keyValueSetSymbolHook={triggerSource}
        className={cx("triggerSource")}
        hidden={false}
      ></DropDown>
      <DropDown
        keyValueSetSymbolHook={globalTriggerSource}
        className={cx("globalTriggerSource")}
        hidden={false}
      ></DropDown>
    </div>
  );
};

export default ADCComboBoxComponent;
