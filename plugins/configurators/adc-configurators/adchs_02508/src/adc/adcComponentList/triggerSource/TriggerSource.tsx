import React, { useContext } from "react";
import {
  createClassResolver,
  useKeyValueSetSymbol,
  PluginConfigContext,
  DropDown,
  useBooleanSymbol,
  CheckBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";
import useADCModuleConfig from "../useADCModuleConfig";
import useSymbolControl from "../../channelConfig/useSymbolControl";

export type TriggerSymboProps = {
  moduleId: number;
};
const getTriggerSymbolId = (analogInput: number, NUM_SIGNALS_COUNT: number) => {
  let symbol: number | string = analogInput;
  if (analogInput < 4) {
    symbol = `ADCTRG1__TRGSRC${analogInput}`;
  }
  if (analogInput >= 4 && analogInput < 8) {
    symbol = `ADCTRG2__TRGSRC${analogInput}`;
  }
  if (analogInput >= 8 && analogInput < 12) {
    symbol = `ADCTRG3__TRGSRC${analogInput}`;
  }
  if (analogInput >= 12 && analogInput < 16) {
    symbol = `ADCTRG4__TRGSRC${analogInput}`;
  }
  if (analogInput >= 16 && analogInput < 20) {
    symbol = `ADCTRG5__TRGSRC${analogInput}`;
  }
  if (analogInput >= 20 && analogInput < 24) {
    symbol = `ADCTRG6__TRGSRC${analogInput}`;
  }
  if (analogInput >= 24 && analogInput < NUM_SIGNALS_COUNT) {
    symbol = `ADCTRG7__TRGSRC${analogInput}`;
  }
  return symbol;
};
const cx = createClassResolver(positions);
const TriggerSource = ({ moduleId }: TriggerSymboProps) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { getSharedSymbolIds, sharedModuleId } = useADCModuleConfig();
  const { NUM_SIGNALS_COUNT } = useSymbolControl();
  const dedicated = getTriggerSymbolId(moduleId, NUM_SIGNALS_COUNT);
  const shared = getSharedSymbolIds(sharedModuleId);
  const sharedTrigger = useKeyValueSetSymbol({
    componentId,
    symbolId: shared.triggerSource,
  });
  const dedicatedTrigger = useKeyValueSetSymbol({
    componentId,
    symbolId: dedicated as string,
  });
  const scanInterrupt = useBooleanSymbol({
    componentId,
    symbolId: "ADCCON2__EOSIEN",
  });
  const channelEnable = useBooleanSymbol({
    componentId,
    symbolId: `ADCHS_${moduleId}_ENABLE`,
  });
  return (
    <div>
      <DropDown
        keyValueSetSymbolHook={sharedTrigger}
        className={cx("sharedTrigger")}
        disabled={!(moduleId === sharedModuleId) || !channelEnable.value}
        hidden={false}
      ></DropDown>
      {moduleId !== sharedModuleId && (
        <DropDown
          keyValueSetSymbolHook={dedicatedTrigger}
          className={cx("dedicatedTrigger")}
          hidden={false}
          disabled={!channelEnable.value}
        ></DropDown>
      )}
      <label className={cx("scanInterruptLabel")}>End Of Scan Interrupt</label>
      <CheckBox
        className={cx("scanInterrupt")}
        booleanSymbolHook={scanInterrupt}
      ></CheckBox>
    </div>
  );
};

export default TriggerSource;
