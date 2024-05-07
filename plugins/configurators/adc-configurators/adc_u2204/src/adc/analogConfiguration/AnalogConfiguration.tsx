import React from "react";
import { createClassResolver, DropDown, InputNumber } from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../styles/positions.module.css";
import useAnalogConfigurationSymbols from "./useAnalogConfigurationSymbols";

const cx = createClassResolver(positions);
const AnalogConfiguration = () => {
  const {
    sampleLenght,
    reference,
    gain,
    conversionTime,
    channelConfigNegative,
    channelConfigPositve,
    resultResolution,
  } = useAnalogConfigurationSymbols();
  return (
    <div>
      <DropDown
        className={cx("resultResolution")}
        keyValueSetSymbolHook={resultResolution}
      ></DropDown>

      <DropDown
        className={cx("channelConfigPositve")}
        keyValueSetSymbolHook={channelConfigPositve}
      ></DropDown>

      <DropDown
        className={cx("channelConfigNegative")}
        keyValueSetSymbolHook={channelConfigNegative}
      ></DropDown>

      <DropDown className={cx("gain")} keyValueSetSymbolHook={gain}></DropDown>

      <InputNumber
        className={cx("clockCycle")}
        integerSymbolHook={sampleLenght}
      ></InputNumber>

      <DropDown
        className={cx("reference")}
        keyValueSetSymbolHook={reference}
      ></DropDown>
      <span
        className={cx("conversion")}
        style={{ overflow: "hidden", textOverflow: "ellipsis" }}
      >
        {conversionTime?.label
          ?.replace("**** Conversion Time is ", "")
          ?.replace(" ****", "")}
      </span>
    </div>
  );
};

export default React.memo(AnalogConfiguration);
