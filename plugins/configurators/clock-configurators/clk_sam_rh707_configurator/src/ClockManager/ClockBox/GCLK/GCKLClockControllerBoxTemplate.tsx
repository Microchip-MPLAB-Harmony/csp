import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import {
  CheckBoxDefault,
  InputNumberDefault,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
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
  gclKsettingsClassName: string;
  gclkresetClassName: string;
  gclKinputNumberClassName: string;
  gclkEnableClassName: string;
  gclkFrequencyClassName: string;
  gclkDivLabelClassName: string;
  gclkRadioName: string;
  gclkRadioLabelName: string;
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
  const gclkEnable = useBooleanSymbol({
    componentId: componentId,
    symbolId: "CLK_PCK" + props.tabTitle + "_EN",
  });
  const settingsArray = [
    "CLK_PCK" + props.tabTitle + "_EN",
    "CLK_PCK" + props.tabTitle + "_PRES",
    "CLK_PCK" + props.tabTitle + "_CSS",
  ];
 
  return (
    <div>
      <PlainLabel
        disPlayText={gclkDiv.value +1+ ""}
        className={props.cx('clk_pck_pres_lbl')}
        booldStatus={true}
      />
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={"CLK_PCK" + props.tabTitle + "_PRES"}
        className={props.cx('clk_pck_pres')}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={"CLK_PCK" + props.tabTitle + "_EN"}
        className={props.cx('clk_pck_en')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={gclkSel}
        classPrefix={'clk_pck_css'}
        classResolver={props.cx}
      />

      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={"CLK_PCK" + props.tabTitle  + "_FREQ"}
        redColorForZeroFrequency={true}
        className={props.cx('progrramblrClkFrq')}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={"CLK_MD_SLCK_FREQ"}
        boldLabelStatus={gclkSel.value===0}
        className={props.cx('programClkSlowLbl')}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={"CLK_MAINCK_FREQ"}
        boldLabelStatus={gclkSel.value===1}
        className={props.cx('programClkMainLbl')}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={"CLK_PLLACK_FREQ"}
        boldLabelStatus={gclkSel.value===2}
        className={props.cx('programClkPllaLbl')}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={"CLK_PLLBCK_FREQ"}
        boldLabelStatus={gclkSel.value===3}
        className={props.cx('programClkPllbLbl')}
      />
      <FrequencyLabelComponent
        componentId={props.componentId}
        symbolId={"CLK_MCK_FREQ"}
        boldLabelStatus={gclkSel.value===4}
        className={props.cx('programClkMckLbl')}
      />
      {/* <SettingsDialog
        tooltip={'GCLK ' + props.tabTitle + ' Settings Configuration'}
        componentId={props.componentId}
        className={props.cx(props.gclKsettingsClassName)}
        symbolArray={props.gclkSettingsSymbolArray}
        dialogWidth='47rem'
        dialogHeight='50rem'
      /> */}
      <ResetSymbolsIcon
        tooltip={"PCK " + props.tabTitle + " symbols to default value"}
        className={props.cx("pcReset")}
        componentId={props.componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};
export default React.memo(GCKLClockControllerBoxTemplate);
