import {
  GetLabelWithCustomDisplay,
  GetStyle,
  globalSymbolStyleData,
} from "../../Common/UIComponent";
import { GetSymbolValue } from "../../Common/SymbolAccess";
import { component_id } from "./MainBlock";

export function AddCustomLabels() {
  try {
    return (
      <div>
        {AddLabel("label_enableGenerator", "Enable Generator Initialization")}

        {/* {AddLabel("label_externalClockFreq","/" )} */}
        {/* {AddLabel("label_startupTime","Label" )} */}
        {/* {AddLabel("label_externalClockXTALFreq","Label" )} */}

        {AddDiv(
          "label_pclkPres",
          GetSymbolValue(component_id, "CLK_CPU_CKR_PRES")
        )}
        {AddDiv(
          "label_pclkMdiv",
          GetSymbolValue(component_id, "CLK_CPU_CKR_MDIV")
        )}

        {AddMDivType(
          "label_pclk_1",
          GetSymbolValue(component_id, "CLK_CPU_CKR_MDIV")
        )}

        {AddDivioType(
          "label_usbdivVal",
          GetSymbolValue(component_id, "CLK_USB_USBDIV")
        )}

        {AddDivpmcType(
          "label_pllaDivpmcVal",
          GetSymbolValue(component_id, "CLK_PLLA_DIVPMC")
        )}

        {AddDivpmcType(
          "label_audioPllDivpmcVal",
          GetSymbolValue(component_id, "CLK_AUDIOPLL_DIVPMC")
        )}
        {AddDivioType(
          "label_audiopllDivioVal",
          GetSymbolValue(component_id, "CLK_AUDIO_IOPLLCK_DIVIO")
        )}

        {AddDivpmcType(
          "label_lvdspllDIVPMCVal",
          GetSymbolValue(component_id, "CLK_LVDSPLL_DIVPMC")
        )}

        {AddBoldLabel(
          "label_MD_SLCK",
          "MD_SLCK",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "SLOW_CLK")
        )}
        {AddBoldLabel(
          "label_MAINCK",
          "MAINCK",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "MAIN_CLK")
        )}
        {AddBoldLabel(
          "label_PLLACK",
          "PLLACK",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "PLLACK")
        )}
        {AddBoldLabel(
          "label_UPLLACK",
          "UPLLCK",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "UPLLCK")
        )}

        {AddBoldLabel(
          "label_usb_PLLACK",
          "PLLACK",
          CheckSelectedSymbolValue("CLK_USB_USBS", "PLLA")
        )}
        {AddBoldLabel(
          "label_usb_UPLLCK",
          "UPLLCK",
          CheckSelectedSymbolValue("CLK_USB_USBS", "UPLL")
        )}
        {AddBoldLabel(
          "label_MAINXTLCK",
          "MAINXTLCK",
          CheckSelectedSymbolValue("CLK_USB_USBS", "MAINXTAL")
        )}
      </div>
    );
  } catch (err) {}
}

export function CheckSelectedSymbolValue(symbolId: string, checkValue: string) {
  if (GetSymbolValue(component_id, symbolId) === checkValue) {
    return true;
  } else {
    return false;
  }
}

export function AddBoldLabel(
  id: string,
  text: string,
  symbolSelectionStatus: boolean
) {
  try {
    let style: Map<string, string> | undefined = globalSymbolStyleData.get(id);
    if (style !== undefined) {
      if (symbolSelectionStatus === true) {
        style.set("font-weight", "bold");
      } else {
        style.set("font-weight", "normal");
      }
    }
    return <div>{AddLabelWithCustomStyle(id, text, style)}</div>;
  } catch (err) {}
}

function AddDivpmcType(id: string, text: string) {
  try {
    let newvalue = "( " + text + " + 1 )";
    return <div>{AddLabel(id, "/ " + newvalue)}</div>;
  } catch (err) {}
}

export function AddDivioType(id: string, text: string) {
  try {
    let newvalue = "( " + text + " + 1 )";
    return <div>{AddLabel(id, "/ " + newvalue)}</div>;
  } catch (err) {}
}

export function AddMDivType(id: string, text: string) {
  try {
    let newValue = text.replace(/^\D+/g, "");
    let val = 1;
    if (newValue.length > 0) {
      if (+newValue > 1) {
        val = +newValue / 2;
      }
    }
    return <div>{AddLabel(id, "/ " + val)}</div>;
  } catch (err) {}
}

function AddDiv(id: string, text: string) {
  try {
    let divValue = RemoveDiv(text);
    divValue = divValue.replace("DIV", "");
    return <div>{AddLabel(id, "/ " + divValue)}</div>;
  } catch (err) {}
}

function AddLabel(id: string, text: string) {
  try {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={id}
          labelDisplayText={text}
          labelStyle={GetStyle(id)}
        />
      </div>
    );
  } catch (err) {}
}

function AddLabelWithCustomStyle(id: string, text: string, styleMap: any) {
  try {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={id}
          labelDisplayText={text}
          labelStyle={Object.fromEntries(styleMap)}
        />
      </div>
    );
  } catch (err) {}
}

function RemoveDiv(value: string) {
  let newValue = value.split("_");
  return newValue[1];
}
