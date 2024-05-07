import React from "react";
import { createClassResolver, KeyValueSetRadio, InputNumber, InputLong } from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../styles/positions.module.css";
import styles from "./clockSource.module.css";
import useClockSourceSymbols from "./useClockSourceSymbols";
const className = [
  "clkSrcLable0",
  "clkSrcLable1",
  "clkSrcLable2",
  "clkSrcLable3",
];
const cx = createClassResolver(positions, styles);
const ClockSource = () => {
  const { clockSource, controlClockDivider, labelTQ, frequency } =
    useClockSourceSymbols();
  return (
    <div>
      <>
        {clockSource.options.map((option, index) => {
          return (
            <label
              className={cx(className[index])}
              style={{
                fontWeight:
                  clockSource?.selectedOption === option ? "bold" : "initial",
              }}
            >
              {option}
            </label>
          );
        })}
      </>

      <KeyValueSetRadio
        keyValueSetSymbolHook={clockSource}
        classPrefix="clockSource"
        classResolver={cx}
      ></KeyValueSetRadio>
      <InputLong
        longSymbolHook={controlClockDivider}
        className={cx("controlClockDivider")}
      ></InputLong>
      <label className={cx("clkFreq")}>{frequency.value} Hz</label>
      <label className={cx("labelTCLK")}>
        TCLK ={" "}
        {frequency.value === 0
          ? 0
          : ((1.0 / frequency.value) * 1000000000).toFixed(3)}{" "}
        ns
      </label>
      <label className={cx("labelTQ")}>
        TQ = {labelTQ.value.toFixed(3)} ns
      </label>
    </div>
  );
};

export default React.memo(ClockSource);
