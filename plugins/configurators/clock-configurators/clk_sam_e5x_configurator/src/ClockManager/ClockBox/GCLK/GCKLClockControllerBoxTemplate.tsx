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
    symbolId: "GCLK_" + props.tabTitle + "_SRC",
  });
  const gclkDiv = useIntegerSymbol({
    componentId,
    symbolId: "GCLK_" + props.tabTitle + "_DIVIDER_VALUE",
  });
  const gclkEnable = useBooleanSymbol({
    componentId: componentId,
    symbolId: "GCLK_INST_NUM" + props.tabTitle,
  });

  return (
    <div>
      <PlainLabel
        disPlayText={gclkDiv.value + ""}
        className={props.cx(props.gclkDivLabelClassName)}
      />
      <InputNumberDefault
        componentId={props.componentId}
        symbolId={"GCLK_" + props.tabTitle + "_DIV"}
        className={props.cx(props.gclKinputNumberClassName)}
      />
      <CheckBoxDefault
        componentId={props.componentId}
        symbolId={"GCLK_INST_NUM" + props.tabTitle}
        className={props.cx(props.gclkEnableClassName)}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={gclkSel}
        classPrefix={props.gclkRadioName}
        labelClassPrefix={props.gclkRadioLabelName}
        classResolver={props.cx}
      />
      {gclkEnable.value === true && (
        <FrequencyLabelComponent
          componentId={props.componentId}
          symbolId={"GCLK_" + props.tabTitle + "_FREQ"}
          redColorForZeroFrequency={true}
          className={props.cx(props.gclkFrequencyClassName)}
        />
      )}
      <SettingsDialog
        tooltip={"GCLK " + props.tabTitle + " Settings Configuration"}
        componentId={props.componentId}
        className={props.cx(props.gclKsettingsClassName)}
        symbolArray={props.gclkSettingsSymbolArray}
        dialogWidth="55rem"
        dialogHeight="45rem"
      />
      <ResetSymbolsIcon
        tooltip={"GCLK " + props.tabTitle + " symbols to default value"}
        className={props.cx(props.gclkresetClassName)}
        componentId={props.componentId}
        resetSymbolsArray={props.gclkSettingsSymbolArray}
      />
    </div>
  );
};
export default React.memo(GCKLClockControllerBoxTemplate);
