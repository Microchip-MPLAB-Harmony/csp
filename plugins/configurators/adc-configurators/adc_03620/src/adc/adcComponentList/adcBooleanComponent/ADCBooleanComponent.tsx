import React, { useContext } from "react";
import {
  createClassResolver,
  PluginConfigContext,
  useBooleanSymbol,
  CheckBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";
type Props = {
  moduleId: number;
};

const cx = createClassResolver(positions);
const ADCBooleanComponent = ({ moduleId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const channelInterrupt = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_INTENSET_CHNERRC`,
  });
  const eventOutput = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_EVCTRL_RESRDYEO`,
  });
  const eventInput = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_EVCTRL_STARTEI`,
  });
  const endOfScanInterrupt = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_INTENSET_EOSRDY`,
  });
  const adcResult = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_PFFCTRL_PFFCR`,
  });

  return (
    <div>
      <CheckBox
        booleanSymbolHook={channelInterrupt}
        className={cx("channelInterrupt")}
        hidden={false}
        disabled={false}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={eventOutput}
        className={cx("eventOutput")}
        hidden={false}
        disabled={false}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={eventInput}
        className={cx("eventInput")}
        hidden={false}
        disabled={false}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={endOfScanInterrupt}
        className={cx("endOfScanInterrupt")}
        hidden={false}
        disabled={false}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={adcResult}
        className={cx("adcResult")}
        hidden={false}
        disabled={false}
      ></CheckBox>
    </div>
  );
};

export default ADCBooleanComponent;
