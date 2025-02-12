import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import {
  CheckBoxDefault,
  InputNumberDefault,
  KeyValueSetRadio,
  PluginConfigContext,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";
import React, { useContext } from "react";

const GCKLClockControllerBoxTemplate = (props: {
  tabTitle: string;
  componentId: string;
  cx: (...classNames: string[]) => string;
  gclkSettingsSymbolArray: string[];
  gclkController: ControlInterface[];
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const gclkSel = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_PCK" + props.tabTitle + "_CSS",
  });
  const gclkDiv = useIntegerSymbol({
    componentId,
    symbolId: "CLK_PCK" + props.tabTitle + "_PRES",
  });
  return (
    <div>
      <PlainLabel
        disPlayText={`/ (${gclkDiv.value} + 1)`}
        className={props.cx("programmableClkPressLabel")}
      />
      <FrequencyLabelComponent
        componentId={componentId}
        symbolId={"CLK_PCK" + props.tabTitle + "_FREQUENCY"}
        className={props.cx("progrramblrClkFrq")}
        redColorForZeroFrequency
      />
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={"CLK_PCK" + props.tabTitle + "_PRES"}
        className={props.cx("clk_pckx_css")}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={"CLK_PCK" + props.tabTitle + "_EN"}
        className={props.cx("clk_pckx_en")}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={gclkSel}
        classPrefix={"clk_pckx_css"}
        labelClassPrefix={"clk_pckx_css_l"}
        classResolver={props.cx}
      />

      <SettingsDialog
        tooltip={'PCLK ' + props.tabTitle + ' Settings Configuration'}
        componentId={props.componentId}
        className={props.cx('proClkSetting')}
        symbolArray={props.gclkSettingsSymbolArray}
        dialogWidth='47rem'
        dialogHeight='50rem'
      />
      <ResetSymbolsIcon
        tooltip={'PCLK' + props.tabTitle + ' symbols to default value'}
        className={props.cx('proReClkSetting')}
        componentId={props.componentId}
        resetSymbolsArray={props.gclkSettingsSymbolArray}
      />
    </div>
  );
};
export default React.memo(GCKLClockControllerBoxTemplate);
