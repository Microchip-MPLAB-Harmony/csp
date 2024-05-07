import React, { useContext } from "react";
import {
  createClassResolver,
  PluginConfigContext,
  useBooleanSymbol,
  CheckBox,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";

export type ChannelEnableSymboPropsl = {
  inputScanSymbol: string;
  signModeSymbol: string;
  interruptSymbolo: string;
  channelEnableSymbol: string;
};

const cx = createClassResolver(positions);
const CommonCheckBox = ({
  inputScanSymbol,
  signModeSymbol,
  interruptSymbolo,
  channelEnableSymbol,
}: ChannelEnableSymboPropsl) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const channelEnable = useBooleanSymbol({
    componentId,
    symbolId: channelEnableSymbol,
  });
  const inputScan = useBooleanSymbol({
    componentId,
    symbolId: inputScanSymbol,
  });
  const signMode = useBooleanSymbol({
    componentId,
    symbolId: signModeSymbol,
  });
  const interrupt = useBooleanSymbol({
    componentId,
    symbolId: interruptSymbolo,
  });
  return (
    <div>
      <label className={cx("signedModeLabel")}>Signed Mode</label>
      <label className={cx("inputScanLabel")}>Input Scan</label>
      <label className={cx("interruptLabel")}>Interrupt</label>
      <CheckBox
        booleanSymbolHook={inputScan}
        className={cx("inputScan")}
        disabled={!channelEnable.value}
        hidden={false}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={signMode}
        className={cx("signedMode")}
        disabled={!channelEnable.value}
        hidden={false}
      ></CheckBox>
      <CheckBox
        booleanSymbolHook={interrupt}
        className={cx("interrupt")}
        disabled={!channelEnable.value}
        hidden={false}
      ></CheckBox>
    </div>
  );
};

export default CommonCheckBox;
