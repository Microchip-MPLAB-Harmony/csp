import React from "react";
import {
  createClassResolver,
  ComboRadio,
  DropDown,
  CheckBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../styles/positions.module.css";
import useGenerealConfigurationSymbols from "./useGeneralConfigurationSymbols";
type Props = {
  enableSlaveCheckBox: boolean;
};
const cx = createClassResolver(positions);
const GeneralConfiguration = ({ enableSlaveCheckBox }: Props) => {
  const {
    conversionTrigger,
    resultEvent,
    runStandby,
    leftAlignResult,
    resultInterrupt,
    preScaler,
    flushEvent,
    startEvent,
    onDemandctrl,
  } = useGenerealConfigurationSymbols();
  let matches = preScaler.selectedOptionPair?.key.match(/(\d+)/);
  return (
    <div>
      <DropDown
        className={cx("startEvent")}
        keyValueSetSymbolHook={startEvent}
        hidden={false}
        disabled={
          !(conversionTrigger.value === "HW Event Trigger") ||
          enableSlaveCheckBox
        }
      ></DropDown>

      <DropDown
        className={cx("flushEvent")}
        keyValueSetSymbolHook={flushEvent}
        hidden={false}
        disabled={
          !(conversionTrigger.value === "HW Event Trigger") ||
          enableSlaveCheckBox
        }
      ></DropDown>

      <ComboRadio
        hidden={false}
        comboSymbolHook={conversionTrigger}
        classPrefix={"coversionTrigger"}
        classResolver={cx}
        disabled={enableSlaveCheckBox}
      ></ComboRadio>
      <CheckBox
        className={cx("runStandby")}
        booleanSymbolHook={runStandby}
      ></CheckBox>
      <CheckBox
        className={cx("demandControl")}
        booleanSymbolHook={onDemandctrl}
      ></CheckBox>
      <CheckBox
        className={cx("leftAlignResult")}
        booleanSymbolHook={leftAlignResult}
      ></CheckBox>

      <DropDown
        className={cx("prescaler")}
        hidden={false}
        keyValueSetSymbolHook={preScaler}
        disabled={enableSlaveCheckBox}
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
