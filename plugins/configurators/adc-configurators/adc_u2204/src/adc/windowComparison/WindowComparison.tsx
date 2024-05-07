import React from "react";
import {
  createClassResolver,
  CheckBox,
  InputNumber,
  DropDown,
} from "@mplab_harmony/harmony-plugin-client-lib";

import positions from "../../styles/positions.module.css";
import useWindowComparisonSymbols from "./useWindowComparisonSymbols";

const cx = createClassResolver(positions);

const WindowComparison = () => {
  const { comparisonMode, win, winmonInterrupt, vlo, vhi } =
    useWindowComparisonSymbols();
  return (
    <div>
      <InputNumber
        className={cx("vhi")}
        integerSymbolHook={vhi}
        hidden={false}
      ></InputNumber>
      <InputNumber
        className={cx("vlo")}
        integerSymbolHook={vlo}
        hidden={false}
      ></InputNumber>
      <CheckBox
        className={cx("winmonInterrupt")}
        booleanSymbolHook={winmonInterrupt}
        hidden={false}
      ></CheckBox>
      <CheckBox
        className={cx("win")}
        booleanSymbolHook={win}
        hidden={false}
      ></CheckBox>

      <DropDown
        className={cx("comparisonMode")}
        keyValueSetSymbolHook={comparisonMode}
      ></DropDown>
    </div>
  );
};

export default React.memo(WindowComparison);
