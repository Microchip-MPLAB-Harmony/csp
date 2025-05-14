import ResetSymbolsIcon from "clock-common/lib/Components/ResetSymbolsIcon";
import ControlInterface from "clock-common/lib/Tools/ControlInterface";
import SettingsDialog from "clock-common/lib/Components/SettingsDialog";
import { useContext } from "react";
import {
  CheckBox,
  InputNumber,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import FrequencyLabelComponent from "clock-common/lib/Components/LabelComponent/FrequencyLabelComponent";

const settingsArray = ["CLK_USB_USBS","CLK_USB_EN","CLK_USB_USBDIV",];

const USBClockController = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = "core" } = useContext(PluginConfigContext);
  const clk_usb_usbs = useKeyValueSetSymbol({
    componentId,
    symbolId: "CLK_USB_USBS",
  });


  const clk_usb_en = useBooleanSymbol({
    componentId,
    symbolId: "CLK_USB_EN",
  });

  const clk_usb_usbdiv = useIntegerSymbol({
    componentId,
    symbolId: "CLK_USB_USBDIV",
  });
  return (
    <div>
      <CheckBox
        booleanSymbolHook={clk_usb_en}
        className={props.cx("clk_usb_en")}
      />
      <FrequencyLabelComponent
        className={props.cx("clk_uhp48m")}
        componentId={componentId}
        symbolId="CLK_UHP48M"
        redColorForZeroFrequency
      />
      <InputNumber
        integerSymbolHook={clk_usb_usbdiv}
        className={props.cx("clk_usb_usbdiv")}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={clk_usb_usbs}
        classPrefix="clk_usb_usbs"
        classResolver={props.cx}
      />
      <label style={{fontWeight:clk_usb_usbs.selectedOption==="PLLA"?'bold':''}} className={props.cx("clk_usb_usbs_l0")}>PLLACK</label>
      <label style={{fontWeight:clk_usb_usbs.selectedOption==="UPLL"?'bold':''}} className={props.cx("clk_usb_usbs_l1")}>UPLLCK</label>
      <label style={{fontWeight:clk_usb_usbs.selectedOption==="MAINXTAL"?'bold':''}} className={props.cx("clk_usb_usbs_l2")}>MAINXTALCK</label>
      <label className={props.cx("usbDivLabel")}>/ {`(${clk_usb_usbdiv.value} + 1)`}</label>
      <SettingsDialog
        tooltip="Advanced Settings"
        componentId={componentId}
        className={props.cx("usbSetting")}
        symbolArray={settingsArray}
        dialogWidth="50rem"
        dialogHeight="47rem"
      />
      <ResetSymbolsIcon
        tooltip="Reset Clock symbols to default value"
        className={props.cx("usbReSetting")}
        componentId={componentId}
        resetSymbolsArray={settingsArray}
      />
    </div>
  );
};

export default USBClockController;
