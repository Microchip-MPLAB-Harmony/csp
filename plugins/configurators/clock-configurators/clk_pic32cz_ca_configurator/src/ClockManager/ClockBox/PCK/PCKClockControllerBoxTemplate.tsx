import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import {
  CheckBox,
  DropDown,
  InputNumber,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import { GetClockDisplayFreqValue } from "clock-common/lib/Tools/Tools";
import React, { useContext } from "react";

const PCKClockControllerBoxTemplate = (props: {
  tabTitle: string;
  componentId: string;
  cx: (...classNames: string[]) => string;
  clkSettingsSymbolArray: string[];
  clkController: ControlInterface[];
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const pllEnable = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_ENABLE",
  });
  const plloscFdpllChannelSource = useKeyValueSetSymbol({
    componentId,
    symbolId: "GCLK_ID_" + (parseInt(props.tabTitle) + 1) + "_GENSEL",
  });
  const plloscFdpllChannelEnable = useBooleanSymbol({
    componentId,
    symbolId: "GCLK_ID_" + (parseInt(props.tabTitle) + 1) + "_CHEN",
  });
  const pllRefClock = useKeyValueSetSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_REF_CLOCK",
  });
  const pllrefdiv = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLREFDIV_REFDIV",
  });
  const plldigitalFilterBWSel = useKeyValueSetSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_BWSEL",
  });
  const pllfbdiv = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLFBDIV_FBDIV",
  });
  const pllpostdiv0 = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_POSTDIV0",
  });
  const pllpostdiv1 = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_POSTDIV1",
  });
  const pllpostdiv2 = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_POSTDIV2",
  });
  const pllpostdiv3 = useIntegerSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_POSTDIV3",
  });
  const pllouten0 = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_OUTEN0",
  });
  const pllouten1 = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_OUTEN1",
  });
  const pllouten2 = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_OUTEN2",
  });
  const pllouten3 = useBooleanSymbol({
    componentId,
    symbolId: "CONFIG_CLOCK_PLL" + props.tabTitle + "_PLLPOSTDIVA_OUTEN3",
  });
  const pllFreq0 = useIntegerSymbol({
    componentId,
    symbolId: "PLL" + props.tabTitle + "_CLOCK_FREQ0",
  });
  const pllFreq1 = useIntegerSymbol({
    componentId,
    symbolId: "PLL" + props.tabTitle + "_CLOCK_FREQ1",
  });
  const pllFreq2 = useIntegerSymbol({
    componentId,
    symbolId: "PLL" + props.tabTitle + "_CLOCK_FREQ2",
  });
  const pllFreq3 = useIntegerSymbol({
    componentId,
    symbolId: "PLL" + props.tabTitle + "_CLOCK_FREQ3",
  });
  let freq: any = 0;
  const freq1 = useIntegerSymbol({
    componentId,
    symbolId: "GCLK_" + plloscFdpllChannelSource.value + "_FREQ",
  });
  const freq2 = useIntegerSymbol({ componentId, symbolId: "XOSC_FREQ" });
  const freq3 = useIntegerSymbol({ componentId, symbolId: "DFLL_CLOCK_FREQ" });
  if (pllRefClock.value === 0) {
    if (plloscFdpllChannelEnable.value) {
      freq = freq1.value;
    }
  }
  if (pllRefClock.value === 1) {
    freq = freq2.value;
  }
  if (pllRefClock.value === 2) {
    freq = freq3.value;
  }
  const fpfdFreq = freq / pllrefdiv.value;
  const fvcoFreq = (freq * pllfbdiv.value) / pllrefdiv.value;
  return (
    <div>
      <CheckBox
        booleanSymbolHook={pllEnable}
        className={props.cx("pllEnable")}
      />
      <DropDown
        keyValueSetSymbolHook={plloscFdpllChannelSource}
        className={props.cx("plloscFdpllChannelSource")}
      />
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(freq) + ""}
        className={props.cx("fckrFreqLabel")}
      />
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(fpfdFreq) + ""}
        redColorStatus={
          fpfdFreq < 4000000 || fpfdFreq > 60000000 ? true : false
        }
        className={props.cx("fpfdFreqLabel")}
      />
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(fvcoFreq) + ""}
        redColorStatus={
          fvcoFreq < 800000000 || fvcoFreq > 16000000000 ? true : false
        }
        className={props.cx("fvcoFreqLabel")}
      />

      <CheckBox
        booleanSymbolHook={plloscFdpllChannelEnable}
        className={props.cx("plloscFdpllChannelEnable")}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={pllRefClock}
        classPrefix="pllRefClock"
        classResolver={props.cx}
      />
      <InputNumber
        integerSymbolHook={pllrefdiv}
        className={props.cx("pllrefdiv")}
      />
      <DropDown
        keyValueSetSymbolHook={plldigitalFilterBWSel}
        className={props.cx("plldigitalFilterBWSel")}
      />
      <InputNumber
        integerSymbolHook={pllfbdiv}
        className={props.cx("pllfbdiv")}
      />
      <InputNumber
        integerSymbolHook={pllpostdiv0}
        className={props.cx("pllpostdiv0")}
      />
      <InputNumber
        integerSymbolHook={pllpostdiv1}
        className={props.cx("pllpostdiv1")}
      />
      <InputNumber
        integerSymbolHook={pllpostdiv2}
        className={props.cx("pllpostdiv2")}
      />
      <InputNumber
        integerSymbolHook={pllpostdiv3}
        className={props.cx("pllpostdiv3")}
      />
      <CheckBox
        booleanSymbolHook={pllouten0}
        className={props.cx("pllouten0")}
      />
      <CheckBox
        booleanSymbolHook={pllouten1}
        className={props.cx("pllouten1")}
      />
      <CheckBox
        booleanSymbolHook={pllouten2}
        className={props.cx("pllouten2")}
      />
      <CheckBox
        booleanSymbolHook={pllouten3}
        className={props.cx("pllouten3")}
      />

      {pllouten0.value && (
        <PlainLabel
          disPlayText={GetClockDisplayFreqValue(pllFreq0.value) + ""}
          redColorStatus={
            pllFreq0.value <= 12700000 || pllFreq0.value >= 16000000000
              ? true
              : false
          }
          className={props.cx("pllFreq0")}
        />
      )}
      {pllouten1.value && (
        <PlainLabel
          disPlayText={GetClockDisplayFreqValue(pllFreq1.value) + ""}
          redColorStatus={
            pllFreq1.value <= 12700000 || pllFreq1.value >= 16000000000
              ? true
              : false
          }
          className={props.cx("pllFreq1")}
        />
      )}
      {pllouten2.value && (
        <PlainLabel
          disPlayText={GetClockDisplayFreqValue(pllFreq2.value) + ""}
          redColorStatus={
            pllFreq2.value <= 12700000 || pllFreq2.value >= 16000000000
              ? true
              : false
          }
          className={props.cx("pllFreq2")}
        />
      )}
      {pllouten3.value && (
        <PlainLabel
          disPlayText={GetClockDisplayFreqValue(pllFreq3.value) + ""}
          redColorStatus={
            pllFreq3.value <= 12700000 || pllFreq3.value >= 16000000000
              ? true
              : false
          }
          className={props.cx("pllFreq3")}
        />
      )}
      <PlainLabel
        disPlayText={pllfbdiv.value + ""}
        booldStatus={true}
        className={props.cx("pllFBDivLabel")}
      />
      <PlainLabel
        disPlayText={pllrefdiv.value + ""}
        booldStatus={true}
        className={props.cx("pllrefdivLabel")}
      />
      <PlainLabel
        disPlayText={pllpostdiv0.value + ""}
        booldStatus={true}
        className={props.cx("pllPostDivLabel0")}
      />
      <PlainLabel
        disPlayText={pllpostdiv1.value + ""}
        booldStatus={true}
        className={props.cx("pllPostDivLabel1")}
      />
      <PlainLabel
        disPlayText={pllpostdiv2.value + ""}
        booldStatus={true}
        className={props.cx("pllPostDivLabel2")}
      />
      <PlainLabel
        disPlayText={pllpostdiv3.value + ""}
        booldStatus={true}
        className={props.cx("pllPostDivLabel3")}
      />

      <SettingsDialog
        tooltip={'PCK clock ' + props.tabTitle + ' Settings Configuration'}
        componentId={props.componentId}
        className={props.cx('fdpllSetting')}
        symbolArray={props.clkSettingsSymbolArray}
        dialogWidth='45rem'
        dialogHeight='62rem'
      />
      <ResetSymbolsIcon
        tooltip={'PCK clock ' + props.tabTitle + ' symbols to default value'}
        className={props.cx('fdpllReset')}
        componentId={props.componentId}
        resetSymbolsArray={props.clkSettingsSymbolArray}
      />
    </div>
  );
};
export default React.memo(PCKClockControllerBoxTemplate);
