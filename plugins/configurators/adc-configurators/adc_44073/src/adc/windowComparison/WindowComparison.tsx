import React from "react";
import positions from "../../styles/positions.module.css";
import {
  KeyValueSetRadio,
  createClassResolver,
  CheckBox,
  ComboBox,
  InputNumber,
  DropDown,
} from "@mplab_harmony/harmony-plugin-client-lib";
import useWindowComparisonSymbols from "./useWindowComparisonSymbols";

const cx = createClassResolver(positions);

const WindowComparison = () => {
  const {
    comparisonMode,
    comparisonType,
    windowComparisonBoolean,
    interrupt,
    channelCombo,
    vlo,
    vhi,
  } = useWindowComparisonSymbols();
  return (
    <div>
      <KeyValueSetRadio
        keyValueSetSymbolHook={comparisonType}
        classPrefix="comparisonType"
        classResolver={cx}
        hidden={false}
        disabled={!windowComparisonBoolean.value}
      ></KeyValueSetRadio>
      <CheckBox
        booleanSymbolHook={windowComparisonBoolean}
        className={cx("windowComparisonBoolean")}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={interrupt}
        className={cx("interrupt")}
        hidden={false}
        disabled={!windowComparisonBoolean.value}
      ></CheckBox>
      <ComboBox
        comboSymbolHook={channelCombo}
        className={cx("channelCombo")}
        hidden={false}
        disabled={!windowComparisonBoolean.value}
      ></ComboBox>
      <InputNumber
        integerSymbolHook={vlo}
        className={cx("vlo")}
        hidden={false}
        disabled={!windowComparisonBoolean.value}
        size={10}
      />
      <InputNumber
        integerSymbolHook={vhi}
        className={cx("vhi")}
        hidden={false}
        disabled={!windowComparisonBoolean.value}
        size={30}
      />
      <DropDown
        keyValueSetSymbolHook={comparisonMode}
        className={cx("comparisonMode")}
        hidden={false}
        disabled={!windowComparisonBoolean.value}
        size={10}
      ></DropDown>
    </div>
  );
};

export default React.memo(WindowComparison);
