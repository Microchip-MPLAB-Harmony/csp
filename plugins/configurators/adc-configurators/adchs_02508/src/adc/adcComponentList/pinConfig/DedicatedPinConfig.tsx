import React, { useContext } from "react";
import {
  createClassResolver,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";
import usePinConfigSymbols from "./usePinConfigSymbols";
import { RadioButton } from "primereact/radiobutton";

type Props = {
  moduleId: number;
};
const className = ["pinLabel0", "pinLabel1", "pinLabel2", "pinLabel3"];
const cx = createClassResolver(positions);
const DedicatedPinConfig = ({ moduleId }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { pinConfigPositive, negativePinLable, pinConfigNegative } =
    usePinConfigSymbols(moduleId);
  const channelEnable = useBooleanSymbol({
    componentId,
    symbolId: `ADCHS_${moduleId}_ENABLE`,
  });
  return (
    <div>
      <>
        {pinConfigPositive.options.map((option, index) => {
          return (
            <label
              key={cx(className[index])}
              className={cx(className[index])}
              style={{
                fontWeight:
                  pinConfigPositive?.selectedOption === option
                    ? "bold"
                    : "initial",
              }}
            >
              {option}
            </label>
          );
        })}
        {pinConfigPositive.options.length < 3 && (
          <label key={cx("pinLabel2")} className={cx("pinLabel2")}>
            N/C
          </label>
        )}
        {pinConfigPositive.options.length < 4 && (
          <label key={cx("pinLabel3")} className={cx("pinLabel3")}>
            N/C
          </label>
        )}
      </>
      <KeyValueSetRadio
        keyValueSetSymbolHook={pinConfigPositive}
        classPrefix="pin"
        classResolver={cx}
        disabled={!channelEnable.value}
        hidden={false}
      ></KeyValueSetRadio>

      <label
        className={cx("pinLabelVr0")}
        style={{
          fontWeight: !pinConfigNegative.value ? "bold" : "initial",
        }}
      >
        {negativePinLable[0]}
      </label>
      <label
        className={cx("pinLabelVr1")}
        style={{
          fontWeight: pinConfigNegative.value ? "bold" : "initial",
        }}
      >
        {negativePinLable[1]}
      </label>

      <RadioButton
        key={pinConfigNegative.symbolId}
        inputId={pinConfigNegative.symbolId}
        name={pinConfigNegative.symbolId}
        value={pinConfigNegative.value}
        onChange={(e) => pinConfigNegative.writeValue(false)}
        checked={pinConfigNegative.value === false}
        className={cx("pinVr0")}
        disabled={!channelEnable.value}
      />
      <RadioButton
        key={pinConfigNegative.symbolId + 1}
        inputId={pinConfigNegative.symbolId + 1}
        name={pinConfigNegative.symbolId + 1}
        value={pinConfigNegative.value}
        onChange={(e) => pinConfigNegative.writeValue(true)}
        checked={pinConfigNegative.value === true}
        className={cx("pinVr1")}
        disabled={!channelEnable.value}
      />
    </div>
  );
};

export default DedicatedPinConfig;
