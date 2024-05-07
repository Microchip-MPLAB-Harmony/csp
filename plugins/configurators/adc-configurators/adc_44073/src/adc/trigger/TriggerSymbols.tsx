import positions from "../../styles/positions.module.css";
import React from "react";
import {
  KeyValueSetRadio,
  createClassResolver,
  DropDown,
  InputNumber,
} from "@mplab_harmony/harmony-plugin-client-lib";
import useTriggerSymbols from "./useTriggerSymbols";
import useChannelCount from "../channelConfiguration/useChannelCount";
const cx = createClassResolver(positions);
const TriggerSymbols = () => {
  const { triggerMode, triggerPeriod, triggerSelection } = useTriggerSymbols();
  const { productFamily } = useChannelCount();
  const SAMHComponent = () => (
    <>
      <label className={cx("label2")}>Free Run</label>
      <label className={cx("label3")}>Software Trigger</label>
      <label className={cx("label4")}>Hardware Trigger</label>
      <KeyValueSetRadio
        keyValueSetSymbolHook={triggerMode}
        classPrefix="triggerModeSAMH"
        classResolver={cx}
      ></KeyValueSetRadio>
      <DropDown
        keyValueSetSymbolHook={triggerSelection}
        className={cx("triggerSelection")}
        hidden={false}
        disabled={![2].includes(triggerMode.value)}
      ></DropDown>
    </>
  );

  const NormalComponenct = () => (
    <>
    <label className={cx("label0")}>Software Trigger</label>
      <label className={cx("label1")}>External Trigger Rising Edge</label>
      <label className={cx("label2")}>External Trigger Falling Edge</label>
      <label className={cx("label3")}>External Trigger Any Edge</label>
      <label className={cx("label4")}>Internal Periodic Trigger</label>
      <label className={cx("label5")}>Continuous</label>
      <KeyValueSetRadio
        keyValueSetSymbolHook={triggerMode}
        classPrefix="triggerMode"
        classResolver={cx}
      ></KeyValueSetRadio>
      <DropDown
        keyValueSetSymbolHook={triggerSelection}
        className={cx("triggerSelection")}
        hidden={false}
        disabled={![1, 2, 3].includes(triggerMode.value)}
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
    </>
  );
  return (
    <div>
      {productFamily === "SAMRH" ? <SAMHComponent />:<NormalComponenct />}
    </div>
  );
};

export default React.memo(TriggerSymbols);
