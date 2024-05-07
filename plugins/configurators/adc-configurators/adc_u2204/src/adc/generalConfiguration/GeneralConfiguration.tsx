import React from "react";
import {
  createClassResolver,
  ComboRadio,
  DropDown,
  InputNumber,
  CheckBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../styles/positions.module.css";
import useGenerealConfigurationSymbols from "./useGeneralConfigurationSymbols";

const cx = createClassResolver(positions);
const GeneralConfiguration = () => {
  const {
    conversionTrigger,
    scanToStart,
    inputSCan,
    resultEvent,
    runStandby,
    leftAlignResult,
    resultInterrupt,
    preScaler,
    flushEvent,
    startEvent,
  } = useGenerealConfigurationSymbols();
  let matches = preScaler.selectedOptionPair?.key.match(/(\d+)/);
  return (
    <div>
      <CheckBox
        hidden={false}
        className={cx("startEvent")}
        booleanSymbolHook={startEvent}
        disabled={!(conversionTrigger.value === "HW Event Trigger")}
      ></CheckBox>
      <CheckBox
        hidden={false}
        className={cx("flushEvent")}
        booleanSymbolHook={flushEvent}
        disabled={!(conversionTrigger.value === "HW Event Trigger")}
      ></CheckBox>
      <InputNumber
        className={cx("inputScan")}
        integerSymbolHook={inputSCan}
      ></InputNumber>

      <InputNumber
        className={cx("scanStart")}
        integerSymbolHook={scanToStart}
      ></InputNumber>
      <ComboRadio
        comboSymbolHook={conversionTrigger}
        classPrefix={"conversionTriggerRadio"}
        classResolver={cx}
      ></ComboRadio>
      <CheckBox
        className={cx("runStandby")}
        booleanSymbolHook={runStandby}
      ></CheckBox>
      <CheckBox
        className={cx("leftAlignResult")}
        booleanSymbolHook={leftAlignResult}
      ></CheckBox>

      <DropDown
        className={cx("prescaler")}
        keyValueSetSymbolHook={preScaler}
      ></DropDown>
      <CheckBox
        className={cx("resultInterrupt")}
        booleanSymbolHook={resultInterrupt}
      ></CheckBox>
      <CheckBox
        className={cx("resultEvent")}
        booleanSymbolHook={resultEvent}
      ></CheckBox>
      <span className={cx("preScalarValue")}>{matches && matches[0]}</span>
    </div>
  );
};

export default React.memo(GeneralConfiguration);
