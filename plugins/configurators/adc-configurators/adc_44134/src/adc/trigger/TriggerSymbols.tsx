import positions from "../../styles/positions.module.css";
import React from "react";
import {
  KeyValueSetRadio,
  createClassResolver,
  DropDown,
  InputNumber,
} from "@mplab_harmony/harmony-plugin-client-lib";
import useTriggerSymbols from "./useTriggerSymbols";
const cx = createClassResolver(positions);
const TriggerSymbols = () => {
  const { triggerMode, triggerPeriod, triggerSelection } = useTriggerSymbols();
  const triggerArray = [1, 2, 3];
  return (
    <div>
      <KeyValueSetRadio
        keyValueSetSymbolHook={triggerMode}
        classPrefix="triggerMode"
        classResolver={cx}
      ></KeyValueSetRadio>
      <DropDown
        keyValueSetSymbolHook={triggerSelection}
        className={cx("triggerSelection")}
        hidden={false}
        disabled={!triggerArray.includes(triggerMode.value)}
      ></DropDown>
      <InputNumber
        integerSymbolHook={triggerPeriod}
        className={cx("triggerPeriod")}
        hidden={!(triggerMode.value === 4)}
        size={10}
      />
      {triggerMode.value === 4 && (
        <label className={cx("triggerPeriodLabel")}>
          {triggerPeriod.label}
        </label>
      )}
    </div>
  );
};

export default React.memo(TriggerSymbols);
