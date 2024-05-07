import React from "react";
import {
  createClassResolver,
  ComboRadio,
  DropDown,
  InputNumber,
  CheckBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../styles/positions.module.css";
import styles from "./generalConfiguration.module.css";
import useGenerealConfigurationSymbols from "./useGeneralConfigurationSymbols";

const cx = createClassResolver(positions, styles);
const GeneralConfiguration = () => {
  const {
    resultSign,
    prescaler,
    fifoChunkSize,
    clockFrequency,
    clockFrequencyWarning,
    sleepMode,
    fastWakeUp,
    enableFifo,
    fifoEnableLevel,
  } = useGenerealConfigurationSymbols();
  return (
    <div>
      <CheckBox
        booleanSymbolHook={sleepMode}
        className={cx("sleepMode")}
      ></CheckBox>
      {sleepMode.value && (
        <>
          <label className={cx("fastWakeUpLabel")}>{fastWakeUp.label}</label>
          <label className={cx("fastWakeUpLabel1")}>ON</label>
          <label className={cx("fastWakeUpLabel0")}>OFF</label>
          <ComboRadio
            comboSymbolHook={fastWakeUp}
            classPrefix="fastWakeUp"
            classResolver={cx}
            hidden={false}
          ></ComboRadio>
        </>
      )}

      <CheckBox
        booleanSymbolHook={enableFifo}
        className={cx("enableFifo")}
      ></CheckBox>

      {enableFifo.value && (
        <>
          <label className={cx("fifoEnableLevelLabel")}>
            FIFO {fifoEnableLevel.label}
          </label>
          <DropDown
            keyValueSetSymbolHook={fifoEnableLevel}
            className={cx("fifoEnableLevel")}
            hidden={false}
            size={10}
          ></DropDown>
          <label className={cx("fifoChunkSizeLabel")}>
            FIFO {fifoChunkSize.label}
          </label>
          <InputNumber
            integerSymbolHook={fifoChunkSize}
            className={cx("fifoChunkSize")}
            hidden={false}
            size={10}
          />
        </>
      )}

      <label className={cx("prescalerLabel")}>{prescaler.value}</label>

      <InputNumber
        integerSymbolHook={prescaler}
        className={cx("prescaler")}
        size={10}
      />

      <DropDown
        keyValueSetSymbolHook={resultSign}
        className={cx("resultSign")}
        hidden={false}
        size={50}
      ></DropDown>

      <label
        className={
          clockFrequencyWarning.visible
            ? cx("clockFrequencyLabel")
            : cx("clockFrequencyLabel", "clockFrequencyTextBlack")
        }
      >
        {clockFrequency.value} Hz
      </label>
      {clockFrequencyWarning.visible && (
        <label className={cx("frequencyComment")}>
          {clockFrequencyWarning.label}
        </label>
      )}
    </div>
  );
};

export default React.memo(GeneralConfiguration);
